import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        cards_in_deck = ''
        for card in self.deck:
            cards_in_deck += '\n ' + card.__str__()
        return 'The deck has:' + cards_in_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def get_a_card(self):
        single_card = self.deck.pop()
        return single_card


class PlayerCards:
    def __init__(self):
        self.cards_in_hand = []
        self.total_value = 0
        self.value_of_aces = 0

    def add_card(self, card):
        self.cards_in_hand.append(card)
        self.total_value += values[card.rank]

    def choose_value_for_ace(self):
        pass


test_deck = Deck()
test_deck.shuffle()
print(test_deck)

test_player = PlayerCards()
test_player.add_card(test_deck.get_a_card())
test_player.add_card(test_deck.get_a_card())
print(test_player.total_value)


