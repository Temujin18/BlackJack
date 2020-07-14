import random


class Dealer(object):

    def __init__(self, deck):
        self.deck = deck
        self.hand = []

        # pre-shuffle deck upon instantiation
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()

    def add_to_hand(self, *cards):
        for card in cards:
            self.hand.append(card)

    def show_initial_hand(self):
        return str(self.hand[0])

    def show_hand(self):
        return ', '.join(list(map(str, self.hand)))

    @staticmethod
    def evaluate_hand_blackjack(hand):
        hand_value: int = 0
        aces = []
        for card in hand:
            if card.face == 'ace':
                aces.append(card)
                hand_value += 1  # consider all aces as having a value of 1, initially.
            elif card.face in ['jack', 'queen', 'king']:
                hand_value += 10
            else:
                hand_value += card.face

        # for each ace in hand, add 10 to hand_value while hand_value is less than 12, so as not to go bust/over 21.
        if aces:
            for _ in aces:
                while hand_value < 12:
                    hand_value += 10

        return hand_value
