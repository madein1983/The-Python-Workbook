import sys

if len(sys.argv) != 2:
    print("argv is not 2")

try:
    file_container = open(sys.argv[1],"r")
    lines = file_container.readlines()
    print(lines)

    upper_lines = []
    for i in lines:
        upper_lines.append(i.upper())
    print(upper_lines)
    
    new_list = []
    for i in upper_lines:
        temp = ""
        for j in i:
            if ord("A") <= ord(str(j)) and ord(str(j)) <= ord("Z"):
               temp = temp + j
            else:
               temp = temp + " " 
        new_list.append(temp)
    print(new_list)
    print("Length o fneues list is: ",len(new_list))
    
    neues_list = []
    for i in range(0,len(new_list)):
        neues_list.append(new_list[i].split())
    print("Length o fneues list is: ",len(neues_list))
    print(neues_list)

    out_dict = {}
    for i in neues_list:
        for j in i:
            if j not in out_dict:
                out_dict[j] = 0
    for i in neues_list:
        for j in i:
            if j in out_dict:
                out_dict[j] = out_dict[j] + 1

    print("Length of dicitonary is: ", len(out_dict))
    
    print(out_dict)

except IOError:
    print("OIError")
