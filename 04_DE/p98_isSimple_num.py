def isSimpNum(x) :
    while x!=1 :
        if x % 2 == 0 :
           return False
              
        else :
           x -=1
           return True
def isSimp(x):
    i = 2
    simple = 0
    for i in range(x) :
        if (x % (x-i)) == 0 :
            simple +=1
    print(simple)
def main():
    x = int(input("Enter number: "))
    if isSimpNum(x):
        print("The number is Simple")
    else:
        print("The number is NOT Simple")
    isSimp(x)


if __name__ == "__main__":
    main()