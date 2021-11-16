from random import randint
from math import floor

def ran_num_lottery(start) :
    win_num = []
    i = 0
    while len(win_num) != 6 :
            r = randint(1,49)
            if r not in win_num :
                win_num.append(r)
            i += 1
    win_num.sort()
    print(win_num)

def main() :
    
    ran_num_lottery(True)
    


if __name__ == "__main__" :
    main()