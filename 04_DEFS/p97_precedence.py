


def precedence(operator):
    if operator == "+" or operator == "-" :
        return 1
    elif operator == "*" or operator == "/" :
        return 2
    elif operator == "^" :
        return 3
    else :
        return -1




def main():
    operator = input("Enter operator: ")
    print(precedence(operator))
 

if __name__ == "__main__" :
    main()