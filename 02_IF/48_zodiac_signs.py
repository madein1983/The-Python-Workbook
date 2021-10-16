month = str(input("Enter the month: "))
day = int(input("Enter the day:"))
month = month.lower()
if (month == "december" and day >= 22) or (month == "january" and day <= 19) :
    print("Capricorn")
elif (month == "january" and day >= 20) or (month == "february" and day <= 18) :
    print("Aquarius")
elif (month == "february" and day >= 19) or (month =="march" and day <= 20) :
    print("Fishes")
elif (month == "march" and day >= 21) or (month == "april" and day <= 19) :
    print("ibex")
elif (month == "april" and day >= 21) or (month == "may" and day <= 20) :    
    print("Taurus")
elif (month == "may" and day >= 21) or (month == "june" and day <= 20) :
    print ("twins")
elif (month == "june" and day >= 21) or (month == "july" and day <= 22) :
    print("cancer")
elif (month == "july" and day >= 23) or (month == "august" and day <= 22) :
    print("lion")
elif (month == "august" and day >=23) or (month == "september" and day <= 22) :
    print ("virgin")
elif (month == "september" and day >= 23) or (month == "october" and day <= 22) :
    print("scales")
elif (month == "october" and day >= 23) or (month == "november" and day <= 21) :
    print("scorpio")
elif (month == "november" and day >= 22) or (month == "december" and day <=21) :
    print("saggitarius")
else :
    print("It's impossible")