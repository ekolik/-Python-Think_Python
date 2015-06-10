class Card:

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King']

    def __str__(self):
        return '{} of {}'.format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        # t1 and t2 are tuples
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

import random

class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = [str(card) for card in self.cards]
        return '\n'.join(res)

    def pop_card(self, i=-1):
        return self.cards.pop(i)

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_hands, num_cards):
        if num_cards*num_hands > 52:
            return 'Not enough cards'

        list_of_hands = []
        for i in range(1, num_hands+1):
            hand_i = Hand('Hand {}'.format(i))
            self.move_cards(hand_i, num_cards)
            list_of_hands.append(hand_i)
        return list_of_hands


class Hand(Deck):
    """represents a hand of playing cards"""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    """
    :param obj: any python object
    :param method_name: string method name
    :return: the class object that will provide the definition of method_name
     (as a string) if it is invoked on obj.
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    hands = deck.deal_hands(3, 3)
    for h in hands:
        print(h.label)
        h.sort()
        print(h, '\n')