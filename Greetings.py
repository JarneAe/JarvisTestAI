import random
from Narrator import Narrator


def greetings():
    PREDEFINED_GREETINGS = ["hello", "greetings", "goodmorning sir", "jarvis on standby", "good day"]

    narrator = Narrator(random.choice(PREDEFINED_GREETINGS))
    narrator.narrator()

    return True
