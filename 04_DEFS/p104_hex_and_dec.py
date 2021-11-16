def hex2int(line_in) :
    if str(line_in) == "A" or str(line_in) == "a" :
        return 10
    elif str(line_in) == "B" or str(line_in) == "b" :
        return 11
    elif str(line_in) == "C" or str(line_in) == "c" :
        return 12
    elif str(line_in) == "D" or str(line_in) == "D" :
        return 13
    elif str(line_in) == "E" or str(line_in) == "e" :
        return 14
    elif str(line_in) == "F" or str(line_in) == "f" :
        return 15
    else :
        return line_in
    
def int2hex(line_in) :
    if str(line_in) == "10" :
        return "A"
    elif str(line_in) == "11" :
        return "B"
    elif str(line_in) == "12" :
        return "C"
    elif str(line_in) == "13" :
        return "D"
    elif str(line_in) == "14" :
        return "E"
    elif str(line_in) == "15" :
        return "F"
    else :
        return line_in

def main() :
    line_in = input("Enter the number in DEC or HEX: ")
    if 48 <= ord(line_in) and ord(line_in) <= 57 :
        print(int2hex(line_in))
    elif 65 <= ord(line_in) and ord(line_in) <= 70 or 97 <= ord(line_in) and ord(line_in) <= 102 :
        print(hex2int(line_in))
        
    else :
        print("you made a mistake")

if __name__ == "__main__" :
    main()