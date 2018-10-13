import random
import sys

class Card:
    def __init__(self, suit, value, face, ace):
        self.suit = suit
        self.value = value
        self.face = face
        self.ace = ace

    def showCard(self):
        # Cole, add your logic here
        if self.face == False and self.ace == False:
            cardString = str(self.value) + " of " + str(self.suit)
        elif self.face != False:
            cardString = str(self.face) + " of " + str(self.suit)
        if self.face == False and self.ace == True:
            cardString = "Ace of " + str(self.suit)
        return cardString


deck = [] # create an empty list

# Initialize List With Placeholder Value "False"
# We will replace these placeholder values with
# instances of the class "Card"
for x in range(52):
    deck.append(False)

# Fill List With Instances of the Class "Card"
deck[0] = Card("Spades", 2, False, False)
deck[1] = Card("Spades", 3, False, False)
deck[2] = Card("Spades", 4, False, False)
deck[3] = Card("Spades", 5, False, False)
deck[4] = Card("Spades", 6, False, False)
deck[5] = Card("Spades", 7, False, False)
deck[6] = Card("Spades", 8, False, False)
deck[7] = Card("Spades", 9, False, False)
deck[8] = Card("Spades", 10, False, False)

deck[9] = Card("Hearts", 2, False, False)
deck[10] = Card("Hearts", 3, False, False)
deck[11] = Card("Hearts", 4, False, False)
deck[12] = Card("Hearts", 5, False, False)
deck[13] = Card("Hearts", 6, False, False)
deck[14] = Card("Hearts", 7, False, False)
deck[15] = Card("Hearts", 8, False, False)
deck[16] = Card("Hearts", 9, False, False)
deck[17] = Card("Hearts", 10, False, False)

deck[18] = Card("Clubs", 2, False, False)
deck[19] = Card("Clubs", 3, False, False)
deck[20] = Card("Clubs", 4, False, False)
deck[21] = Card("Clubs", 5, False, False)
deck[22] = Card("Clubs", 6, False, False)
deck[23] = Card("Clubs", 7, False, False)
deck[24] = Card("Clubs", 8, False, False)
deck[25] = Card("Clubs", 9, False, False)
deck[26] = Card("Clubs", 10, False, False)

deck[27] = Card("Diamonds", 2, False, False)
deck[28] = Card("Diamonds", 3, False, False)
deck[29] = Card("Diamonds", 4, False, False)
deck[30] = Card("Diamonds", 5, False, False)
deck[31] = Card("Diamonds", 6, False, False)
deck[32] = Card("Diamonds", 7, False, False)
deck[33] = Card("Diamonds", 8, False, False)
deck[34] = Card("Diamonds", 9, False, False)
deck[35] = Card("Diamonds", 10, False, False)

deck[36] = Card("Spades", 10, "King", False)
deck[37] = Card("Spades", 10, "Queen", False)
deck[38] = Card("Spades", 10, "Jack", False)
deck[39] = Card("Spades", 11, False, True)

deck[40] = Card("Hearts", 10, "King", False)
deck[41] = Card("Hearts", 10, "Queen", False)
deck[42] = Card("Hearts", 10, "Jack", False)
deck[43] = Card("Hearts", 11, False, True)

deck[44] = Card("Clubs", 10, "King", False)
deck[45] = Card("Clubs", 10, "Queen", False)
deck[46] = Card("Clubs", 10, "Jack", False)
deck[47] = Card("Clubs", 11, False, True)

deck[48] = Card("Diamonds", 10, "King", False)
deck[49] = Card("Diamonds", 10, "Queen", False)
deck[50] = Card("Diamonds", 10, "Jack", False)
deck[51] = Card("Diamonds", 11, False, True)

print("Hello and welcome to BlackJack (inster crowd cheering)")
print("My my my! What a turnout tonight!")

# ------------------------------------------------------------------------------
# ------------------ Create a New Shuffled Deck of Cards -----------------------
# ------------------------------------------------------------------------------
# Initialize List cardSelected (keeps track which cards have been selected)
cardSelected = []
for x in range(52):
    cardSelected.append(False)

# Create New List of Shuffled Cards (initalize as empty array)
shuffledDeck = []
for x in range(52):
    repeat = True
    while repeat == True:
        randomNumber = random.randint(0, 51)
        if cardSelected[randomNumber] == False:
            repeat = False
            shuffledDeck.append(deck[randomNumber]) # add random card to deck

print("Your cards are the " + shuffledDeck[0].showCard() + " and the " + shuffledDeck[1].showCard())
if shuffledDeck[0].value + shuffledDeck[1].value == 21:
    print("BLACKJACK! You lucky dog, you won.")
else:
    choice = raw_input("Would you like to hit or stand? ")
if choice == "hit":
    print("Your card is the " + shuffledDeck[2].showCard())
    if shuffledDeck[0].value + shuffledDeck[1].value + shuffledDeck[2] == 21:
        print("You win!")
    elif shuffledDeck[0].value + shuffledDeck[1].value + shuffledDeck[2] > 21:
        print("You lose! You went over 21!")
    else:
        choice = raw_input("Would you like to hit or stand? ")
        if choice == "hit":
            print("nothing")
            #
            #finish this you goober
            #
        else:
            print("nothing")
elif choice == "stand":
    print("ok")
else:
    print("I didn't understand that, try again.")
    sys.exit()
