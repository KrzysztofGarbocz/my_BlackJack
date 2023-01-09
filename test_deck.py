"""Testing deck"""

from deck import Deck, Card


def test_how_many_card():
    """Check size of single deck"""
    deck = Deck()
    assert len(deck.deck) == 52


def test_how_many_cards_in_3_deck():
    """Check size deck"""
    deck = Deck(how_many_deck=3)
    assert len(deck.deck) == 52*3


def test_print_deck():
    """Print deck"""
    deck = Deck()
    print(deck.deck)


def test_len_single_color():
    """Test len of single color"""
    assert len(Card.Possible_name) == 13
