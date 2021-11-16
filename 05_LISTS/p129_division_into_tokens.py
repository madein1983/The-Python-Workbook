def token_division_hjklgjfkctctc(line_in) :
    token_list = [] 
    for i in range(0,len(line_in)) :
        num_counter = 0
        if line_in[i] == "+" or line_in[i] == "-" or line_in[i] == "*" or line_in[i] == "/" or line_in[i] == "^" \
            or line_in[i] == "(" or line_in[i] ==")" :
            token_list.append(line_in[i])
        elif (48 <= ord(line_in[i]) and ord(line_in[i]) <= 57):
            dig = line_in[i]
            flag = 0
            for k in range(i+1,len(line_in)):
                if (48 <= ord(line_in[k]) and ord(line_in[k]) <= 57) and flag == 0:
                    dig = dig + line_in[k]
                else :
                    flag = 1
            token_list.append((dig))         
def token_division(line_in) :
    token_list = [] 
    i = 0 
    while i < len(line_in) :
        if line_in[i] == "+" or line_in[i] == "-" or line_in[i] == "*" or line_in[i] == "/" or line_in[i] == "^" \
            or line_in[i] == "(" or line_in[i] ==")" :
            token_list.append(line_in[i])
            i +=1
        elif (48 <= ord(line_in[i]) and ord(line_in[i]) <= 57):
            digits = ""
            j = i
            while j < len(line_in) and (48 <= ord(line_in[j]) and ord(line_in[j]) <= 57):
                    digits = digits + line_in[j]
                    j +=1
            token_list.append((digits))         
            i = i + len(digits)
        else : 
            print("Error!")
    print(token_list)
    return token_list
def main() :
    line_in = str(input("Enter math sequence(for example (2+3^2)/3): "))
    token_division(line_in)
if __name__ == "__main__" :
    main()
