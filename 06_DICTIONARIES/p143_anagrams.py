# two dictionaries is equal if they contain same numbers of key and same values for these keys

def count(line_in) :
    dict = {}
    
    for sym in line_in :
        # print("i: ",i)
        if sym in dict :
            dict[sym] = dict[sym] + 1
        else :
            dict[sym] = 1

    print(dict)
    return dict 

def main() :
    line1_in = str(input("Enter 1t line: "))
    line2_in = str(input("Enter 2d line: "))
    c1 = count(line1_in)
    c2 = count(line2_in)
    if c1 == c2 :
        print("Entered lines are anagram")
    else :
        print("Entered lines are NOT anagram")

if __name__ == "__main__" :
    main()