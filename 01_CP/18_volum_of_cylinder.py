from math import pi
# Get a volume of cylinder
diametr = float(input("Enter the diametr of cylinder: "))
length_of_cylinder = float(input("Enter the length of cylinder: "))
volume = (diametr/2)*pi*length_of_cylinder
print ("The volume of cyliner with diametr %.0f diametr and length %.0f length_of_cylinder is: %.0f" % (diametr, length_of_cylinder, volume))