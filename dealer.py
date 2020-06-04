import random


class Dealer(object):

    def __init__(self, deck):
        self.deck = deck

        #pre-shuffle deck upon instantiation
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()
