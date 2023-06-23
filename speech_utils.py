import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
speaker = pyttsx3.init()


def speak(text):
    """
    Converts the given text into speech and plays it.

    Args:
        text (str): The text to be spoken.
    """
    speaker.say(text)
    speaker.runAndWait()


def take_confirmation():
    """
    Prompts the user for confirmation using speech recognition.

    Returns:
        str: The user's confirmation ('yes' or 'no').
    """
    try:
        with sr.Microphone() as source:
            print("\n\nListening....\n\n")
            speak('Do you need help?')
            # Optional: Adjust for ambient noise
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=10, phrase_time_limit=15)
            confirmation = listener.recognize_google(voice)
            confirmation = confirmation.lower()
            if 'yes' in confirmation:
                confirmation = 'yes'
            if 'no' in confirmation:
                confirmation = 'no'
    except:
        confirmation = 'no'
        pass
    return confirmation


def take_command():
    """
    Listens to user input and converts it into a command using speech recognition.

    Returns:
        str: The user's command.
    """
    try:
        with sr.Microphone() as source:
            print("\n\nListening....\n\n")
            # Optional: Adjust for ambient noise
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=15, phrase_time_limit=40)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hero' in command:
                command = command.replace('hero', '')
    except sr.WaitTimeoutError:
        speak("Sorry, I didn't hear anything.")
        if take_confirmation() == 'yes':
            return take_command()
        else:
            command = 'exit'
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand you.")
        if take_confirmation() == 'yes':
            return take_command()
        else:
            command = 'exit'
    except sr.RequestError:
        speak("Sorry, I'm having trouble accessing the speech recognition service.")
        if take_confirmation() == 'yes':
            return take_command()
        else:
            command = 'exit'
    return command
