class Search:

    def __init__(self, inputUser):
        self.inputUser = inputUser

    def formatInput(self):
        loweredUserInput = self.inputUser.lower()
        splitUserInput = loweredUserInput.split()

        return splitUserInput

    def searchFilter(self):
        POP_LOOKUP_ARGS = ["is", "was", "did", "the", "take", "place", "happen", "invented"]

        formattedInput = self.formatInput()
        removeCmd = formattedInput[1:]
        removeArgs = []
        for index in removeCmd:
            if index in POP_LOOKUP_ARGS:
                continue
            else:
                removeArgs.append(index)
        searchInput = " ".join(removeArgs)

        return searchInput
