from p129_division_into_tokens import token_division
def unary_excretion (l_o_t) : # split_off
    list_out = []
    for i in range(0, len(l_o_t)) :
        if i == 0 and (l_o_t[i] == "+") :
            list_out.append("u+")
        elif i == 0 and (l_o_t[i] == "-") :
            list_out.append("u-")
        elif (l_o_t[i] == "-" ) and (l_o_t[i-1] == "*" or l_o_t[i-1] == "/" or l_o_t[i-1] == "-" or l_o_t[i-1] == "+") :
            list_out.append("u-")
        elif (l_o_t[i] == "+" ) and (l_o_t[i-1] == "*" or l_o_t[i-1] == "/" or l_o_t[i-1] == "-" or l_o_t[i-1] == "+") :
            list_out.append("u+")
        else :
            list_out.append(l_o_t[i])
    print(list_out)
def main() :
    line_in = input("Enter the string: ")
    unary_excretion(token_division(line_in))

if __name__ == "__main__" :
    main()