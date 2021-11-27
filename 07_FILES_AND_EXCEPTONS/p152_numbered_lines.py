import sys

if len(sys.argv) != 3:
    print("argv is not equal two. Enter two argv. File to read and file to write")
    quit()
list1 = []
try :
    file_container = open(sys.argv[1], "r")
    line = file_container.readline()
    while line != "":
        line = line.rstrip()
        list1.append(line)
        print(line)
        line = file_container.readline()
    file_container.close()
    print(list1)
except IOError:
    print("IOError_1!")
    quit()

try :
    list2 = []
    for i in range(1,len(list1)):
        list2.append(str(i) + " : " + list1[i])
    print(list2)
    new_file_container = open(sys.argv[2],"w")
    for i in list2 :
        i = i+"\n"
        new_file_container.write(i)
    new_file_container.close()
except IOError:
    print("IOError_2!")
    quit()