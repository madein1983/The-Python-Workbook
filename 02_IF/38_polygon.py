# guess the figure
sides = int(input("Enter the number of sides of polygon: "))
if sides == 0 :
    print("its a point")
elif sides == 1 :
    print("Its a line")
elif sides == 2 :
    print("Its a rays")
elif sides == 3 :
    print("Its a triangle")
elif sides == 4 :
    print("Its  a square")
elif sides == 5 :
    print("its a pentagon")
elif sides == 6 :
    print("Its a hexagon")
else  :
    print("Its a polygon")
