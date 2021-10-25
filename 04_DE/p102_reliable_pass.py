
def reliable(passw):
    up_case = 0
    low_case = 0
    digit = 0
    for i in range(len(passw)):
        if 65 < ord(passw[i]) and ord(passw[i]) < 90 :
            up_case +=1
        elif 97 < ord(passw[i]) and ord(passw[i]) < 122 :
            low_case +=1
        elif 48 < ord(passw[i]) and ord(passw[i]) < 57 :
            digit +=1
        else :
            pass
    if up_case != 0 and low_case != 0 and digit != 0 and len(passw) >=8 :
        return True
    else : 
        return False


def main():
    passw = str(input("Enter password: "))
    
    if reliable(passw) :
        print("Password is reliable!")
    else :
        print("Password is not reliable!")

if __name__ == "__main__" :
    main()