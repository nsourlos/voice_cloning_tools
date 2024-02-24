#Clone a voice with coqui TTS API (takes ~10secs) - After a point it is charged (https://coqui.ai/pricing/)

#Import libraries
import requests
import os

#Path of audio file
path_audio=os.getcwd()+ "/input_audio.mp3" #Path of audio file - English audio works better than Greek

save_path=os.getcwd()+ "/speech_to_txt.wav" #Path to save the new audio file

text_to_read="Dear Christos, Luiz, and George-Dukas, I would like to give you my wishes for your marriage and baptism. \
    There is a rumor that this will bring you bad luck, but I hope it won't.  Nevertheless, I would like you to always be happy \
    and always have love in your life." #Text to read - Greek text will result in error - will try to spell each letter. 

#First call API to clone a voice
url = "https://app.coqui.ai/api/v2/voices/clone-from-file/"

files = {"file": (path_audio, open(path_audio, "rb"), "audio/mpeg")} #Open audio file
payload = {"name": "temp"} #Just a temporary name
headers = { #Headers needed for the API call
    "accept": "application/json",
    "authorization": "Bearer xxxxxxxxxxx"} #API key - Get it from the website

response = requests.post(url, data=payload, files=files, headers=headers) #Result of the API call
# print(response.text)
voice_id=response.text.split('"id":')[1].split('"')[1] #Voice ID of the cloned voice - Used below for txt-to-speech
print("Voice ID is:",voice_id)


#Using the above voice_id, call API for text-to-speech
url = "https://app.coqui.ai/api/v2/samples"

payload = {
    "emotion": "Neutral",
    "speed": 1, #2 is faster, 0 is slower (currently doesn't work)
    "voice_id": voice_id, #Voice id from above
    "name": "temp", #Temporary name
    "text": text_to_read}

headers = {
    "accept": "application/json",
    # "content-type": "application/json",
    "authorization": "Bearer xxxxxxxxxxx" #API key - Get it from the website
}

response = requests.post(url, json=payload, headers=headers) #Result of the API call
# print(response.text)

wav_url=response.text.split('"audio_url":')[1].split('"')[1] #Audio url of the new audio file
print("Audio link in:", wav_url)

#Download file from url
print("Downloading audio file and saving to:", save_path)
r = requests.get(wav_url, allow_redirects=True)
open(save_path, 'wb').write(r.content)