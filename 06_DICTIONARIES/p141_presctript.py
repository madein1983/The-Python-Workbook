
def prescript(line_in) :
    units = { 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    teens = { 10 :"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",18:"eighteen", 19:"ninteen"}
    dozens = { 2:"tventy", 3:"thirty", 4:"fourty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety" }

    units_str = ""
    dozens_str = ""
    hundreds_str = ""
    
    if len(line_in) == 0 :
       print("mistake")
    
    elif  len(line_in) == 1 and (ord("0") <= ord(line_in[0]) and ord(line_in[0]) <= ord("9")) :
        for j in units :
            if line_in[0] == str(j) : 
               units_str = units.get(j)
    elif len(line_in) == 2 and int(line_in[0]) == 1 :
        for k in teens :
            if line_in == str(k) :
                units_str = teens.get(k)
    elif len(line_in) == 2 :
        for j in units :
            if line_in[len(line_in)-1] == str(j) :
                units_str = units.get(j)
        for k in dozens :
            if line_in[len(line_in)-2] == str(k) :
                dozens_str = dozens.get(k)
    elif len(line_in) == 3 :
        for j in units :
            if line_in[len(line_in)-1] == str(j) :
                units_str = units.get(j)
        for k in dozens :
            if line_in[len(line_in)-2] == str(k) :
                dozens_str = dozens.get(k)
        for l in units :
            if line_in[len(line_in)-3] == str(l) :
                hundreds_str =  units.get(l) + " hundred"
        
    print("It is a bill $ ", hundreds_str, dozens_str,units_str)

def main() :
    line_in = str(input("Enter sum: "))
    prescript(line_in)

if __name__ == "__main__" :
    main()