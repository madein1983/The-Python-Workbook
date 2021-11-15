
def precedence(operator):
    if operator == "+" or operator == "-" :
        return 1
    elif operator == "*" or operator == "/" :
        return 2
    elif operator == "^" :
        return 3
    else :
        return -1