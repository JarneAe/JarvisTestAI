import pyjokes
from Narrator import Narrator


def getJoke():
    # Inputs arguments and lets the narrator say it
    joke = pyjokes.get_joke()
    print(joke)
    narrator = Narrator(joke)
    narrator.narrator()
    return True
