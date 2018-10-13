import random

class Card:
    def __init__(self, suit, value, face, ace):
        self.suit = suit
        self.value = value
        self.face = face
        self.ace = ace

deck = [] # create an empty list

# Initialize List With Placeholder Value "False"
# We will replace these placeholder values with
# instances of the class "Card"
for x in range(52):
    deck.append(False)

# Fill List With Instances of the Class "Card"
deck[0] = Card("spades", 2, False, False)
deck[1] = Card("spades", 3, False, False)
deck[2] = Card("spades", 4, False, False)
deck[3] = Card("spades", 5, False, False)
deck[4] = Card("spades", 6, False, False)
deck[5] = Card("spades", 7, False, False)
deck[6] = Card("spades", 8, False, False)
deck[7] = Card("spades", 9, False, False)
deck[8] = Card("spades", 10, False, False)

deck[9] = Card("hearts", 2, False, False)
deck[10] = Card("hearts", 3, False, False)
deck[11] = Card("hearts", 4, False, False)
deck[12] = Card("hearts", 5, False, False)
deck[13] = Card("hearts", 6, False, False)
deck[14] = Card("hearts", 7, False, False)
deck[15] = Card("hearts", 8, False, False)
deck[16] = Card("hearts", 9, False, False)
deck[17] = Card("hearts", 10, False, False)

deck[18] = Card("clubs", 2, False, False)
deck[19] = Card("clubs", 3, False, False)
deck[20] = Card("clubs", 4, False, False)
deck[21] = Card("clubs", 5, False, False)
deck[22] = Card("clubs", 6, False, False)
deck[23] = Card("clubs", 7, False, False)
deck[24] = Card("clubs", 8, False, False)
deck[25] = Card("clubs", 9, False, False)
deck[26] = Card("clubs", 10, False, False)

deck[27] = Card("diamonds", 2, False, False)
deck[28] = Card("diamonds", 3, False, False)
deck[29] = Card("diamonds", 4, False, False)
deck[30] = Card("diamonds", 5, False, False)
deck[31] = Card("diamonds", 6, False, False)
deck[32] = Card("diamonds", 7, False, False)
deck[33] = Card("diamonds", 8, False, False)
deck[34] = Card("diamonds", 9, False, False)
deck[35] = Card("diamonds", 10, False, False)

deck[36] = Card("spades", 10, "King", False)
deck[37] = Card("spades", 10, "Queen", False)
deck[38] = Card("spades", 10, "Jack", False)
deck[39] = Card("spades", 11, False, True)

deck[40] = Card("hearts", 10, "King", False)
deck[41] = Card("hearts", 10, "Queen", False)
deck[42] = Card("hearts", 10, "Jack", False)
deck[43] = Card("hearts", 11, False, True)

deck[44] = Card("clubs", 10, "King", False)
deck[45] = Card("clubs", 10, "Queen", False)
deck[46] = Card("clubs", 10, "Jack", False)
deck[47] = Card("clubs", 11, False, True)

deck[48] = Card("diamonds", 10, "King", False)
deck[49] = Card("diamonds", 10, "Queen", False)
deck[50] = Card("diamonds", 10, "Jack", False)
deck[51] = Card("diamonds", 11, False, True)

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

if shuffledDeck[0].face == False:
    print("Your cards are the " + str(shuffledDeck[0].value) + " of " + shuffledDeck[0].suit)
else:
    print("Your cards are the " + str(shuffledDeck[0].face) + " of " + shuffledDeck[0].suit)
if shuffledDeck[1].face == False:
    print("and the " + str(shuffledDeck[1].value) + " of " + shuffledDeck[1].suit)
else:
    print("and the " + str(shuffledDeck[1].face) + " of " + shuffledDeck[1].suit)
