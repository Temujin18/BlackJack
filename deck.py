from itertools import product


class CardDeck(object):

    __suites = ['hearts', 'spades', 'clubs', 'diamonds']

    __faces = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']

    def __init__(self):

        self.__deck = list(product(CardDeck.__faces,CardDeck.__suites))

    def __len__(self):
        return len(self.__deck)

    def __str__(self):
        return str(self.__deck)

    def __getitem__(self, item):
        return self.__deck[item]

    def __setitem__(self, key, value):
        self.__deck[key] = value

    def pop(self):
        return self.__deck.pop()

    def empty(self):
        return len(self.__deck) == 0

