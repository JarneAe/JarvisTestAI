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
        print("I think you said: " + recognizer.recognize_google(audio, language="en-ph"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        recordAudio()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        exit()

    # Concatenate the words good and morning once triggered
    if recognizer.recognize_google(audio, language="en-ph").lower() == "good morning":
        inputUser = "goodmorning"
    else:
        inputUser = recognizer.recognize_google(audio, language="en-ph").lower()

    return inputUser
