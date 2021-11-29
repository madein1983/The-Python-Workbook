def letter_to_number(mark_in):
    A_PLUS = 4.0
    A = 4.0
    A_MINUS = 3.7
    B_PLUS = 3.3
    B = 3.0
    B_MINUS = 2.7
    C_PLUS = 2.3
    C = 2.0
    C_MINUS = 1.7
    D_PLUS = 1.3
    D = 1.0
    F = 0
    INVALID = -1
    if   mark_in == "A+" or mark_in == "A" :
        mark_out = A_PLUS
    elif mark_in == "A-" :
        mark_out = A_MINUS
    elif mark_in == "B+" :
        mark_out = B_PLUS
    elif mark_in == "B" :
        mark_out = B
    elif mark_in == "B-" :
        mark_out = B_MINUS
    elif mark_in == "C+" :
        mark_out = C_PLUS
    elif mark_in == "C" :
        mark_out = C_MINUS
    elif mark_in == "C-" :
        mark_out = C_MINUS
    elif mark_in == "D+" :
        mark_out = D_PLUS
    elif mark_in == "D" :
        mark_out = D
    elif mark_in == "F" :
        mark_out = F
    else :
        mark_out = INVALID
    if mark_out == INVALID :
       print("You have entereda wrong mark", mark_in)
    print("Letter mark ", mark_in, "equivalent ", mark_out, " points")
    return mark_out

def number_to_letter(mark_in):
    mark_in = float(mark_in)
    A = 4.0
    A_MINUS = 3.7
    B_PLUS = 3.3
    B = 3.0
    B_MINUS = 2.7
    C_PLUS = 2.3
    C = 2.0
    C_MINUS = 1.7
    D_PLUS = 1.3
    D = 1.0
    F = 0
    INVALID = -1
    if mark_in >= A :
        mark_out = "A+"
    elif mark_in < A and mark_in >= A_MINUS :
        mark_out = "A-"
    elif mark_in < A_MINUS and mark_in >= B_PLUS :
        mark_out = "B+"
    elif mark_in < B_PLUS and mark_in >= B :
        mark_out = "B"
    elif mark_in < B and mark_in >= B_MINUS :
        mark_out =  "B-"
    elif mark_in < B_MINUS and mark_in >= C_PLUS :
        mark_out =  "C+"
    elif mark_in < C_PLUS and mark_in >= C :
        mark_out = "C"
    elif mark_in < C and mark_in >= C_MINUS :
        mark_out = "C-"
    elif mark_in < C_MINUS and mark_in >= D_PLUS :
        mark_out = "D+"
    elif mark_in < D_PLUS and mark_in >= D :
        mark_out = "D"
    elif mark_in < D and mark_in >= F :
        mark_out ="F"
    else :
        print ("You have entered wrong number", mark_in)
    return mark_out
        
def main():
    mark_in = input("Enter the mark in format letter and sign or number in format 0,1,2,3,4( or 1.2 only decimal) for example 5 or A+( Enter to exit.): ")
    while mark_in != "":
        try:
            if len(mark_in) > 3 :
                print("Incorrect input: try again.")
            elif len(mark_in) == 3 and (ord("0") <= ord(mark_in[0]) and ord(mark_in[0]) <= ord("4") )  and (mark_in[1] == "." or mark_in[1] == ","):
                print(number_to_letter(mark_in))
            elif len(mark_in) == 2 and (ord("A") <= ord(mark_in[0]) and ord(mark_in[0]) <= ord("F") )  and (mark_in[1] == "+" or mark_in[1] == "-"):
                print(letter_to_number(mark_in))
            elif len(mark_in) == 1 and (ord("A") <= ord(mark_in[0]) and ord(mark_in[0]) <= ord("F") ) :
                print(letter_to_number(mark_in))
            elif len(mark_in) == 1 and (ord("0") <= ord(mark_in) and ord(mark_in) <= ord("4")):
                print(number_to_letter(mark_in))
            
            mark_in = input("Enter the mark in format letter and sign or number in format 0,1,2,3,4( or 1.2 only decimal) for example 5 or A+( Enter to exit.):")
        except ValueError :
            print ("You made a mistake ValueError try again!  Enter to exit.")
        except TypeError :
            print ("You made a mistake TypeError try again!  Enter to exit.")    


if __name__ == "__main__" :
    main()