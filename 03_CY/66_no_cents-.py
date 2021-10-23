# CONCAT THE ALL ENTERED SYMBOULS
# price = input("Enter the first price: ")
# i = 0
# while i != "" :
#       i = input("Enter price: ")
#       price = price + i
#       print(price)
import math
PENNI_PER_NICKEL = 5
    
current_price = float(input("Enter the first price: "))
total = 0.00

while current_price != "" :
      total = total + float(current_price)
      current_price = input("Enter the price: " )
print("The total sum for payment is: %0.2f " % total)

flag = (total*100)%PENNI_PER_NICKEL
print(flag)


