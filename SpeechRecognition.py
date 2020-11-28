import speech_recognition as sr


class SpeechRecognition():

    def recordAudio(self):

        # Obtain audio from the microphone
        recognizer = sr.Recognizer() 
        with sr.Microphone() as source:
            print('>')
            audio = recognizer.listen(source)

        # Recognize speechs using Google Speech Recogniton
        try:
            print("I think you said: " + recognizer.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return recognizer.recognize_google(audio)