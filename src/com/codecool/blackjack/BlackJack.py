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
        self.aces_track = 0

    def add_card(self, card):
        self.cards_in_hand.append(card)
        self.total_value += values[card.rank]

        if card.rank == "Ace":
            self.aces_track += 1

    def choose_value_for_ace(self):
        while self.total_value > 21 and self.aces_track > 0:
            self.total_value -= 10
            self.aces_track -= 1


class Chips(object):

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win(self):
        self.total += self.bet

    def lost(self):
        self.total -= self.bet


# Function definitions to play the game

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Enter your bet: '))
        except ValueError:
            print("Please give your bet with numbers")
        else:
            if chips.bet > chips.total:
                print('You do not have enough chips')
            else:
                break


def hit(deck,playercards):

    playercards.add_card(deck.get_a_card())
    playercards.choose_value_for_ace()




test_deck = Deck()
test_deck.shuffle()
print(test_deck)

test_player = PlayerCards()
test_player.add_card(test_deck.get_a_card())
test_player.add_card(test_deck.get_a_card())
print(test_player.total_value)
for card in test_player.cards_in_hand:
    print(card)


