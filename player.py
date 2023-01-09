"""Player class"""
from deck import Card


class WinException(Exception):
    """Win Exception"""


class LostException(Exception):
    """Lost Exception"""


class BlackJack(Exception):
    """You have BlackJack"""


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.score = 0
        self.blackjack = False
        self.wait = False

    def get_card(self, card: Card):
        """Get card"""
        self.hand.append(card)

    def count_card(self):
        self.score = 0
        how_many_as = 0
        if self.blackjack is False:
            for card in self.hand:

                if card.name not in Card.Possible_name[0:4]:
                    self.score += int(card.name)
                    for _ in range(0, how_many_as):
                        if self.score > 21:
                            self.score -= 10

                if card.name in Card.Possible_name[1:4]:
                    self.score += 10
                    for _ in range(0, how_many_as):
                        if self.score > 21:
                            self.score -= 10

                if card.name == Card.Possible_name[0]:
                    how_many_as = len([card_as for card_as in self.hand if card_as.name == 'A'])
                    if how_many_as == 2 and len(self.hand) == 2:
                        self.score = 21
                        self.blackjack = True
                        self.wait = True
                        raise BlackJack('You have BlackJack !!!')

                    if self.score > 10 and self.blackjack is False:
                        self.score += 1

                    if self.score <= 10 and self.blackjack is False:
                        self.score += 11

                if self.score > 21:
                    raise LostException('You lost. You have more than 21')
                print(f'Score: {self.score}')

    def show_cards(self):
        """Show cards"""
        print(self.hand)

    def present_me(self):
        """Print msg"""
        print(f'Player: {self.name}')

    def welcome(self):
        """Start game print"""
        print(f'Welcome {self.name} in game.')
