A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0
INVALID = -1

mark_in = float(input("Enter the mark in forma letter and sign, for example 4: "))

if mark_in >= A :
    mark_out = "A+"
elif mark_in < A and mark_in >= A_MINUS :
    mark_out = "A-"
elif mark_in < A_MINUS and mark_in >= B_PLUS :
    mark_out = "B+"
elif mark_in < B_PLUS and mark_in >= B :
    mark_out = "B"
elif mark_in < B and mark_in >= B_MINUS :
    mark_out =  "B-"
elif mark_in < B_MINUS and mark_in >= C_PLUS :
    mark_out =  "C+"
elif mark_in < C_PLUS and mark_in >= C :
    mark_out = "C"
elif mark_in < C and mark_in >= C_MINUS :
    mark_out = "C-"
elif mark_in < C_MINUS and mark_in >= D_PLUS :
    mark_out = "D+"
elif mark_in < D_PLUS and mark_in >= D :
    mark_out = "D"
elif mark_in < D and mark_in >= F :
    mark_out ="F"
else :
    print ("You have entered wrong number", mark_in)
print("The mark", mark_in,"is correspondent to" , mark_out)
