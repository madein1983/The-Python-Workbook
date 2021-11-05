from random import shuffle, randint

def createDeck() :
    nominal = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    suit = ["S","H","D","C"]
    deck = list()
    temp_deck = ""
    for i in range(0,4) :
        for j in range(0,13) : 
            temp_deck = temp_deck + suit[i] + nominal[j] + " "
    deck = temp_deck.split()
    print("Initial deck:    ",deck)
    return deck

def shuffle_resident(deck) :
    shuffle(deck)
    print("Standart shuffle:", deck)
    return deck

def shuffle_new(deck) :
    for i in range(0,len(deck)) :
        random_integer = randint(i,len(deck))
        if random_integer + i >= len(deck) :
            random_integer = - random_integer
        temp = deck[i] 
        deck[i] = deck[random_integer] 
        deck[random_integer] = temp
    print("My shuffle      :",deck)
    return deck

def main() :
    deck = createDeck()
    shuffle_resident(deck)
    shuffle_new(deck)


if __name__ == "__main__" :
    main()
