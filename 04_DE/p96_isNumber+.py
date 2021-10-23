
##### Обязательно расширить программу до возможности анализировать текст и выделять оттуда цифры и номера 

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
    print(digit_count," : ",oth_symbols_count)
    if oth_symbols_count == 0 and digit_count >0 :
        return True
    elif oth_symbols_count > 0 and digit_count == 0 :
        return False
    elif oth_symbols_count >0 and digit_count > 0 :
        return False

def main():
    x = input("e: ")
    # isInteger(x)
    if isInteger(x) :
        print("Entered string is number")
    else :
        print("Entered string is NOT number")
if __name__ == "__main__" :
    main()