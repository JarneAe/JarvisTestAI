from datetime import datetime
from Narrator import Narrator

def getTime():
    now = datetime.now()

    currentTime = now.strftime("%H:%M")
    narrator = Narrator("The current time is: " + currentTime)
    narrator.narrator()
