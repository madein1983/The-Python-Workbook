
def calc(weight):
    TEASPOON = 4.2
    SPOON = 15
    CUP = 200
    full_cups = weight // CUP
    print("full_cups = weight // CUP", full_cups  )
    remainder = weight % CUP
    print("remainder = weight % CUP", remainder)
    full_spoons = remainder // SPOON
    print("full_spoons = remainder // SPOON", full_spoons )
    remainder = full_cups % SPOON
    print("remainder = full_cups % SPOON", remainder)
    full_teaspoons = remainder // TEASPOON
    print("full_teaspoons = remainder // TEASPOON",full_teaspoons)
    remainder = remainder % TEASPOON
    print("remainder = remainder % TEASPOON",remainder)
    return weight,full_cups,full_spoons,full_teaspoons

def main():
    weight = float(input("Enter in teaspoons: "))
    
    print(calc(weight))
    # print("The weight %0.0f is equivalent to: %0.0f cups, %0.0f spoons, %0.0f teaspoons" % (full_cups,))

if __name__ == "__main__":
    main()

