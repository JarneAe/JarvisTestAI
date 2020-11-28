from playsound import playsound
from gtts import gTTS
import os

class Narrator():

    def __init__(self, inputUser):
        self.inputUser = inputUser

    # Output
    def narrator(self):

        narratorOutput = gTTS(text = self.inputUser, lang = "en", slow = False)
        narratorOutput.save("narrator.mp3")
        playsound("narrator.mp3")

        return True