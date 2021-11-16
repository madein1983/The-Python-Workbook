from math import tan,pi
# s -the length of the side, n - number of the sides
s = float(input("Enter the length of the regular side: "))
n = int(input("Enter the number of regular sides: "))
area = (n*(s**2))/4*tan(pi/n)
print ("The area of regular polygon with %.0f sides with length equal %.2f is %.2f" % (n,s,area))
