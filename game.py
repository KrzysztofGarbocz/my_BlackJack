"""Game class"""
from deck import Deck
from player import Player, WinException, LostException, BlackJack


class Game:

    def __init__(self, how_many_deck=1, how_many_players=1):
        self.players = [Player('Croupier')]
        self.how_many_deck = how_many_deck
        self.how_many_players = how_many_players
        self.deck = Deck(how_many_deck=self.how_many_deck)
        self.deck.shuffle()
        self.win_player = []
        self.start()
        self.player_game()
        self.who_win_between_players()
        self.player_vs_croupier()

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
        while any([True for player in self.players[1:] if player.wait is False]):
            for player in self.players:
                print('_________________________')
                if player.name != 'Croupier':
                    player.present_me()
                    player.show_cards()
                    try:
                        player.count_card()
                        wait = input('Do you want next card? [y/n]')
                        if wait == 'y' or wait == 'Y':
                            player.get_card(self.deck.take_card())
                        else:
                            player.wait = True
                    except LostException as msg:
                        print(msg)
                    except BlackJack as msg:
                        print(msg)
                    except WinException as msg:
                        print(msg)

    def who_win_between_players(self):
        max_score = max([player.score for player in self.players if player.loose is False])
        self.win_player = [player for player in self.players if player.score == max_score]
        print(f'Winner is {self.win_player[0].name}. The score is: {self.win_player[0].score}')

    def player_vs_croupier(self):
        while self.players[0].score < self.win_player[0].score and self.players[0].loose is False:
            self.players[0].present_me()
            self.players[0].get_card(self.deck.take_card())
            self.players[0].show_cards()
            try:
                self.players[0].count_card()
            except BlackJack as msg:
                print(msg)
                print('Croupier Win')
            except LostException as msg:
                print(msg)
                print(f'Score: {self.players[0].score}')
                print('Croupier Lost')
            if self.players[0].score > self.win_player[0].score and self.players[0].loose is not True:
                print('Croupier WIN')
