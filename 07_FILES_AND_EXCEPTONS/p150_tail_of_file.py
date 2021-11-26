from os import close
import sys
if len(sys.argv) != 2 :
    print("count of argv != 2 quit()")
    quit()
file_cont = open(sys.argv[1],"r")
file_in_list = []
print(sys.argv[0])
print(sys.argv[1])
try :
    line_in = file_cont.readline()
    line_in.strip()
    while line_in != "" :
        # print(line_in, end ="")
        line_in = file_cont.readline()
        # line_in = line_in.removesuffix('\n')  3.9
        if line_in.endswith('\n') :
            line_in = line_in[:-2]
        file_in_list.append(line_in)
    for i in range(len(file_in_list)-10,len(file_in_list)):
        print(file_in_list[i])
    # print(file_in_list)
    file_cont.close() 
except IOError:
    print("IOError")
    quit()
