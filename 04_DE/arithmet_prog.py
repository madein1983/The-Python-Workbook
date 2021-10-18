import drawBox 

def sumGeometric(a,r,n) :
    if r == 1 :
        return a * n
    s = a*(1-r**n)/(1-r)
    return s


def main() :   
    drawBox.drawBox1
    init = float(input("Enter the first sequence element \"a\":(0 for exit)"))
    while init != 0 :
        ratio = float(input("Enter sequence denominator r: "))
        num = int(input("Enter quantity of elements n: "))
        total = sumGeometric (init,ratio,num)
        print("The sum of first ", num, "elements equal", total )
        
        init = float(input("Enter a:(0 for exit)"))

if __name__ == "__main__" :
    main()