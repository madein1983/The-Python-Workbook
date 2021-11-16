cents = int(input("Enter the sum: "))
cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quater = 25
cents_per_dime = 10
cents_per_nickel = 5
print(" ", cents // cents_per_toonie, "двухдолларовых монет")
cents = cents % cents_per_toonie
print("Остаток в центах ", cents)

print(" ", cents // cents_per_loonie, "однодолларовых монет")
cents = cents % cents_per_loonie
print("Остаток в центах ", cents)


print(" ", cents // cents_per_quater, "25-ти центовых монет")
cents = cents % cents_per_quater
print("Остаток в центах ",cents)

print(" ", cents // cents_per_dime, "10-ти центовых монет")
cents = cents % cents_per_dime
print("Остаток в центах ",cents)
 
print(" ", cents // cents_per_nickel, "5-ти центовых монет")
cents = cents % cents_per_nickel
print("Остаток в центах ",cents)

print("Остаток в 1 центовых монетах ",cents)