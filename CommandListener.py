from Narrator import Narrator

class CommandListener():

    def __init__(self, userInput):
        self.userInput = userInput

    def formatInput(self):
        loweredUserInput = self.userInput.lower()
        splitUserInput = loweredUserInput.split()

        return splitUserInput

    def commandListener(self):
        formattedInput = self.formatInput()
        COMMANDS = ["say"]

        for cmds in COMMANDS:
            if formattedInput[0] in cmds:
                if formattedInput[0] == "say":
                    slicedList = formattedInput[1:]
                    narrator = Narrator(" ".join(slicedList))
                    narratorCall = narrator.narrator()

        return True