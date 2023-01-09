"""Class card"""


class ColorException(Exception):
    pass


class NameException(Exception):
    pass


class Card:
    Possible_color = ['Club', 'Diamond', 'Heart', 'Spades']
    Possible_name = ['A', 'Q', 'K', 'J'] + [str(x) for x in range(2, 11)]

    def __init__(self, name, color):
        if name in self.Possible_name:
            self.name = name
        else:
            raise NameException('Selected wrong name')

        if color in self.Possible_color:
            self.color = color
        else:
            raise ColorException('Selected wrong color')
