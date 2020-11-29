from Narrator import Narrator
from GetDate import getDate
from GetTime import getTime
from Greetings import greetings
from Search import Search
from SearchWiki import SearchWiki


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
        LOOKUP_CMDS = ["look up", "who", "where", "when", "what"]
        DATE_CMDS = ["today", "date", "day"]
        TIME_CMDS = ["time"]
        GREET_CMDS = ["hello", "hey", "goodmorning", "jarvis"]

        for cmds in COMMANDS:
            if formattedInput[0] in cmds:
                if formattedInput[0] == "say":
                    slicedList = formattedInput[1:]
                    narrator = Narrator(" ".join(slicedList))
                    narrator.narrator()
                if formattedInput[0] == "exit":
                    exit()
        inputSnippets = formattedInput.copy()
        for dateCmds in DATE_CMDS:
            for snippets in inputSnippets:
                if snippets in dateCmds:
                    inputSnippets.clear()
                    getDate()
        for timeCmds in TIME_CMDS:
            for snippets in inputSnippets:
                if snippets in timeCmds:
                    inputSnippets.clear()
                    getTime()
        for greetCmds in GREET_CMDS:
            if inputSnippets[0] in greetCmds:
                inputSnippets.clear()
                greetings()
        for lookupCmds in LOOKUP_CMDS:
            for snippets in inputSnippets:
                if snippets[0] in lookupCmds:
                    inputSnippets.clear()
                    search = Search(self.userInput)
                    searchFiltered = search.searchFilter()
                    wiki = SearchWiki(searchFiltered)
                    wiki.searchWiki()

        return True
