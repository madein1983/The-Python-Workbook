day_in = int(input("Enter the day: "))
month_in = int(input("Enter the month: "))
if day_in > 31 or month_in > 12 :
    holyday = ""
    print("There is no such combination of day and month: ", day_in, month_in)

elif day_in == 1 and month_in == 1 or day_in == 1 and month_in == "january" :
    holyday = "New Year"
elif day_in == 1 and month_in == 7 or day_in == 1 and month_in == "july" :
    holyday = "Day of CANADA"
else :
    holyday = "there is no such holyday"
print(holyday)