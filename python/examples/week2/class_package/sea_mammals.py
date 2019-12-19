from .mammals import Mammal
import datetime

class Whale(Mammal):

    def __init__(self):
        self.limbs = 2
        self.has_hair = False

    def greet(self):
        print('Echo')

