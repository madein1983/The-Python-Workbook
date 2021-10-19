from math import ceil
def payment(distance):
    BASE_TARIFF = 4
    OVERPAY_TARIFF = 0.25
    DIST_FOR_OVERPAY_TARIFF = 140
    overdistance = distance/DIST_FOR_OVERPAY_TARIFF
    print(overdistance)
    price_total = BASE_TARIFF + overdistance*OVERPAY_TARIFF
    print(price_total)
    return price_total
def main():
    distance = float(input("Enter the length of trip:"))
    price = payment(distance)
    print("The total price is: %0.2f" % price)
if __name__ == "__main__":
    main()