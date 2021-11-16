def is_triangle(a,b,c):
    if a <= 0 or b <= 0 or c <= 0 :
       return False
    elif (a+b)<=c or (b+c)<=a or (c+a)<=b:
       return False
    else :
       return True
def main():
    a = float(input("Enter a - side: "))
    b = float(input("Enter b - side: "))
    c = float(input("Enter c - side: "))
    result = is_triangle(a,b,c)
    print(result)
if __name__ == "__main__" :
    main()