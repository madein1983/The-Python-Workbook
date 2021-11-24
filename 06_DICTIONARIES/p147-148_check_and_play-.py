##########################################
# please don't judge too strict. Its my first try. Task is not accomplished.
##########################################
from p146_lotto_gentake_card import initial_spread,take_card
from random import randint
from colorama import Fore,Back
def spin_the_drum():
    print()

def replace_by_zero(card,win_nu) :
    checked_card = []
    # UNPACK LIST OF THE LISTS^!!!!! found by myself
    for k in card :
        for l in k :
            if l in win_nu :
                checked_card.append(0)
                # print("The win number in the card: ", l)
            else :
                checked_card.append(l)
    # print(checked_card)
    return(checked_card)

def win_num():
     # define win combination:
    win_numbers =  []
    for i in range(0,15):
        w = randint(1,75)
        if w not in win_numbers :
            win_numbers.append(w)
    # print("All win numbers is: ",win_numbers)
    return win_numbers

def sum_of(zer_card):
     s1 = sum(zer_card[0:5])
    #  print("Sum 1 row",s1)
     s2 = sum(zer_card[5:10])
    #  print("Sum 2 row",s2)
     s3 = sum(zer_card[10:15])
    #  print("Sum 3 row",s3)
     s4 = sum(zer_card[15:20])
    #  print("Sum 4 row",s4)
     s5 = sum(zer_card[20:25])
    #  print("Sum 5 row",s5)
     s11 = zer_card[0] + zer_card[5] + zer_card[10] + zer_card[15] + zer_card[20]
    #  print("Sum 1 col",s11)
     s12 = zer_card[1] + zer_card[6] + zer_card[11] + zer_card[16] + zer_card[21]
    #  print("Sum 1 col",s12)
     s13 = zer_card[2] + zer_card[7] + zer_card[12] + zer_card[17] + zer_card[22]
    #  print("Sum 1 col",s13)
     s14 = zer_card[3] + zer_card[8] + zer_card[13] + zer_card[18] + zer_card[23]
    #  print("Sum 1 col",s14)
     s15 = zer_card[4] + zer_card[9] + zer_card[14] + zer_card[19] + zer_card[24]
    #  print("Sum 1 col",s15) 
     sd1 = zer_card[0] + zer_card[6] + zer_card[12] + zer_card[18] + zer_card[24]
    #  print("Sum 1 dia",sd1)
     sd2 = zer_card[4] + zer_card[8] + zer_card[12] + zer_card[16] + zer_card[20]
    #  print("Sum 2 dia",sd2)
     if s1 == 0 or s2 == 0 or  s3 == 0 or s4 == 0 or s5 == 0 or  s11 == 0 or s12 == 0 or s13 == 0 or s14 == 0 or s15 == 0 or sd1 == 0 or sd2 == 0 :
        flag = True
     else :
        flag = False
     return flag

def main() :
    init_spread = initial_spread()
    win_nu = win_num()
    print("The win numbers is: ", win_nu)
    num_of_flag = 0
    for i in range(0,1000):
        card = take_card(init_spread)
        # print("Taken card: ",card)    
        zer_card = replace_by_zero(card,win_nu)
        if sum_of(zer_card) :
          print("The card: ", card, " is winner")
          num_of_flag += 1
    
    print(num_of_flag)
  
if __name__ == "__main__" :
    main()