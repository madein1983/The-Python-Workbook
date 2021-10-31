zero_arr = []
posi_arr = []
nega_arr = []
line_in = input("Enter integer numbers( empty string to exit): ")
while line_in != "" :
    line_in = int(line_in)
    if  line_in < 0 :
        nega_arr.append(line_in)
    elif line_in == 0 :
        zero_arr.append(line_in)
    elif line_in > 0 :
        posi_arr.append(line_in)
    else :
        print("It's impossible!")
        print("Error! Rerpeat input! ")
    line_in = input("Enter integer numbers( empty string to exit): ")

for i in nega_arr :
    print(i)
for i in zero_arr :
    print(i)
for i in posi_arr :
    print(i)

zero_arr.append(posi_arr)
nega_arr.append(zero_arr)
print(nega_arr)
