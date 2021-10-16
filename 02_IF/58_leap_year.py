year = int(input("Enter year: "))

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
