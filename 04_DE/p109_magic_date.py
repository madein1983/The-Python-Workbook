import p106_imported_58

def is_magic_date(dd,mm,yyyy) :

    las_two_digit = int(yyyy[2:])
    if dd*mm == las_two_digit :
        print("It's a magic date")
def main():
    # dd = int(input("Enter day: "))
    # mm = int(input("Enter month: "))
    # yyyy = str(input("Enter year: "))
    # is_magic_date(dd,mm,yyyy)
    print("All magic dates are: ")
    for i in range(1,99) :
        for j in range(1,12) :
            if j == 2 and p106_imported_58 == True :
                for k in range(1,29) :
                    if k*j  == i  :
                        print ("It's a magic date: ", k,"/",j,"/",i)
            if j == 2 and p106_imported_58 == False :
                for k in range(1,28) :
                    if k*j  == i   :
                        print ("It's a magic date: ", k,"/",j,"/",i)
            if j == 1 or j == 3 or j == 5 or j == 7 or j == 8 or j == 10 or j == 12 :
                for k in range(1,31) :
                    if k*j  == i   :
                        print ("It's a magic date: ", k,"/",j,"/",i)
            if j == 4 or j == 6 or j == 9 or j == 11 :
                for k in range(1,30) :
                    if k*j  == i   :
                        print ("It's a magic date: ", k,"/",j,"/",i)

if __name__ == "__main__" :
    main()
