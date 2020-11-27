from playsound import playsound
from gtts import gTTS
import os

class Narrator():

    # Functionality: [narrator]
    #
    # Sets an object containing text, language and slow attribute
    # and then converts it to an audio file and saves that to play it.
    def narrator(self, inputUser):

        print(inputUser)

        narratorOutput = gTTS(text = inputUser, lang = "eng", slow = False)
        narratorOutput.save("narrator.mp3")
        playsound("narrator.mp3")