import random

#TODO: Create Cards class as follows:
# 1.- Generates Initial card 
# 2.- Compare card enter by user with initial card (high or low)
# 3.- Return 100 pts or -75 pts

class Cards:
    """ 
        Creates constructor and attributes
    """

    def __init__(self):
        self.card = 0
        self.guess = ""
        self.current = 0
        self.next = 0

    #Generates a random card from 1 to 13
    def draw_card(self):
        return random.randint(1, 13)

    #Calculates points earned or lost according to answer and return them
    def has_points(self, guess, current, next):
        if current > next:
            self.card = "l"
            if self.card == guess:
                return 100
            else:
                return -75
        elif current < next:
            self.card = 'h'
            if self.card == guess:
                return 100
            else:
                return -75
        else: 
            return 0
