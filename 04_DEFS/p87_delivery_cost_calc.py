
def sum_calc(count) :
    FIRST_ITEM_EXPRESS_DELIVERY_COST = 10.95
    OVER_FIRST_ITEM_DELIVERY_COST = 2.95
    if count == 1:
        sum = FIRST_ITEM_EXPRESS_DELIVERY_COST
        return sum
    else:
        sum = (count-1)*OVER_FIRST_ITEM_DELIVERY_COST+FIRST_ITEM_EXPRESS_DELIVERY_COST
        return sum

def main():
    count = int(input("Enter the number of  item in basket: "))
    total_delivery_cost = sum_calc(count)
    print("The total delivery cost is: %0.2f" % total_delivery_cost)

if __name__ == "__main__":
    main()