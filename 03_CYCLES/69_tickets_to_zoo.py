BABY_PRICE = 0
KID_PRICE = 14
ADULT_PRICE = 23
RETIREE_PRICE = 18
KIDS_AGE = 3
ADULTS_AGE = 12
RETIREE_AGE = 65
total_price = 0
count_visitors = 0

line = input("Enter visitor age: ")
while line != "" :
    count_visitors = count_visitors + 1
    age = int(line)
    if age < KIDS_AGE :
        total_price = total_price + BABY_PRICE
    elif KIDS_AGE <= age  and age < ADULTS_AGE :
       total_price = total_price + KID_PRICE
    elif ADULTS_AGE <= age and age < RETIREE_AGE :
       total_price = total_price + ADULT_PRICE
    elif age >= RETIREE_AGE  :
       total_price = total_price + RETIREE_PRICE
    else : 
       print("O_O")
    line = input("Enter visitor age: ")

print (total_price, count_visitors )
