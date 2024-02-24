# python version is 3.10
# pip install TTS==0.22.0 #This is the latest, also 0.20.6 worked (0.14.0 for xtts v1 and tortoise)
# pip install transformers==4.37.2 (4.29.2 for earlier versions of TTS)

#Code below taken from: https://tts.readthedocs.io/en/latest/models/tortoise.html
#Deepspeed doesn't work. More information can be found in https://docs.coqui.ai/en/latest/models/xtts.html
#For non-tts API (not used here), models downloaded from https://huggingface.co/jbetker/tortoise-tts-v2/tree/main/.models

import torch
import torchaudio

text="Joining two modalities results in a surprising increase in generalization! What would happen if we combined them all?"

#XTTS v2.0.2 from coqui (takes <30secs)
#Run with just 6 sec of audio and result of good quality

from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init TTS - Alternative is 'xtts_v1.1' or 'tts_models/multilingual/multi-dataset/xtts_v2', but not that good
#Only works well for 1-2 small sentences - 24khz sampling rate
tts = TTS("xtts_v2.0.2").to(device) #gpu=True should not be used anymore

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech to a file
tts.tts_to_file(text=text, speaker_wav="opus_combined.mp3", language="en", file_path="coqui_xtts_v2.0.2_split_false.wav", split_sentences=False) 
tts.tts_to_file(text=text, speaker_wav="opus_combined.mp3", language="en", file_path="coqui_xtts_v2.0.2_split_true.wav", split_sentences=True) 



#Below needed to create folder used by Tortoise

# Prompt: Read an mp3 file using soundfile and return a folder with wav files named 1.wav, 2.wav etc., etc one being a 10 sec segment of the original audio. 
# Take these segments one after the other until all the audio in the original mp3 file is used.
# do not use pydub library at all. Find an alternative

import soundfile as sf
import librosa
import os

def mp3_to_wav(input_mp3, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the MP3 file using librosa
    audio, sr = librosa.load(input_mp3, sr=None, mono=True)

    # Calculate the duration of each segment (10 seconds)
    segment_duration = 10  # in seconds

    # Convert segment duration to samples
    segment_samples = int(segment_duration * sr)

    # Create 10-second segments and save as WAV files
    for i in range(0, len(audio), segment_samples):
        segment = audio[i:i + segment_samples]

        # Save the segment as WAV using soundfile
        output_wav = os.path.join(output_folder, f"{i // segment_samples + 1}.wav")
        sf.write(output_wav, segment, sr)

    print(f"Conversion completed. {i // segment_samples} segments created in {output_folder}")

# Example usage
input_mp3 = '/home/soyrl/input_file.mp3'
output_folder = '/home/soyrl/output_folder'

mp3_to_wav(input_mp3, output_folder)



#BEST - Tortoise Fastest Inference from script (~7min) - Can also be downloaded from https://huggingface.co/jbetker/tortoise-tts-v2/tree/main
from TTS.tts.configs.tortoise_config import TortoiseConfig
from TTS.tts.models.tortoise import Tortoise

config = TortoiseConfig()
model = Tortoise.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="/home/soyrl/.local/share/tts/tts_models--en--multi-dataset--tortoise-v2", eval=True) 
# cloning a speaker
output_dict = model.synthesize(text, config, speaker_id="zof", voice_dirs="/home/soyrl/")

#Save result
torchaudio.save("tortoise_v2_script.wav", torch.tensor(output_dict["wav"]).squeeze(0), 24000)

# ........................................................................................................................................

# #XTTS_v2 - Not as good as the latest version above or Tortoise
# # Can downloaded manually from https://huggingface.co/coqui/XTTS-v2 or with the code below:
# # git lfs install
# # git clone https://huggingface.co/coqui/XTTS-v2

# #Taken from https://docs.coqui.ai/en/latest/models/xtts.html
# # import torch
# # import torchaudio
# import os

# from TTS.tts.configs.xtts_config import XttsConfig
# from TTS.tts.models.xtts import Xtts

# print("Loading model...")
# config = XttsConfig()
# config.load_json("/home/soyrl/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v2/config.json")#XTTS_v2/config.json")
# model = Xtts.init_from_config(config)
# model.load_checkpoint(config, checkpoint_dir="/home/soyrl/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v2", eval=True)  
# #Also works with .local/share/tts/tts_models--multilingual--multi-dataset--xtts_v2.0.2

# model.cuda()

# print("Computing speaker latents...")
# gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=["/home/soyrl/audio.mp3"])

# print("Inference...")
# out = model.inference(
#     text,
#     "en",
#     gpt_cond_latent,
#     speaker_embedding,
#     temperature=0.7 # Add custom parameters here
# )

# print("Saving audio...")
# torchaudio.save("xtts_v2_script.wav", torch.tensor(out["wav"]).unsqueeze(0), 24000)


#Tortoise - Best quality but takes the longest (2+ hours)
# from TTS.api import TTS
# import time
# start=time.time()
# tts = TTS("tts_models/en/multi-dataset/tortoise-v2")

# path_with_voice_samples='/home/soyrl/'
# speaker_name='pvo' #Path with audio file samples (10 secs each) of the person to be cloned

# # cloning voice - Took 1-2h for all 3 below in CPU, 11.5mins in GTX 1660TI 6GB GPU - 3h40mins
# tts.tts_to_file(text=text,
#                 file_path=path_with_voice_samples+"modalitites_local_new.wav",
#                 voice_dir=path_with_voice_samples, #tortoise-tts/tortoise/voices
#                 speaker=speaker_name,
#                 num_autoregressive_samples=500, #more samples means a higher probability of creating something “great”
#                 diffusion_iterations=250,
#                 preset="high_quality") #Number of diffusion steps to perform. [0,4000]. More steps means the network has more chances to 
#                                         #iteratively refine the output, which should theoretically mean a higher quality output. 
#                                         #Generally a value above 250 is not noticeably better, however. Defaults to 30.
# end=time.time()
# print("Total time taken: ", end-start)


# # Using presets with the same voice 
# # presets are a collection of processing settings that have been pre-configured to achieve a specific sound or effect on a vocal recording
# tts.tts_to_file(text=text,
#                 file_path=path_with_voice_samples+"output_fast.wav",
#                 voice_dir=path_with_voice_samples,
#                 speaker=speaker_name,
#                 preset="fast") #"standard", "high_quality" and can even use emotion='Happy',speed=0.5