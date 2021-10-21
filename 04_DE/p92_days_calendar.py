def isLeap(yyyy) :
    # year = int(input("Enter year: "))
    if (yyyy % 400) == 0 :
        is_leap = True
    elif (yyyy % 100) == 0 :
        is_leap = False
    elif (yyyy % 4) == 0 :
        is_leap = True
    else :
        is_leap = False
    return is_leap

def ordinalDate(dd,mm,yyyy):
    ODD = 31
    EVEN = 30
    if mm == 1 :
        ord = dd
        return ord
    elif mm == 2 :
        ord = ODD+dd
        return ord
    elif mm == 3 :
        ord = ODD+28+dd
        return ord
    elif mm == 4 :
        ord = 2*ODD+28+dd
        return ord
    elif mm == 5 :
        ord = 3*ODD+28+EVEN+dd
        return ord
    elif mm == 6 :
        ord = 3*ODD+28+2*EVEN+dd
        return ord
# ......
    


def main():
    dd = int(input("Enter day: "))
    mm = int(input("Enter day: "))
    yyyy = int(input("Enter day: "))
    ord = ordinalDate(dd,mm,yyyy)
    if isLeap(yyyy) :
        ord += 1
        print(ord)
    else :
        print(ord)

if __name__ == "__main__":
    main()