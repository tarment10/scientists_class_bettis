#!/usr/bin/env python

import random

class CardDeck():
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, color):
        self._color = color
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = f"{rank}-{suit}"
                self._cards.append(card)

    def get_cards(obj):
        return obj._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f"CardDeck({len(self._cards)})"

    def get_color(self):  # getter (AKA accessor)
        return self._color

    def set_color(self, new_color): # setter (AKA mutator)
        # if type(new_color) is str:
        if isinstance(new_color, str):
            self._color = new_color
        else:
            raise TypeError("Color must be a string")

if __name__ == '__main__':
    c1 = CardDeck('red')
    c2 = CardDeck('purple')
    c3 = CardDeck('green')
    print(c1.get_color())
    print(c3.get_color())
    print(CardDeck.get_color(c3))
    c1.set_color('black')
    print(c1.get_color())
    print(c1.get_cards())
    c1.shuffle()
    for i in range(8):
        print(c1.draw())
    print(c1)
    print(len(c1))
    print(type(c1))

s = "foo"
print(s.upper())  # str.upper(s)
