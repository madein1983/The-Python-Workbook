## Arifmetica
#
from math import log10

a = float(input("Введите число а: ")) 
b = float(input("Введите число b: ")) 
s = a + b
print(s)
diff = a - b
print (diff)
mult = a * b
print (mult)
div = a // b
print(div)
ost = a % b
print(ost)
log = log10(a)
print(log)
pow = a ** b
print(pow)


print (a, "+", b, " = ", a + b )
print (a, "-", b, " = ", a - b )
print (a, "x", b, " = ", a * b )
print (a, "//", b," = ", a // b )
print (a, " % ", b, " = ", a % b )
print (a, "log10(a)", " = ", log10(a))
print (a, "**", b, " = ", a ** b )