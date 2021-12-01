import sys 
if len(sys.argv) != 2 :
    print("only one file as argument ") 
file_in_lines = []
try:
    file_container = open(sys.argv[1])
    line = file_container.readline()
    file_in_lines.append(line)
    while line != "":
        line = file_container.readline()
        if line != "":
            file_in_lines.append(line)
    file_container.close()
    print(file_in_lines)
# extract hash symbol
    new_file_in_lines = []
    for i in file_in_lines :
            if i[0] != "#" :
               new_file_in_lines.append(i)
    print(new_file_in_lines)
    new_file_container=open(sys.argv[1]+".new","w")
    for i in new_file_in_lines:
        i = i+"\n"
        new_file_container.write(i)
    new_file_container.close()
except IOError:
    print("IOError")
