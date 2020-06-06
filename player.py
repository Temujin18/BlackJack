

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_to_hand(self, *cards):
        for card in cards:
            self.hand.append(card)

    def show_hand(self):
        return self.hand
