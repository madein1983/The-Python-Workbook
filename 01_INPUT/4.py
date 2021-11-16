## 8/13/2021 9:00 pm
print("Enter the side a in foot")
side_a = float(input())
print("Enter the side b in foot")
side_b = float(input())
S_foot = side_a * side_b
S_akre = S_foot/43560
print("%.2f" %S_akre)

#######################################FROM BOOK###################################################
SQRFT_PER_ACRE = 43560
length = float(input("Введиет ширину участка в футах: "))
width  = float(input("Введиет ширину участка в футах: "))
acres = length * width /SQRFT_PER_ACRE
print ("Площадь садового участка равна", acres, "акров")