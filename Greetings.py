import random   
from Narrator import Narrator

def greetings():
    greetings = ["hello","Greetings","Goodmorning sir","Jarvis on standby","Good day"]

    narrator = Narrator(random.choice(greetings))
    narrator.narrator()
