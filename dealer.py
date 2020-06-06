import random


class Dealer(object):

    def __init__(self, deck):
        self.deck = deck

        # pre-shuffle deck upon instantiation
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()

    @staticmethod
    def evaluate_hand_blackjack(hand):
        hand_value: int = 0
        aces = []
        for card in hand:
            if card[0] == 'ace':
                aces.append(card)
                hand_value += 1
            elif card[0] in ['jack','queen','king']:
                hand_value += 10
            else:
                hand_value += card[0]

        if aces:
            for _ in aces:
                while hand_value < 12:
                    hand_value += 10

        return hand_value
