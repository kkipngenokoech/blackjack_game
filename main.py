from IPython.display import clear_output
from random import randint


class black_jack():
    def __init__(self):
        self.deck = []
        self.suits = ("spades", "hearts", "clubs", "diamonds")
        self.values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")

    def make_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))  # first round spades are alloctaed to all the values
                # second round hearts is allocted all the values

    def pull_card(self):
        return self.deck.pop(randint(0, len(self.deck) - 1))


game = black_jack()
game.make_deck()


# print(game.deck)-used to thest if the loop and class is working probalby
# print(game.pull_card(),len(game.deck))-checks wether the pull methods work properly
class blackjack_player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self, dealer_start=True):
        print("\n{}".format(self.name))
        print("=" * 7)
        for index in range(len(self.hand)):
            if self.name == "dealer" and index == 0 and dealer_start:
                print("-of-")  # hides the first card
            else:
                card = self.hand[index]
                print("{} of {}".format(card[0], card[1]))
                print("TOTAL:{}".format(self.calculate_hand(dealer_start)))
    def calculate_hand(self,dealer_start=True):
        total=0
        ace=0#aces can worth 11 or 1 point
        card_value={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9 10:10,"J":10,"Q":10,"K":10,"A":11}
        if self.name=="dealer" and dealer_start:
            card=self.hand[1]
            return card_value[card[0]]
        for card in self.hand:
            if card[0]=="A":
                ace+=1
            else:
                total+=[card_value[0]]
        for index in range(ace):
            if total+11>21:
                total+=1
            else:
                total+=11


player_name = input("enter your name:")
clear_output()
player = blackjack_player(player_name)
dealer = blackjack_player("dealer")
# print(player.name,dealer.name)-test
"""
add two cards to both players and dealers hands
"""
for index in range(2):
    player.add_card(game.pull_card())
    dealer.add_card(game.pull_card())
# print("PLAYER'S HAND:{}\nDEALER'S HAND:{}".format(player.hand,dealer.hand))
player.show_hand()
dealer.show_hand()
