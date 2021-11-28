import  sys

alphabet = {}
for i in range(65,91):
    alphabet[chr(i)] = 0
# print(alphabet)
if len(sys.argv) != 2:
    print("argv error")
file_container = open(sys.argv[1],"r")
lines = file_container.readlines()
# print(lines) #add al lines in list
# print(type(lines))
file_container.close()

lines1 = []
for i in lines :
    lines1.append(i[:-2])


for i in lines:
    for j in i:
        if j.upper() in alphabet:
           alphabet[j.upper()] = alphabet[j.upper()] + 1  
# print(alphabet)
for i in alphabet:
    print(i, " : ", alphabet[i])
