from playsound import playsound
from gtts import gTTS
import os


class Narrator:

    # Initialize the inputUser variable
    def __init__(self, inputUser):
        self.inputUser = inputUser

    # Outputs the given input in a text to speech format.
    def narrator(self):
        narratorOutput = gTTS(text=self.inputUser, lang="en-ph", slow=False)
        narratorOutput.save("narrator.mp3")
        playsound("narrator.mp3")
        os.remove("narrator.mp3")

        return True
