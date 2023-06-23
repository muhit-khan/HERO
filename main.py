import speech_recognition as sr
import pyttsx3
from bardapi import Bard
import os
from speech_utils import speak, take_confirmation, take_command

# Set Bard API key
os.environ['_BARD_API_KEY'] = "XwgSsb1-u89sDYgBeVkbC3yP69J98Z_Qi-IUKah9sWTCqT_jEdeCP9FAhAd5QDeg1_53ww." #use your own API key

# Running VA
speak("Hey, I am your 'Hero' here! How can I help you?")

while True:
    cmd = take_command()
    if cmd == 'exit':  # Termination command to stop the loop
        speak('I am leaving for now. If you need any help, run me again. Thank you!')
        break
    message = Bard().get_answer(cmd)['content']
    message = message.replace('Bard', 'Hero')
    message = message.replace('bard', 'Hero')
    print(message)
    speak(message)
