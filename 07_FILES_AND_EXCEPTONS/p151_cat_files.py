import sys

if len(sys.argv) < 2 :
    print("Incorrect input")
print("The rersult of concatenation of: ")
# for i in range(1,len(sys.argv)) :
#     print(sys.argv[i])
#### equivalent to:
# for j in sys.argv :
#     print(j)
for i in range(1,len(sys.argv)):
    print("The fiel name is: ",sys.argv[i])
    file_container = open(sys.argv[i])
    line_from_file = file_container.readline()
    while line_from_file != "" :
        print(line_from_file, end='')
        line_from_file = file_container.readline()
    file_container.close()
    
