from math import floor
year = int(input("Enter year: "))

day_of_week = (year + floor((year-1)/4) - floor((year-1)/100)+floor((year - 1)/400)) % 7
if day_of_week == 0 : 
    the_1_jan_is = "Sunday"
elif day_of_week == 1 :
    the_1_jan_is = "Monday"
elif day_of_week == 1 :
    the_1_jan_is = "Thusday"
elif day_of_week == 1 :
    the_1_jan_is = "Wednesday"
elif day_of_week == 4 :
    the_1_jan_is = "Thurthsday"
elif day_of_week == 5 :
    the_1_jan_is = "Friday"
elif day_of_week == 6 :
    the_1_jan_is = "Saturday"
else :
    print("O_O")

print(the_1_jan_is)
