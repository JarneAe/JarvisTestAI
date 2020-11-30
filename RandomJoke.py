import pyjokes
from Narrator import Narrator

def getJoke():
    narrator = Narrator(pyjokes.get_joke())
    narrator.narrator()
    return True