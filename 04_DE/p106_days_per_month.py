from p106_imported_58 import is_Leap
mm = int(input("Enter month: "))
year = int(input("Enter year: "))
is_Leap(year)
print(is_Leap(year))

if is_Leap(year) == False and mm == 2 :
    print("28 days")
elif is_Leap(year) == True and mm == 2 :
    print("29 days")

elif mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12 :
    print("31 days")
elif mm == 4 or mm == 6 or mm == 9 or mm == 11 :
    print("30 days")


