import unittest

from dealer import Dealer
from deck import Card


class TestBlackJack(unittest.TestCase):

    def test_int_hand(self):
        hand = [Card(3, 'hearts'), Card(5, 'spades')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 8)

    def test_solo_ace_hand(self):
        hand = [Card('ace', 'hearts')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 11)

    def test_faces_hand(self):
        hand = [Card('jack', 'hearts'), Card('king', 'spades'), Card('queen', 'spades')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 30)

    def test_aces_hand(self):
        hand = [Card('ace', 'hearts'), Card('ace', 'spades'), Card('ace', 'spades')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 13)

    def test_aceblackjack_hand(self):
        hand = [Card('ace', 'hearts'), Card('king', 'diamonds')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 21)

    def test_acecombi_hand(self):
        hand = [Card('ace', 'hearts'), Card('king', 'diamonds'), Card('ace', 'clubs')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 12)

    def test_acecombi2_hand(self):
        hand = [Card('ace', 'hearts'), Card('king', 'diamonds'), Card(6, 'clubs')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 17)

if __name__ == '__main__':
    unittest.main()


