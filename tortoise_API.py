# https://www.cloudbooklet.com/tortoise-tts-a-new-text-to-speech-system/

#Installation
# git clone https://github.com/neonbjb/tortoise-tts.git
# cd tortoise-tts
# pip install -r requirements.txt
# pip install librosa einops rotary_embedding_torch omegaconf pydub inflect
# python setup.py install

import torchaudio
import tortoise.api as api
import tortoise.utils as utils
import os

# If you want to use deepspeed the pass use_deepspeed=True nearly 2x faster than normal
# tts = api.TextToSpeech(use_deepspeed=True, kv_cache=True) #In practice slower!
##Took ~1h with default, ~3h with HQ, 7h with standard

# This is the text that will be spoken.
# text = "Joining two modalities results in a surprising increase in generalization! What would happen if we combined them all?"
text="And this is another version of deepfakes, called faceswap. Here we can see my face being placed on top of one of my PhD students."

# Pick a "preset mode" to determine quality. Options: {"ultra_fast", "fast" (default), "standard", "high_quality"}. See docs in api.py
preset = "high_quality"  
# Pick one of the voices - These files copied there for the speaker we want to clone
voice = '/home/soyrl/tortoise-tts/tortoise/voices/pvo/'

clips_paths=[voice+os.listdir(voice)[i] for i in range(len(os.listdir(voice)))]
reference_clips = [utils.audio.load_audio(p, 22050) for p in clips_paths]
# This will download all the models used by Tortoise from the HF hub.
tts = api.TextToSpeech() #35min - fast, 2.4h - HQ
pcm_audio = tts.tts_with_preset(text, voice_samples=reference_clips, preset=preset)
torchaudio.save('/home/soyrl/generated_hq_faceswap.wav', pcm_audio.squeeze(0).cpu(), 24000)