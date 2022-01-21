from game.cards.py import Cards

class Interface:
    """ Class to show on display the different options
        1.- Initial Card
        2.- Higher or Lower (h/l):
        3.- Next Card
        4.- New Score
        5.- Play again? 

        Create all attributes and methods needed for this class
    """
    def __init__(self):
        self.score = 300

    def start_game(self):
        pass