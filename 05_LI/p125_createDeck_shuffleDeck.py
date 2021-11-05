from random import shuffle

def createDeck() :
    nominal = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    suit = ["S","H","D","C"]
    deck = list()
    temp_deck = ""
    for i in range(0,4) :
        for j in range(0,13) : 
            temp_deck = temp_deck + suit[i] + nominal[j] + " "
    deck = temp_deck.split()
    print(deck)
    return deck

def shuffle_resident(deck) :
    shuffle(deck)
    print(deck)
    return deck

def shuffle_new(deck) :
    print()
def main() :
    deck = createDeck()
    shuffle_resident(deck)


if __name__ == "__main__" :
    main()
