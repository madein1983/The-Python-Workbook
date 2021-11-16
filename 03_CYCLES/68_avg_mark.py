A_PLUS = 4.0
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

marks_total = 0
count = 0

mark_in = str(input("Enter the 1t mark in forma letter and sign, for example A+: "))
while mark_in != "" :
    mark_in = str(input("Enter the mark in forma letter and sign: "))
    if   mark_in == "A+" or mark_in == "A" :
        mark_out = A_PLUS
    elif mark_in == "A-" :
         mark_out = A_MINUS
    elif mark_in == "B+" :
         mark_out = B_PLUS
    elif mark_in == "B" :
         mark_out = B
    elif mark_in == "B-" :
         mark_out = B_MINUS
    elif mark_in == "C+" :
         mark_out = C_PLUS
    elif mark_in == "C" :
         mark_out = C_MINUS
    elif mark_in == "C-" :
         mark_out = C_MINUS
    elif mark_in == "D+" :
         mark_out = D_PLUS
    elif mark_in == "D" :
         mark_out = D
    elif mark_in == "F" :
         mark_out = F
    else :
         mark_out = 0
    marks_total = marks_total + mark_out
    count = count + 1
    print(mark_out, count)
avr = marks_total/count
print("The average mark of %.0f is: %.2f" % (count,avr))
    