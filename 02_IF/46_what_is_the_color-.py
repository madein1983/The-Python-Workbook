in_x = str(input("Enter the coordinate of cell: for example f1: "))
if  in_x[0].upper()== "A" : 
    row = 1
elif in_x[0].upper() == "B" :
    row = 2
elif in_x[0].upper() == "C" :
    row = 3 
elif in_x[0].upper() == "D" :
    row = 4 
elif in_x[0].upper() == "E" :
    row = 5 
elif in_x[0].upper() == "F" :
    row = 6 
elif in_x[0].upper() == "G" :
    row = 7 
elif in_x[0].upper() == "H" :
    row = 8
else :
    row = 0
col = int(in_x[1])
if col // 2 and row // 2 :
    print ("The cell is white ")
else :
    print ("The cell is black ")

