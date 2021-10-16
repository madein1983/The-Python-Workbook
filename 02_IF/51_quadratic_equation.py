#
from math import sqrt
a = float(input("Enter the const a: ")) 
b = float(input("Enter the const b: ")) 
c = float(input("Enter the const c: ")) 

discrim = b**2-4*a*c
if discrim < 0 :
    print("The equation hasn't real result! ")
elif discrim == 0 :
    root = -b/2*a
    print("The ",a,"*x2+",b,"*x+",c," has root",root)
elif discrim > 0 :
    root_1 = (-b+sqrt(discrim))/2*a
    root_2 = (-b-sqrt(discrim))/2*a
    print(root_1)
    print(root_2)
    print("The ",a,"*x2+",b,"*x+",c," has root",root_1,root_2)
else :
    print("its impossible")
