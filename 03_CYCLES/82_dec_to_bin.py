result = ""
q = int(input("Enter the DEC number: "))
while q != 0 :
    r = q % 2
    result = result + str(r)
    q = q // 2
print(result)