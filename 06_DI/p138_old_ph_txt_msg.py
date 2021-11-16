

def main() :
    symb = {".": 1, ",":11, "?":111, "!":1111, ":": 11111, "A": 2,"B": 22,"C": 222,"D": 3,"E": 33,"F": 333, "G": 4,"H": 44, "I": 444, \
         "J": 5, "K": 55, "L": 555, "M": 6, "N": 66, "O": 666, "P": 7, "Q": 77, "R": 777, "S": 7777, "T": 8, "U": 88, "V": 888, "W": 9, \
         "X": 99, "Y": 999, "Z": 9999, " " : 0}

    # access to value
    # for j in symb :
    #     print(symb.get(j))

    line_in = input("Enter text: ")
    line_in = line_in.upper()
    line_out = ""

    for i in range(0,len(line_in)) :
        for j in symb :
            if line_in[i] == j :
               line_out = line_out + " " + str(symb.get(j))
    # print(line_in[i])
    # for j in symb :
    #      print(j)
    print(line_out)


if __name__ == "__main__" :
    main()