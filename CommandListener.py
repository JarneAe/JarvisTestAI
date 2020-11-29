from Narrator import Narrator
from GetDate import getDate


class CommandListener:

    # Initialize userInput variable.
    def __init__(self, userInput):
        self.userInput = userInput

    # Function to format and split the user input.
    def formatInput(self):
        loweredUserInput = self.userInput.lower()
        splitUserInput = loweredUserInput.split()

        return splitUserInput

    # Actual CommandListener with the command lists.
    def commandListener(self):
        formattedInput = self.formatInput()
        COMMANDS = ["say", "exit"]
        DATE_CMDS = ["today", "date", "day"]

        for cmds in COMMANDS:
            if formattedInput[0] in cmds:
                if formattedInput[0] == "say":
                    slicedList = formattedInput[1:]
                    narrator = Narrator(" ".join(slicedList))
                    narrator.narrator()
                if formattedInput[0] == "exit":
                    exit()
        dateSnippets = formattedInput.copy()
        for dateCmds in DATE_CMDS:
            for snippets in dateSnippets:
                if snippets in dateCmds:
                    dateSnippets.clear()
                    getDate()

        return True
