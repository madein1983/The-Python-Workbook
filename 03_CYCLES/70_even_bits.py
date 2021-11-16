line_in = str(input("Enter the 8 bit 0 and 1: "))

while line_in != "" :
    if len(line_in) != 8 or (line_in.count("0") + line_in.count("1")) != 8 :
        print("You made a mistake, retry.")
    else :
        if line_in.count("1") % 2 == 0 :
            parity_bit = 0
            print("The parity bit is: ", parity_bit)
        else :
            parity_bit = 1
            print("The parity bit is: ", parity_bit)
    
    line_in = str(input("Enter the 8 bit 0 and 1: "))


