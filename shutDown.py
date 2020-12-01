import subprocess
from Narrator import Narrator
import random


class shutdown:

    def __init__(self,inputUser):
        self.inputUser = inputUser



    def shutdown(self):

        shutdownSentences = ["Goodbye sir","Goodnight sir","Edith shutting down system"]
        
        
        print("Are you sure?")
        narrator = Narrator("Are you sure?")
        narrator.narrator()

        if self.inputUser == "yes":
            text = random.choice(shutdownSentences)
            print(text)
            narrator = Narrator(text)
            narrator.narrator()
            subprocess.call(["shutdown" , "/s"])
        elif self.inputUser == "no":
            pass
        else:
            print("I did not quite understand that.")
            narrator = Narrator("I did not quite understand that.")
            narrator.narrator()

