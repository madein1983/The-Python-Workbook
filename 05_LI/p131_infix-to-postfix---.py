from p96_isNumber_repeat import isInteger
from p129_division_into_tokens import token_division
from p130_unary_and_binary_ops import unary_excretion
from p97_presedense_repeat import precedence
operators = []
postfix =[]
tmp  = []

def main():
    line_in = input("Enter math string: ")
    tmp = unary_excretion(token_division(line_in))
    for i in range(0, len(tmp)) :
        if isInteger(tmp[i]):
           postfix[i] = tmp[i]
        elif  precedence(tmp[i]) != -1 :
           while len() :
               print()

    print(ops)
if __name__ == "__main__" :
    main()
