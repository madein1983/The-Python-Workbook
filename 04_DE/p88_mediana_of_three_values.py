def mediana(a,b,c):
    if a == b or a == c or b == c :
        print("Mediana is absent.")
        return 0
    else :
        med = (a+b+c)-min(a,b,c)-max(a,b,c)
        return med


def main():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    c = float(input("Enter the third value: "))
    med = mediana(a,b,c)
    print("The mediana is: ", med)

if __name__ == "__main__":
    main()
