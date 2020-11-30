import pyjokes
from Narrator import Narrator


def getJoke():

    # Inputs arguments and lets the narrator say it
    narrator = Narrator(pyjokes.get_joke())
    narrator.narrator()
    return True
