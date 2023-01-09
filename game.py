"""Game class"""
import pytest
from deck import Deck
from player import Player, WinException, LostException, BlackJack


class Game:

    def __init__(self, how_many_deck=1, how_many_players=1):
        self.players = [Player('Croupier')]
        self.how_many_deck = how_many_deck
        self.how_many_players = how_many_players
        self.deck = Deck(how_many_deck=self.how_many_deck).shuffle()
        self.start()
        self.player_game()


    def start(self):
        for _ in range(0, self.how_many_players):
            name = input('Write yours nik: ')
            while any([True for x in self.players if x.name == name]):
                print('This nick is not available.')
                name = input('Write another nik: ')
            if all([True for x in self.players if x.name != name]):
                self.players.append(Player(name))
        for player in self.players:
            if player.name != 'Croupier':
                player.welcome()
            player.get_card(self.deck.take_card())
            player.get_card(self.deck.take_card())
        self.players[0].present_me()
        print(self.players[0].hand[0])

    def player_game(self):
        while any([True for player in self.players if player.wait is False]):
            for player in self.players:
                print('_________________________')
                player.present_me()
                player.show_cards()
                with pytest.raises(LostException) or pytest.raises(WinException) or pytest.raises(BlackJack):
                    player.count_card()
                    wait = input('Do you want next card? [y/n]')
                    if wait == 'y' or wait == 'Y':
                        player.get_card(self.deck.take_card())
                    else:
                        player.wait = True
