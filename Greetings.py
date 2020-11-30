import random
from Narrator import Narrator


def greetings():

    # Predefine a list with predefined greetings Edith can use.
    PREDEFINED_GREETINGS = ["hello", "greetings", "goodmorning sir", "jarvis on standby", "good day"]

    # Pass the arguments in a string and let the narrator say it
    narrator = Narrator(random.choice(PREDEFINED_GREETINGS))
    narrator.narrator()

    return True
