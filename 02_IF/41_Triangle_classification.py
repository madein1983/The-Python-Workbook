a = float(input("Enter the length of the first side  a = "))
b = float(input("Enter the length of the second side b = "))
c = float(input("Enter the length of the third side  c = "))

if a == b and b == c :
    print("The sides are equil so triangle is equialateral.")
elif  a == b or a == c or b == c :
    print("The triangle is isosceles with sides: a = %0.2f b = %0.2f c = %0.2f" % (a,b,c))
else : 
    print("The triangle is versatile a = %0.2f b = %0.2f c = %0.2f" % (a,b,c))