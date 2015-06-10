from cards import *

class PokerHand (Hand):

    all_labels = ["Pair", "Two pair", "Three of a kind", "Straight", "Flush",
                  "Full house", "Four of a kind", "Straight flush"]

    def suit_hist(self):
        """ builds a histogram of the suits that appear in the hand.
        stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """ builds a histogram of the ranks that appear in the hand.
        stores the result in attribute ranks.
        :return: None
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """
        :return: returns True if the hand has two cards with the same rank,
        False otherwise.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_2pairs(self):
        """
        :return: returns True if the hand has two pairs of cards with the same rank,
        False otherwise.
        """
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count += 1
        if count >= 2:
            return True
        return False

    def has_3(self):
        """
        :return: returns True if the hand has three cards with the same rank,
        False otherwise.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def straight_seq(self):
        """ finds all straight sequences in the hand. Note: aces can be high or low,
        so 'Ace-2-3-4-5' is a straight sequence and so is '10-Jack-Queen-King-Ace', but 'Queen-King-Ace-2-3' is not.
        :return: returns a list of all straight sequences in the hand.
        If the hand has no straight sequences, an empty list is returned.
        """
        l = str_list()
        #print(l)
        seq = []

        self.rank_hist()
        hist_keys = self.ranks.keys()
        hist_keys = sorted(hist_keys)

        if len(hist_keys) < 5:
            return []

        # accounts for high Aces:
        if 1 in hist_keys:
            hist_keys.append(1)

        #print('\nall ranks in order:', hist_keys)

        for i in range(len(hist_keys)-4):
            #print(hist_keys[i:i+5])
            if hist_keys[i:i+5] in l:
                seq.append(hist_keys[i:i+5])

        return seq

    def has_straight(self):
        """
        :return: returns True if the hand has five cards with ranks in sequence
        (aces can be high or low,
        so 'Ace-2-3-4-5' is a straight and so is '10-Jack-Queen-King-Ace', but 'Queen-King-Ace-2-3' is not.),
        False otherwise.
        """
        seq = self.straight_seq()
        #print(seq)
        return seq != []

    def has_flush(self):
        """
        :return: returns True if the hand has a flush (five cards with the same suit),
        False otherwise.
        ! the function works correctly for hands with more than or
        equal to 5 cards.
        """
        self.suit_hist()
        #print('suit_hist:', '\n', self.suits)
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_fullhouse(self):
        """
        :return: returns True if the hand has a full house (three cards with one rank, two cards with another),
        False otherwise.
        """
        self.rank_hist()
        hist = self.ranks
        hist_keys = hist.keys()
        for key in hist_keys:
            if hist[key] >= 3:
                hist[key] = 0
                for key2 in hist_keys:
                    if hist[key2] >= 2:
                        return True

        return False

    def has_4(self):
        """
        :return: returns True if the hand has four cards with the same rank,
        False otherwise.
        """
        self.rank_hist()
        #print('rank_hist:', '\n', self.ranks)
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_straightFlush(self):
        """
        :return: returns True if the hand has five cards with ranks in sequence (as defined above in has_straight())
        and with the same suit,
        False otherwise.
        """
        seq = self.straight_seq()
        if seq == []:
            return False

        for lst in seq:
            suits_list = []

            for index in lst:
                for card in self.cards:
                    if card.rank == index:
                        suits_list.append(card.suit)
            hist = histogram(suits_list)
            #print(hist)
            for val in hist.values():
                if val >= 5:
                    return True
        return False

    def classify(self):
        """ method classifies a hand. All poker labels for the hand are stored in a created attribute 'poker_labels'.

        :return: the highest-value label for a hand.
        For example, if a 7-card contains a flush and a pair, the returned value will be “flush”.

        Creates an attribute:
          'poker_labels'
        """
        self.poker_labels = []

        if self.has_pair():
            self.poker_labels.append("Pair")
        if self.has_2pairs():
            self.poker_labels.append("Two pair")
        if self.has_3():
            self.poker_labels.append("Three of a kind")
        if self.has_straight():
            self.poker_labels.append("Straight")
        if self.has_flush():
            self.poker_labels.append("Flush")
        if self.has_fullhouse():
            self.poker_labels.append("Full house")
        if self.has_4():
            self.poker_labels.append("Four of a kind")
        if self.has_straightFlush():
            self.poker_labels.append("Straight flush")

        if self.poker_labels == []:
            return self.poker_labels
        else:
            return self.poker_labels[len(self.poker_labels)-1]


def str_list():
    """
    creates a list of possible sequences of ranks in a straight.
    :return: a list of sequences.
    """
    s = []
    for i in range(1, 10):
        seq = []
        for j in range(i, i+5):
            seq.append(j)
        s.append(seq)
    s.append([10, 11, 12, 13, 1])
    return s


def histogram(lst):
    """
    :param lst: list of anything
    :return: histogram in the form {value_1: its frequency in the list, ...}.
    """
    d = dict()
    for i in lst:
        d[i] = 1 + d.get(i, 0)
    return d


class PokerDeck(Deck):
    """Represents a deck of cards that can deal poker hands.
    """
    def deal_poker_hands(self, num_hands=10, num_cards=5):
        if num_cards*num_hands > 52:
            return 'Not enough cards'

        list_of_hands = []
        for i in range(1, num_hands+1):
            hand_i = PokerHand('Hand {}'.format(i))
            self.move_cards(hand_i, num_cards)
            hand_i.sort()
            hand_i.classify()
            list_of_hands.append(hand_i)
        return list_of_hands

if __name__ == '__main__':
    # loop n times, dealing 7 hands per iteration, 7 cards each
    count_labels = dict()

    n = 10000
    for i in range(n):
        if i%1000 == 0:
            print(i)
        deck = PokerDeck()
        deck.shuffle()

        hands = deck.deal_poker_hands(7, 7)
        for hand in hands:
            for label in hand.poker_labels:
                count_labels[label] = 1 + count_labels.get(label, 0)

    # print the probabilities of each poker label
    total_cards = n * 7
    print('Total 7-card poker hands dealt: ', total_cards)
    #print(count_labels)

    for label in PokerHand.all_labels:
        if count_labels[label] == 0:
            continue
        prob = total_cards/count_labels[label]
        print('The odds of drawing {0} are {1:.2f}-1'.format(label, prob))





