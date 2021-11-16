min = 60
hour = 3600
day = 86400
daysIn = int(input("Enter the number of days: "))
hourIn = int(input("Enter the number of hours: "))
minIn = int(input("Enter the number of minutes: "))
secIn = int(input("Enter the number of seconds: "))
daysInsec = daysIn*day
hourInsec = hourIn*hour
minInsec = minIn*min
result = daysInsec+hourInsec+minInsec+secIn
print("The total seconds is: ", result)