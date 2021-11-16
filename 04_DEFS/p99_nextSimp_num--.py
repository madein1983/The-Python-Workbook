def isSimpNum(x) :
    while x!=1 :
        if x % 2 == 0 :
           return False
        else :
           x -=1
           return True
def isSimp(x):
    i = 2
    simple_count = 0
    for i in range(x) :
        if (x % (x-i)) == 0 :
            simple_count +=1
    print(simple_count)

def nextSimple(x):
    is_not_simple_flag = False
    j = 2
    simple_count = 0
    while not is_not_simple_flag :
        
        if (x % (x+j)) == 0 :
            is_not_simple_flag = True
            simple_count +=1
            j += 1
        else:
            return False
    
    

def main():
    x = int(input("Enter number: "))
    if isSimpNum(x):
        print("The number is Simple")
    else:
        print("The number is NOT Simple")
    print(isSimp(x))
    nextSimple(x)
    if not nextSimple :
            print(nextSimple(x), "the num is: ", x)
            

if __name__ == "__main__":
    main()