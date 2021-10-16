##Расстояние между точками на земле
#
from math import radians, sin,cos,acos
t1 = radians(float(input("Enter in degree N1 ")))
g1 = radians(float(input("Enter in degree E1 ")))
t2 = radians(float(input("Enter in degree N2 ")))
g2 = radians(float(input("Enter in degree E2 ")))
print(t1,g1,t2,g2)
distance = 6371.01 * acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
print("%.4f" % distance, "km")