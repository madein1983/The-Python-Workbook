import sys

if len(sys.argv) != 2 :
    print("Ups! ")

try:
    temp_list = []    
    file_container = open(sys.argv[1],"r")
    line = file_container.readline()
    temp_list.append(line)
    # print(line)
    while line != "":
        line = file_container.readline()
        temp_list.append(line)
    # print(temp_list)
    file_container.close()
    
    
    max_length = ""
    for i in temp_list:
        if len(i)>len(max_length):
            max_length = i
    print(max_length)
    longest_words = []
    longest_words.append(max_length)
    for i in temp_list:
        if len(max_length)-4 == len(i):
            longest_words.append(i) 
    print(longest_words)
except IOError:
    print("IOError")