from random import randint
i=0
len_line = 0
while i <=9 : 
    line = ""
    j = 0
    exit_flag = False
    
    while exit_flag == False :
        a = randint(0,1)
        line = line + str(a)
        if j >=2 and line[j] == line[j-1] and line[j-1] == line[j-2] :
            print(line, "count: ",len(line))
            exit_flag = True
        j +=1
    i +=1
    len_line = len_line + len(line)
print("The average of 10 attempts is: ",len_line/10)


