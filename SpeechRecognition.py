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
            print('Google Speech Recognition could not understand you, you dumbass.')
        except sr.RequestError as e:
            print("Request results from Google Speech service error; " + e)

        return recognizer.recognize_sphinx(audio)