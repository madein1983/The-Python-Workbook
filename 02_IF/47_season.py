month = str(input("Enter the month in string: "))
month = month.lower()
day = int(input("Enterthe day of month:"))
if    month == "january" or month == "february" or (month == "december" and day >= 21) or (month == "march" and day < 20) :
    season = "winter"
elif  month == "april" or month =="may" or (month == "march" and day >= 21) or (month =="june" and day > 21) :
    season = "spring"
elif  month =="july" or month =="august" or (month =="june" and day >= 21) or (month =="september" and day > 22) :
    season = "summer"
elif month == "october" or month =="november" or (month =="september" and day > 22) or (month=="december" and day < 21) :
    season = "autum"
else :
    season = "it's impossible"
print (season)