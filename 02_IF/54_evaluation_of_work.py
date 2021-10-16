UNACCEPTABLE = 0
ACCEPTABLE = 0.4
MERITORIUS = 0.6
RAISE_FACTOR = 2400

current_level = float(input("Enter the raiting: "))

if current_level >= UNACCEPTABLE and current_level < ACCEPTABLE :
    level = "low level"
elif current_level >= ACCEPTABLE and current_level < MERITORIUS :
    level = "acceptable"
elif current_level >= MERITORIUS :
    level = "meritorius"
else :
    level =""


if level == "" :
    print("You have entered wrong number")
elif level == "acceptable" or level == "low level" :
    print ("Your rating is %s" % level)
else :
    salary = RAISE_FACTOR*current_level
    print ("Your current level is meritorious and you will have $%.2f" % salary)
