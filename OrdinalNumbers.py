class OrdinalNumbers:

    # Initialize the number variable.
    def __init__(self, number):
        self.number = number

    # Function to provide ordinal numbers for the getDate() function.
    def ordinalNumbers(self):
        numberInput = int(self.number)
        suffix = ["th", "st", "nd", "rd"][min(numberInput % 10, 4)]
        if 11 <= (numberInput % 100) <= 13:
            suffix = "th"
        return str(numberInput) + suffix
