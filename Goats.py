from PIL import Image
import random


def goat():
    goats = []
    for index in range(1, 10):
        goats.append("GOAT_IMGS/goat_" + str(index) + ".jpg")
    im = Image.open(random.choice(goats))
    im.show()
