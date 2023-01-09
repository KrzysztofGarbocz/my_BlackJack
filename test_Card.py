import pytest

from card import Card, NameException, ColorException


def test_create_card():
    card = Card(name='A', color='Club')
    assert card.name == 'A'
    assert card.color == 'Club'


def test_wrong_color():
    with pytest.raises(ColorException) as msg:
        Card('A', 'wrong')
        assert msg == 'Selected wrong color'


def test_wrong_name():
    with pytest.raises(NameException) as msg:
        Card('Wrong', "Club")
        assert msg == 'Selected wrong name'
