earthquake = float(input("Enter the magnitude: "))
if earthquake < 2 :
    richter = "Minimal"
elif earthquake >= 2 and earthquake < 3 :
    richter = "Very weak"
elif earthquake >= 3 and earthquake < 4 :
    richter = "Weak"
elif earthquake >= 4 and earthquake < 5 :
    richter = "Intermediate"
elif earthquake >= 5 and earthquake < 6 :
    richter = "Moderate"
elif earthquake >= 6 and earthquake < 7 :
    richter = "Strong"
elif earthquake >= 7 and earthquake < 8 :
    richter = "Very strong"
elif earthquake >= 8 and earthquake < 10 :
    richter = "Huge"
elif earthquake >= 10 :
    richter = "Destructive"
print (richter)