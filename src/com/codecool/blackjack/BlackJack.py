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

    def lose(self):
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


def hit(deck, playercards):

    playercards.add_card(deck.get_a_card())
    playercards.choose_value_for_ace()


def hit_or_stand(deck, playercards):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, playercards)

        elif x[0].lower() == 's':
            print("Player stands. Dealer's turn.")
            playing = False

        else:
            print("Please try again. Enter 'h' or 's'")
            continue
        break


def show_all_cards(playercards, dealercards):
    print("\nDealer's Hand:", *dealercards.cards_in_hand, sep='\n ')
    print("Dealer's Hand =", dealercards.total_value)
    print("\nPlayer's Hand:", *playercards.cards_in_hand, sep='\n ')
    print("Player's Hand =", playercards.total_value)


# Ending scenarios

def player_lose(player, dealer, chips):
    print("Player lost!")
    chips.lose()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win()


def tie(player, dealer):
    print("It's a tie!")


# The Game


print("Welcome to my little Black Jack game!")

# new deck & shuffle
game_deck = Deck()
game_deck.shuffle()


# Dealer
dealer = PlayerCards()
dealer.add_card(game_deck.get_a_card())
dealer.add_card(game_deck.get_a_card())

# Player
player = PlayerCards()
player.add_card(game_deck.get_a_card())
player.add_card(game_deck.get_a_card())
player_chips = Chips()

show_all_cards(player, dealer)
take_bet(player_chips)

while playing:
    hit_or_stand(game_deck, player)
    show_all_cards(player,dealer)
    if player.total_value > 21:
        player_lose(player, dealer, player_chips)
        break

    # If the total is 17 or more, dealer must stand.
    # If the total is 16 or under, dealer must take a card.

if player.total_value <= 21:
    while dealer.total_value < 17:
        hit(game_deck, dealer)
        print("Dealer hit")
    show_all_cards(player, dealer)

    if dealer.total_value > 21:
        player_wins(player, dealer, player_chips)
    elif dealer.total_value < player.total_value:
        player_wins(player, dealer, player_chips)
    elif dealer.total_value > player.total_value:
        player_lose(player, dealer, player_chips)
    else:
        tie(player, dealer)





