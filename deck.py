from itertools import product

class Card():

    def __init__(self, face, suit):

        __slots__ = (suit, face)

        self.suit = suit
        self.face = face

    def __str__(self):
        return '{} of {}'.format(self.face, self.suit)

class CardDeck(object):

    __suites = ['hearts', 'spades', 'clubs', 'diamonds']

    __faces = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']

    def __init__(self):

        self.__deck = [Card(suit, face) for face, suit in product(CardDeck.__suites,CardDeck.__faces)]

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

