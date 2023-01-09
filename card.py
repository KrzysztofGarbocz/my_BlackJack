"""Class card"""


class ColorException(Exception):
    """My color exception class"""


class NameException(Exception):
    """My name exception class"""


class Card:
    """Class card
    in name: str: from possible name list
    in color : str: from possible color list
    """
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

    def __repr__(self):
        return f'{self.color}-{self.name}'
