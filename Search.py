class Search:

    # Initialize the inputUser variable
    def __init__(self, inputUser):
        self.inputUser = inputUser

    # Format the user input
    def formatInput(self):
        loweredUserInput = self.inputUser.lower()
        splitUserInput = loweredUserInput.split()

        return splitUserInput

    # Filter out unnecessary words.
    def searchFilter(self):
        POP_LOOKUP_ARGS = ["is", "was", "did", "the", "take", "place", "happen", "invented", "born"]

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
