"""Test class player"""
import pytest

import player
import deck
from player import WinException, LostException, BlackJack
from card import Card


def test_take_card():
    """Test"""
    decks = deck.Deck()
    player1 = player.Player('Kris')
    player1.get_card(decks.take_card())
    player1.show_cards()
    player1.welcome()
    player1.present_me()


def test_count_as_as():
    with pytest.raises(BlackJack) as msg:
        player1 = player.Player('Kris')
        player1.get_card(Card(name='A', color='Club'))
        player1.get_card(Card(name='A', color='Club'))
        player1.show_cards()
        player1.count_card()
        assert player1.blackjack is True
        assert player1.score == 21
        assert msg == 'You have BlackJack !!!'


def test_count_10_as():
    player1 = player.Player('Kris')
    player1.get_card(Card(name='10', color='Club'))
    player1.get_card(Card(name='A', color='Club'))
    player1.show_cards()
    player1.count_card()
    assert player1.score == 21


def test_count_10_8_as():
    player1 = player.Player('Kris')
    player1.get_card(Card(name='10', color='Club'))
    player1.get_card(Card(name='8', color='Club'))
    player1.get_card(Card(name='A', color='Club'))
    player1.show_cards()
    player1.count_card()
    assert player1.score == 19


def test_count_8_as_8():
    player1 = player.Player('Kris')
    player1.get_card(Card(name='8', color='Club'))
    player1.get_card(Card(name='A', color='Club'))
    player1.get_card(Card(name='8', color='Club'))
    player1.show_cards()
    player1.count_card()
    assert player1.score == 17


def test_count_k_q():
    player1 = player.Player('Kris')
    player1.get_card(Card(name='K', color='Club'))
    player1.get_card(Card(name='Q', color='Club'))
    player1.show_cards()
    player1.count_card()
    assert player1.score == 20
