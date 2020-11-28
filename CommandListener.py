from Narrator import Narrator
from GetDate import GetDate

class CommandListener():

    def __init__(self, userInput):
        self.userInput = userInput

    def formatInput(self):
        loweredUserInput = self.userInput.lower()
        splitUserInput = loweredUserInput.split()

        return splitUserInput

    def commandListener(self):
        formattedInput = self.formatInput()
        COMMANDS = ["say", "what is the date"]

        for cmds in COMMANDS:
            if formattedInput[0] in cmds:
                if formattedInput[0] == "say":
                    slicedList = formattedInput[1:]
                    narrator = Narrator(" ".join(slicedList))
                    narratorCall = narrator.narrator()
            elif self.userInput.lower() in cmds:
                narrator = Narrator(GetDate().getDate())
                narratorCall = narratorCall.narrator


        return True