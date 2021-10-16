the_number = int(input("Enter the first number: "))
if the_number == 0 :
    print("You made a mistake, program will be closed.")
i = 0
sum = 0 
while the_number != 0 :
    i += 1
    sum += the_number
    the_number = int(input("Enter next number: "))

if i != 0 :
    print(sum)
    print (i)
    print(sum/i)
else :
    print("Program closed.")
