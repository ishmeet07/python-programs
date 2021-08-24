#this program is made by  ishmeet singh
#this is a deck war game
import random

suits = ['spades', 'club', 'hearts', 'diamond']
ranks = [
    'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'jack', 'queen', 'king', 'ace'
]
dictionary1 ={
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'ten':10,
    'jack':11,
    'queen':12,
    'king':13,
    'ace':14
}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = dictionary1[rank]

    def __str__(self):
        a = self.suit
        b = self.rank
        return b + ' of ' + a


class Deck:
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.allcards)

    def poppin(self):
        return self.allcards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.allcards = []

    def remove(self):
        return self.allcards.pop(0)

    def add(self, newcards):
        if type(newcards) == type([]):
            self.allcards.extend(newcards)
        else:
            self.allcards.append(newcards)

    def __str__(self):
        return f'Player {self.name} has {len(self.allcards)} cards'

n=input("enter name of player1")
m=input("enter name of player2")
player1 = Player(n)
player2 = Player(m)
newdeck = Deck()
newdeck.shuffle()

for x in range(26):
    player1.add(newdeck.poppin())
    player2.add(newdeck.poppin())
round = 0
game = True
while game:
    round += 1
    print(f"round{round}🎃🤩")
    if len(player1.allcards) == 0:
        print( f"{player1.name} of cards")
        game = False
        break
    elif len(player2.allcards) == 0:
        print(f"{player2.name }out of cards")
        game = False
        break
    player1cards = []
    player1cards.append(player1.remove())
    player2cards = []
    player2cards.append(player2.remove())
    war = True
    while war:
        if player1cards[-1].value > player2cards[-1].value:
            player1.add(player1cards)
            player1.add(player2cards)
            war = False
        elif player1cards[-1].value < player2cards[-1].value:
            player2.add(player1cards)
            player2.add(player2cards)
            war = False

        else:
            print("war")
            if len(player1.allcards) < 5:
                print(f"{player1.name} out of cards")
                game = False
                break
            elif len(player2.allcards) < 5:
                print(f"{player1.name} out of cards")
                game = False
                break

            else:
                for n in range(5):
                    player1cards.append(player1.remove())
                    player2cards.append(player2.remove())



