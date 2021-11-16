from random import randint, randrange

def dice() :
    dice1 = []
    dice2 = []
    sum_of_dice1and2 = []
    for i in range(0 ,1000) :
      d1 = randint(1,6)
      dice1.append(d1)
      d2 = randint(1,6)
      dice2.append(d2)
      d3 = d1 + d2
      sum_of_dice1and2.append(d3)
    print(sum_of_dice1and2)
    count_of_2 = sum_of_dice1and2.count(2)
    count_of_3 = sum_of_dice1and2.count(3)
    count_of_4 = sum_of_dice1and2.count(4)
    count_of_5 = sum_of_dice1and2.count(5)
    count_of_6 = sum_of_dice1and2.count(6)
    count_of_7 = sum_of_dice1and2.count(7)
    count_of_8 = sum_of_dice1and2.count(8)
    count_of_9 = sum_of_dice1and2.count(9)
    count_of_10 = sum_of_dice1and2.count(10)
    count_of_11 = sum_of_dice1and2.count(11)
    count_of_12 = sum_of_dice1and2.count(12)

    print("Count of 2: ", count_of_2, "Percentage: ", count_of_2/10)
    print("Count of 3: ", count_of_3, "Percentage: ", count_of_3/10)
    print("Count of 4: ", count_of_4, "Percentage: ", count_of_4/10)
    print("Count of 5: ", count_of_5, "Percentage: ", count_of_5/10)
    print("Count of 6: ", count_of_6, "Percentage: ", count_of_6/10)
    print("Count of 7: ", count_of_7, "Percentage: ", count_of_7/10)
    print("Count of 8 ",  count_of_8, "Percentage: ", count_of_8/10)
    print("Count of 9: ", count_of_9, "Percentage: ", count_of_9/10)
    print("Count of 10: ", count_of_10, "Percentage: ", count_of_10/10)
    print("Count of 11: ", count_of_11, "Percentage: ", count_of_11/10)
    print("Count of 12: ", count_of_12, "Percentage: ", count_of_12/10)

def dice_with_dict() :
    NUMBER_OF_RUNS = 1000
    MAX_NUMBER = 6
    
    # dict of expected:
    expected = {2 : 1/36, 3:2/36, 4:3/36, 5:4/36, 6:5/36, 7:6/36, 8:5/36, 9:4/36, 10:3/36, 11:2/36, 12:1/36}
    counts = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
    for i in range(NUMBER_OF_RUNS) :
        d1 = randrange(1,MAX_NUMBER+1)
        d2 = randrange(1,MAX_NUMBER+1)
        d3 = d1+d2
        counts[d3] = counts[d3] + 1
    print(" all   real    expected")
    print("        %          % ")
    for i in sorted(counts.keys()):
        print("{}       {}    {} ".format(i,counts[i]*100/NUMBER_OF_RUNS,expected[i]*100))

def main () :
    dice()
    dice_with_dict()



if __name__ == "__main__" :
    main()