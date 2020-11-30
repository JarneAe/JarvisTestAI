import speech_recognition as sr


def recordAudio():

    # Obtain audio from the microphone
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print('>')
        audio = recognizer.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        print("I think you said: " + recognizer.recognize_google(audio, language="en-GB"))
    except sr.UnknownValueError:
        raise sr.UnknownValueError("Google Speech Recognition could not understand audio") from None
    except sr.RequestError as e:
        raise sr.RequestError("Could not request results from Google Speech Recognition service; {0}".format(e)) from None

    if recognizer.recognize_google(audio, language="en-GB").lower() == "good morning":
        inputUser = "goodmorning"
    else:
        inputUser = recognizer.recognize_google(audio, language="en-GB").lower()

    return inputUser
