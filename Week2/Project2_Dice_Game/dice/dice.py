from random import randint
from time import sleep
from dice.dice_art import dice_parts as art
import os
os.system("")

class Dice():
    def __init__(self, d1 = 1, d2 = 3):
        self.curr_vals = (d1, d2)
        self.art = art
        
    # Visually mimics dice rolling
    def roll(self):
        for i in range(randint(7,13)):
            self.curr_vals = randint(1,6), randint(1,6)
            self.show()
            sleep((15 + (i)**1.75)/randint(80, 100))
            print("\033[F"*6) # Moves cursor up 6 spaces to overwrite previous dice
        self.show()
        print("")
    def show(self):
        d1, d2 = self.curr_vals
        for col1, col2 in zip(self.art[str(d1)], self.art[str(d2)]):
            print(col1 + col2)
