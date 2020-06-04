import random


class CardDeck(object):

    __suites = ['hearts', 'spades', 'clubs', 'diamonds']

    __faces = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']

    __deck = {}

    __shuffled_keys = []

    def __init__(self):

        for suite in CardDeck.__suites:
            for i, face in enumerate(CardDeck.__faces):
                key = '{} of {}'.format(face, suite)
                self.__deck[key] = i+1 if i+1 < 10 else 10

        # pre-shuffle deck upon instantiation
        self.shuffle_deck()

    def __len__(self):
        return len(self.__deck)

    def __str__(self):
        return str(list(self.__deck.items()))

    def shuffle_deck(self):
        __shuffled_keys = random.shuffle(list(self.__deck.keys()))