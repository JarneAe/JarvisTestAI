import speech_recognition as sr


class SpeechRecognition():

    def recordAudio(self):

        # Sphinx thinks you said
        recognizer = sr.Recognizer() 
        with sr.Microphone() as source:
            print('>')
            audio = recognizer.listen(source)

        # Recognize speechs using Sphinx
        try:
            print('I think you said: ' + recognizer.recognize_sphinx(audio))
        except sr.UnknownValueError: 
            print('Sphinx could not understand audio.')
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        return recognizer.recognize_sphinx(audio)