import os

class TranscribeAudio:

    def __init__(self, inputUser):
        self.inputUser = inputUser

    def getAudio(self):
        alreadyRan = []
        directories = os.listdir("AUDIO_FILES")
        for i in range(2):
            if "waveSearch" in alreadyRan:
                searchFile = [self.inputUser, ".mp3"]
                searchFileOther = "".join(searchFile)
            else:
                searchFile = [self.inputUser, ".wav"]
                searchFileWav = "".join(searchFile)
                alreadyRan.append("waveSearch")
        for index in directories:
            if searchFileWav in directories:
                print("Yay, found 1 wave file.")
                # Here comes different class "Scipy"
            else:
                print("Yay, found 1 mp3 file.")
                # Here comes different class "Scipy"

        return True

    def removeNoise(self):
        pass

    def transcriptionAudio(self):
        pass

transcribe = TranscribeAudio("speech")
transcription = transcribe.getAudio()
