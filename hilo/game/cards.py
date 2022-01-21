import random

#TODO: Create Cards class as follows:
# 1.- Generates Initial card 
# 2.- Compare card enter by user with initial card (high or low)
# 3.- Return 100 pts or -75 pts

class Cards:
    """ Create attributes and methods for this class"""

    def __init__(self):
        self.card = 0

    def draw_card(self):
        self.card = random.randint(1, 13)

    def has_points(self, guess):
        pass