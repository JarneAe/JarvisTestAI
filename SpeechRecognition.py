import speech_recognition as sr
from Narrator import Narrator


def recordAudio():

    # Obtain audio from the microphone
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print('>')
        audio = recognizer.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        print("I think you said: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return recognizer.recognize_google(audio)
