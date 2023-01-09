"""Deck class"""

from card import Card


class Deck:
    """Deck class"""
    def __init__(self, how_many_deck=1):
        self.deck = []
        for _ in range(0, how_many_deck):
            for color in Card.Possible_color:
                for name in Card.Possible_name:
                    self.deck.append(Card(name=name, color=color))
