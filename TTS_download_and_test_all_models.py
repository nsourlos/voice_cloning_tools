#This script download all models from TTS library that can synthesize text.
#It checks which models are multi-language and have an English vocoder, and how many of them have a custom (allows voice cloning) or default English vocoder.
#It also check the same for English models (default vs custom vocoder), and counts the number of non-English models, and the errors that might emerge.

#Import Libraries
from TTS.api import TTS #pip install TTS==0.13.3
import time
import os

start=time.time() #To keep track of time

#Text to convert to speech
text="Deepfakes are AI generated synthetic videos of any person or celebrity that impersonates the actual person and makes them act or say anything they \
originally never did. The process of creation of deepfakes is technically complex and generally requires a vast amount of data which is then fed to a neural \
network to train and generate the synthetic video."

#Set parameters to 0 to count different types of models (see below). Same for models with errors and those that should be ignored.
multi_voice_clone=0 #Multi-language model with English vocoder (allows voice cloning of the input voice)
en_voice_clone=0 #English model with custom English vocoder (allows voice cloning)
multi_default_voc=0 #Multi-language with default English vocoder (no voice cloning)
en_default_voc=0 #English model with default English vocoder (no voice cloning)
other_languages=0 #Other languages
error=0 #Models with errors
ignored=0 #Models that should be ignored (due to errors or other reasons)

#To keep track of their names
multi_voice_clone_list=[]
en_voice_clone_list=[]
multi_default_voc_list=[]
en_default_voc_list=[]
other_languages_list=[]
error_list=[]
ignored_list=[]

for model in TTS.list_models(): #Loop over all TTS models

    if 'en/ek1' not in model: #This model gives error and so, it should be ignored
        if '/en' in model or 'multi' in model or 'univer' in model: #models that support English - If ['/el' in model] gives voice with gibberish (use only in Colab)

            tts = TTS(model_name=model) #Download and load the model - can also use gpu=True argument - No arguments to make it less verbose

            try: #If the model is multi-language and has an English vocoder (for txt-to-speech of a given input audio/voice cloning)
                tts.tts_to_file(text=text, speaker_wav=os.getcwd()+"/input_audio.mp3", language="en", file_path="output_en_"+''.join(model.split('/'))+".wav")
                multi_voice_clone=multi_voice_clone+1
                multi_voice_clone_list.append(model)

            except: #If above results in error
                try: #If the model is English only and has a custom English vocoder for voice cloning
                    tts.tts_to_file(text=text, speaker_wav=os.getcwd()+"/input_audio.mp3", file_path="output_en_"+''.join(model.split('/'))+".wav")
                    en_voice_clone=en_voice_clone+1
                    en_voice_clone_list.append(model)

                except:
                    try: #If the model is multi-language and has a default English vocoder (no voice cloning)
                        tts.tts_to_file(text=text, language="en", file_path="output_en_"+''.join(model.split('/'))+".wav")
                        multi_default_voc=multi_default_voc+1
                        multi_default_voc_list.append(model)

                    except:
                        try: #If the model supports only English and has a default English vocoder (no voice cloning)
                            tts.tts_to_file(text=text, file_path="output_en_"+''.join(model.split('/'))+".wav")
                            en_default_voc=en_default_voc+1
                            en_default_voc_list.append(model)

                        except: #In any other case there is error
                            error=error+1
                            error_list.append(model)

        else: #If the model does not support English
            other_languages=other_languages+1
            other_languages_list.append(model)

    else: #If the model contains 'en/ek1' it will be ignored since it will give an error
        ignored=ignored+1
        ignored_list.append(model)


print("There were", len(TTS.list_models()),"TTS models checked")
print("\n")
print(multi_voice_clone,"Multi-language models with English vocoder for voice cloning:",multi_voice_clone_list)
print("\n")
print(en_voice_clone,"English models with custom vocoder for voice cloning:",en_voice_clone_list)
print("\n")
print(multi_default_voc,"Multi-language models with a default English vocoder (no voice cloning):",multi_default_voc_list)
print("\n")
print(en_default_voc,"English models with default English vocoder (no voice cloning):",en_default_voc_list)
print("\n")
print(other_languages,"models of non-English languages:",other_languages_list)
print("\n")
print(error,"models with errors:",error_list)
print("\n")
print(ignored,"models ignored:",ignored_list)
print("\n")

end=time.time()
print("Time taken:",end-start) #Took ~300secs (3min with models already downloaded)

assert len(TTS.list_models())==multi_voice_clone+en_voice_clone+multi_default_voc+en_default_voc+other_languages+error+ignored, \
                                                                                "Something is wrong with the counting of models"

# # Running a multi-speaker and multi-lingual model
# # print(TTS.list_models())
# # List available 🐸TTS models and choose the first one
# model_name = TTS.list_models()[0]
# # Init TTS
# tts = TTS(model_name)
# # print(tts)
# # Run TTS
# # ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
# # Text to speech with a numpy output
# wav = tts.tts("This is a test!", speaker=tts.speakers[0], language=tts.languages[0])
# # Text to speech to a file
# tts.tts_to_file(text="Hello world!", speaker=tts.speakers[0], language=tts.languages[0], file_path="output.wav")


# #For greek txt-to-speech use the model below - Only works in Colab
# pip install TTS==0.13.3
# !sudo apt-get install espeak

# from google.colab import drive
# drive.mount('/content/gdrive')

# from TTS.api import TTS
# model_name="tts_models/el/cv/vits"
# tts = TTS(model_name=model_name)#, progress_bar=True, gpu=False)
# text = "Τι θα θέλατε να παραγγείλετε; Έχουμε σουβλάκια με σως, πατάτες και από πιάτα ημέρας γκιούλμπαστι. Σας αρέσουν;" 
# tts.tts_to_file(text=text, file_path="content/gdrive/MyDrive/ordergr.wav")