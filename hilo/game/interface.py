from game.cards import Cards

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
        self.playing = True
        self.guess = ""
        self.card = 0
        self.next_card = 0
        self.answer = ""

    def display_card(self):
        card_object = Cards()
        return card_object.draw_card()

    def start_game(self):
        while self.playing:
            self.card = self.display_card()
            print(f'The card is: {self.card}')
            self.guess = input("Higher or Lower (h/l): ")
            self.next_card = self.display_card()
            print(f"Next Card : {self.next_card}")
            card_object = Cards()
            self.score += card_object.has_points(self.guess, self.card, self.next_card)
            print(f"Your new score is: {self.score}")
            self.play_again()
            print()

    def play_again(self):
        if self.score > 0:
            self.answer = input('Play again? y/n: ')
        if self.answer == "n" or self.score <= 0:
            self.playing = False
            print('Game Over!')
