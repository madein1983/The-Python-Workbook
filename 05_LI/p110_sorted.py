arr_in = []
line_in = int(input("Enter element(0 to exit): "))
while line_in != 0 :
    line_in = int(input("Enter element(0 to exit): "))
    arr_in.append(line_in) 
arr_in.sort()
print("Прямой порядок: ")
print(arr_in)
for i in arr_in :
    print(i)
arr_in.reverse()
print("Обратный порядок: ")
print(arr_in)
for i in arr_in :
    print(i)
