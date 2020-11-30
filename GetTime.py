from datetime import datetime
from Narrator import Narrator


def getTime():

    # Instantiate the time class
    now = datetime.now()

    # Declare the current time variable
    currentTime = now.strftime("%H:%M")

    # Pass the arguments in a string and let the narrator say it
    narrator = Narrator("The current time is: " + currentTime)
    narrator.narrator()

    return True
