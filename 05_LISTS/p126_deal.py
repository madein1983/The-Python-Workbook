from p125_createDeck_shuffleDeck import createDeck,shuffle_new

def deal(NUM_OF_PLAYERS,CARDS_ON_HANDS,shuffled_deck):
    keeper1 = ""
    keeper2 = ""
    keeper3 = ""
    keeper4 = ""
    print(shuffled_deck)
    for i in range(0,19,NUM_OF_PLAYERS) :  # 0,5,
        keeper1 = keeper1 + shuffled_deck[i] + " "
        shuffled_deck.pop(i)
    for i in range(1,21,NUM_OF_PLAYERS) :
        keeper2 = keeper2 + shuffled_deck[i] + " "
        shuffled_deck.pop(i)
    for i in range(2,21,NUM_OF_PLAYERS) :
        keeper3 = keeper3 + shuffled_deck[i] + " "
        shuffled_deck.pop(i)
    for i in range(3,21,NUM_OF_PLAYERS) :
        keeper4 = keeper4 + shuffled_deck[i] + " "
        shuffled_deck.pop(i)
    print(keeper1)
    print(keeper2)
    print(keeper3)
    print(keeper4)
    print(shuffled_deck)    

def main():
    CARDS_ON_HANDS = 5
    NUM_OF_PLAYERS = 4
    shuffled_deck = shuffle_new(createDeck())
    deal(NUM_OF_PLAYERS,CARDS_ON_HANDS,shuffled_deck)

if __name__ == "__main__":
    main()