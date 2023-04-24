"""
* Assignment 6
* Xueyao Wang
* Create a model of a deck of cards.
* Sample output:
    6 of dinosaurs
    spades
    Q
    [2 of hearts, 3 of hearts, 4 of hearts, 5 of hearts, 6 of hearts, 7 of hearts, 8 of hearts, 9 of hearts, 10 of hearts, 
    J of hearts, Q of hearts, K of hearts, A of hearts, 2 of clubs, 3 of clubs, 4 of clubs, 5 of clubs, 6 of clubs, 7 of clubs, 
    8 of clubs, 9 of clubs, 10 of clubs, J of clubs, Q of clubs, K of clubs, A of clubs, 2 of diamonds, 3 of diamonds, 
    4 of diamonds, 5 of diamonds, 6 of diamonds, 7 of diamonds, 8 of diamonds, 9 of diamonds, 10 of diamonds, J of diamonds, 
    Q of diamonds, K of diamonds, A of diamonds, 2 of spades, 3 of spades, 4 of spades, 5 of spades, 6 of spades, 7 of spades, 
    8 of spades, 9 of spades, 10 of spades, J of spades, Q of spades, K of spades, A of spades]

"""


class Card:
    """create a Card class"""

    def __init__(self, suit, number):
        """create __init__ method
        args:
            suit(str): the desired suit of a deck
            number(str): the desired number of a deck
        """

        self._suit = suit
        self._number = number

    def __repr__(self):
        """Override the default output of the __repr__ method"""

        return self._number + ' of ' + self._suit

    @property
    def suit(self):
        """create a method to return the value of the _suit attribute"""

        return self._suit

    @suit.setter
    def suit(self, suit):
        """make sure the new suit is one of the usual suits available in a deck of cards.    
        arg:
          suit(str): set the desired suit of a deck
        """

        if suit in ['hearts', 'clubs', 'diamonds', 'spades']:
            self._suit = suit.upper()
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """create a method to return the value of the _number attribute"""

        return self._number

    @number.setter
    def number(self, number):
        """make sure the new number is one of the usual numbers available in a deck of cards.
        arg:
            number(str): set the desired number of a deck
        """

        if number in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            self._number
        else:
            print("That's not a number!")

# Create an object
my_card = Card('dinosaurs', '6')
print(my_card)

# Check setter and getter of suit
Card.suit = 'spades'
my_suit = Card.suit
print(my_suit)

# Check setter and getter of number
Card.number = 'Q'
my_number = Card.number
print(my_number)

my_card = Card(my_suit, my_number)


class Deck:
    """create a Deck class"""

    def __init__(self):
        """create __init__ method"""

        self._cards = []
        self.populate()
        print(self._cards)

    def populate(self):
        """generates the deck of cards."""

        suits = ['hearts', 'clubs', 'diamonds', 'spades']
        numbers = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
        self._cards = [Card(s, n) for s in suits for n in numbers]

my_deck = Deck()
