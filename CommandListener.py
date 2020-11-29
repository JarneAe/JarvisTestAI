from Narrator import Narrator
from GetDate import getDate
from GetTime import getTime
from Greetings import greetings
from Search import Search
from SearchWiki import SearchWiki
from Goats import goat


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
        # Formatted user input, please don't change this one.
        formattedInput = self.formatInput()
        # Copy of the user input variable, can be changed.
        inputSnippets = formattedInput.copy()
        # Check if something already ran
        alreadyRan = []

        TIME_CMDS = ["time"]
        COMMANDS = ["say", "repeat"]
        GOAT_CMDS = ["goat", "goats"]
        DATE_CMDS = ["today", "date", "day"]
        GREET_CMDS = ["hello", "hey", "goodmorning", "jarvis"]
        LOOKUP_CMDS = ["look up", "who", "where", "when", "what"]

        for inputGather in inputSnippets:
            if inputGather in GREET_CMDS:
                if inputSnippets[0] == "repeat":
                    pass
                elif "greetings" in alreadyRan:
                    pass
                else:
                    greetings()
                    alreadyRan.append("greetings")
            elif inputGather in COMMANDS:
                if inputGather == "repeat":
                    if "repeat" in alreadyRan:
                        pass
                    else:
                        slicedList = formattedInput[1:]
                        narrator = Narrator(" ".join(slicedList))
                        narrator.narrator()
                        alreadyRan.append("repeat")
                if inputGather == "exit":
                    if inputGather == "repeat":
                        pass
                    else:
                        exit()
            elif inputGather in DATE_CMDS:
                if inputSnippets[0] == "repeat":
                    pass
                elif "getDate" in alreadyRan:
                    pass
                else:
                    getDate()
                    alreadyRan.append("getDate")
            elif inputGather in TIME_CMDS:
                if inputSnippets[0] == "repeat":
                    pass
                elif "getTime" in alreadyRan:
                    pass
                else:
                    getTime()
                    alreadyRan.append("getTime")
            elif inputGather in GOAT_CMDS:
                if inputSnippets[0] == "repeat":
                    pass
                else:
                    goat()
            elif inputGather in LOOKUP_CMDS:
                if inputSnippets[0] == "repeat":
                    pass
                elif "lookup" in alreadyRan:
                    pass
                else:
                    search = Search(self.userInput)
                    searchFiltered = search.searchFilter()
                    wiki = SearchWiki(searchFiltered)
                    wiki.searchWiki()
                    alreadyRan.append("lookup")

        return True
