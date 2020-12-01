import randfacts
import random
from Narrator import Narrator


def getFact():

    # Instantiate a few default output formats for the narrator
    sayings = ['Here\'s a random fact: ', 'Did you know that: ', 'here\'s a fun fact for you: ']

    # Get a random value for x
    x = randfacts.getFact()

    # Inputs arguments and lets the narrator say it
    print((random.choice(sayings) + x))
    narrator = Narrator(random.choice(sayings) + x)
    narrator.narrator()

    return True
