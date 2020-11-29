from PIL import Image
import random
from Narrator import Narrator

def goatMe():
    goats = ['Goats/Goat01.jpg','Goats/Goat02.jpg','Goats/Goat03.jpg','Goats/Goat04.jpg','Goats/Goat05.jpg','Goats/Goat06.jpeg','Goats/Goat07.jpg','Goats/Goat08.jpg','Goats/Goat09.jpg','Goats/Goat10.jpeg']
    im = Image.open(random.choice(goats))
    im.show()



