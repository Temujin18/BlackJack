import unittest

from dealer import Dealer


class TestBlackJack(unittest.TestCase):

    def test_int_hand(self):
        hand = [(3, 'hearts'), (5, 'spades')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 8)

    def test_faces_hand(self):
        hand = [('jack', 'hearts'), ('king', 'spades'), ('queen', 'spades')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 30)

    def test_aces_hand(self):
        hand = [('ace', 'hearts'), ('ace', 'spades'), ('ace', 'spades')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 13)

    def test_aceblackjack_hand(self):
        hand = [('ace', 'hearts'), ('king', 'diamonds')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 21)

    def test_acecombi_hand(self):
        hand = [('ace', 'hearts'), ('king', 'diamonds'), ('ace', 'clubs')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 12)

    def test_acecombi2_hand(self):
        hand = [('ace', 'hearts'), ('king', 'diamonds'), (6, 'clubs')]
        self.assertEqual(Dealer.evaluate_hand_blackjack(hand), 17)

if __name__ == '__main__':
    unittest.main()


