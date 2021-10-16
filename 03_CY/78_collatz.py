from math import floor, ceil
last_element = float(input("Enter any positive number: "))


while last_element != 1 :
            print(last_element)
            if last_element % 2 == 0 :
                last_element = floor(last_element/2)
            elif last_element % 2 != 0 :
                last_element = ceil(last_element*3 + 1)
            if last_element == 1 :
                print(last_element)
                last_element = float(input("enter the new number: "))

