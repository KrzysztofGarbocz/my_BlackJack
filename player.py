"""Player class"""
from deck import Deck


class WinException(Exception):
    """Win Exception"""


class LostException(Exception):
    """Lost Exception"""


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.score = 0
        self.blackjack = False
        self.wait = False

    deck = Deck()

    def get_card(self, deck):
        self.hand.append(deck.deck)
