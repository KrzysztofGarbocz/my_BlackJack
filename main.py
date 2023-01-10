"""Main module"""
from game import Game

how_many_player = int(input('How many player: '))
how_many_deck = int(input('How many deck: '))
Game(how_many_deck=how_many_deck, how_many_players=how_many_player)
