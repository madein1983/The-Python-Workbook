day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if 1 > day or day > 31 or 1 > month or month > 12 or year < 1 :
    print (" fufu")
    pass

if (year % 400) == 0 :
    is_leap = True
elif (year % 100) == 0 :
    is_leap = False
elif (year % 4) == 0 :
    is_leap = True
else :
    is_leap = False

if is_leap :
    print("The year %s is leap" % year )
else :
    print("The year %s is not leap" % year)

if 1 < day and day < 27 and month == 2  :
    current_day = day + 1
    current_month = month
    current_year = year
elif day == 28 and  is_leap and month == 2:
    current_day = 29
    current_month = month
    current_year = year
elif day == 28 and not is_leap and month == 2 :
    current_day = 1
    current_month = 3
    current_year = year
elif day == 30 and (month == 4 or month == 6 or month == 9 or month == 11) :
    current_day = 1
    current_month = month + 1
elif day == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) :
    current_day = 1
    current_month = month + 1
    current_year =year
elif day == 31 and month == 12 :
    current_day = 1
    current_month = 1
    current_year = year + 1
elif True:
    current_day = day + 1
    current_month = month
    current_year = year
else :
    current_day = 0
    current_month = 0
    current_year = 0
    print("O_O")

print("Next day is: ", current_day," ", current_month," ", current_year)