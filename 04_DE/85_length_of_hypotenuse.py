from math import sqrt

def hypotenuse(a,b):
    c = sqrt(a**2+b**2)
    return c

def main ():
    a = float(input("Enter the a-side: "))
    b = float(input("Enter the a-side: "))
    c = hypotenuse(a,b)
    print("Hypotenuse is: ", c)




if __name__ == "__main__":
     main()
