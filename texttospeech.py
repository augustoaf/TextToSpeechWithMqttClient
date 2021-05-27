#pip3 install gTTS #google lib - need internet to convert the text to speech 
#pip3 install pyttsx3 #offline lib to convert text to speech
#pip3 playsound # lib to play sound

import gtts
#from playsound import playsound
import pygame

# make request to google to get synthesis 
# you can specify the language as a second argument like: lang="pt-br" for Portuguese Brazil
# to get all available languages along with their IETF tag, use: print(gtts.lang.tts_langs())
tts = gtts.gTTS("Hello world")

# save the audio file
audio_file_name = "speech.mp3"
tts.save(audio_file_name)

# play the audio file
###playsound("speech.mp3") # for some reason this playsound lib is not working
pygame.mixer.init()
pygame.mixer.music.load(audio_file_name)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue