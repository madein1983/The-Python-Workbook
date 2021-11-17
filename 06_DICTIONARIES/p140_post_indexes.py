def isInteger(x) :
    # x_new = x.strip(" ")
    i = 0 
    digit_count = 0
    oth_symbols_count = 0
    x = x.strip()
    while i <= len(x)-1 :
        if ord("0") <= ord(x[i]) and ord(x[i])<= ord("9") :
            digit_count +=1
        else :
            oth_symbols_count +=1
        i+=1
    # print(digit_count," : ",oth_symbols_count)
    if oth_symbols_count == 0 and digit_count >0 :
        return True
    elif oth_symbols_count > 0 and digit_count == 0 :
        return False
    elif oth_symbols_count >0 and digit_count > 0 :
        return False


def post_index(line_in):
    index = {"Newfoundland and Labrador" : "A", "Nova Scotia": "B", "Prince Edward Island" : "C", "New Brunswick" : "E",  "Quebec" : "G" , \
             "Quebec" : "H", "Quebec" : "J",  "Ontario" : "K",  "Ontario" : "L", "Ontario" : "M", "Ontario" : "N", "Ontario" : "P", \
             "Manitoba" : "R", "Saskatchewan" : "S",  "Alberta" : "T",  "British Columbia" : "V", "Nunavut" : "X", "Northwest Territories": "X", \
             "Y" : "Yukon" }

    result = []
    for j in index :
        if line_in[0] == index.get(j) :
            result.append(j)
    print(result)
    
    if len(result) == 0 or (not isInteger(line_in[1])):
        print("You  made a mistake. repeat")
    
    if int(line_in[1]) == 0 :
        print("Country side ")
    else:
        print("City")    
        

# T2N1N4

def main() :
    line_in = input("Enter POST code: ")
    line_in = line_in.upper()
    post_index(line_in)
    
   

    

if __name__ == "__main__" :
    main()