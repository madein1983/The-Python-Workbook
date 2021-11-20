from random import randint

def create_lotto_range() :
    columns = "bingo"
    lotto = {}
    for i in range(0,5) :
        if columns[i] == "b" :
            for j in range(0,16) :
                lotto[j] = "B"
        if columns[i] == "i" :
            for j in range(16,31) :
                lotto[j] = "I"
        if columns[i] == "n" :
            for j in range(31,46) :
                lotto[j] = "N"
        if columns[i] == "g" :
            for j in range(46,61) :
                lotto[j] = "G"
        if columns[i] == "o" :
            for j in range(61,75) :
                lotto[j] = "O"                
    print(lotto)
    return lotto

def create_lotto_card(lotto) :
    lotto_card = {}
    count = 0
    for i in range(0,75) :
        temp = randint(0,74)
        if count < 5 :
            lotto_card[temp] = lotto[temp]
            count += 1
    print(lotto_card)
    return lotto_card

def display_created_card(lotto) :
    for i in lotto :
        print(lotto.get(i),":",i)

def main():
    display_created_card(create_lotto_card(create_lotto_range()))

if __name__ == "__main__" :
    main()