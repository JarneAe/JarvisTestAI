import randfacts
import random
from Narrator import Narrator

def getfact():
    sayings = ['Here\'s a random fact: ', 'Did you know that: ', 'here\'s a fun fact for you: ']
    x = randfacts.getFact()
    narrator = Narrator(random.choice(sayings) + x)
    narrator.narrator()
    return True
