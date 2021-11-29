
def numeral(n):
    if n == 1 :
            r = "first"
            return r
    elif n == 2:
            r = "second"
            return r
    elif n == 3:
            r = "third"
            return r
    elif n == 4:
            r = "fourth"
            return r
    elif n == 5:
            r = "fifth"
            return r
    elif n == 6:
            r = "sixth"
            return r 
    elif n == 7:
            r = "seventh"
            return r
    elif n == 8:
            r = "eighth"
            return r
    elif n == 9:
            r = "ninth"
            return r
    elif n == 10:
            r = "tenth"
            return r
    elif n == 11:
            r = "eleventh"
            return r
    elif n == 12:
            r = "twelfth"
            return r
    else : 
        return 0
def main():
    n = int(input("Enter the number from 1 to 12: "))
    resu = numeral(n)
    print("The result is: ", resu)
