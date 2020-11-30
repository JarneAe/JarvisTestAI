from PIL import Image
import random
import os


def goat():

    # Predefine a list called goats
    goats = []

    # Get the amount of files in the goats directory
    files = os.listdir("GOAT_IMGS/")

    # Loop through the goats folder to get all files.
    for index in range(1, len(files) + 1):
        goats.append("GOAT_IMGS/goat_" + str(index) + ".jpg")
    im = Image.open(random.choice(goats))
    im.show()

    return True
