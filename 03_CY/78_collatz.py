from math import floor, ceil
last_element = input("Enter any positive number: ")
if last_element == "" :
    quit()
last_element = float(last_element)


while last_element != 1 :
            print(last_element)
            last_element = float(last_element)
            if last_element % 2 == 0 :
                last_element = floor(last_element/2)
            elif last_element % 2 != 0 :
                last_element = ceil(last_element*3 + 1)
            if last_element == 1 :
                print(last_element)
                last_element = input("enter the new number: ")
            if last_element == 0 or last_element == "":
                quit()

