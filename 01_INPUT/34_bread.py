CONST_PRICE = 3.49
DISCOUNT = 0.6
count = int(input("How many bread did you buy yesterday?: "))
print("The price of bread is      %+5s" % CONST_PRICE)
print("The price with discount is % 2f" % DISCOUNT)
print("The toal count is:         % d" % count)
total_sum = count*CONST_PRICE*0.6
print("The total price is:        % 2f" % total_sum)
