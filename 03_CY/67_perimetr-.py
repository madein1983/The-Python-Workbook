from math import sqrt
perimetr = 0
first_x = float(input("Enter the x-coordinate: "))
first_y = float(input("Enter the y-coordinate: "))
prev_x = first_x
prev_y = first_y

line = input("Enter the next x-coordinate:(Hit enter to exit): ")
while line != "" :
   x = float(line)
   y = float(input("Enter the y-coordinate: ") )
   dist = sqrt((x - prev_x )**2+(y - prev_y)**2)
   perimetr = perimetr + dist
   line = input("Enter the next x-coordinate:(Hit enter to exit): ")
dist = sqrt((first_x-x)**2 + (first_y - y)**2)
perimetr = perimetr + dist

print("The perimetr of polygon is: ", perimetr)