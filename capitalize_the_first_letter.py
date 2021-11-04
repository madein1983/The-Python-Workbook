line = "day"
new_line = ""
for i in range(0,len(line)) :
    if i == 0 :
        new_line = new_line + line[i].upper()
    else :
        new_line = new_line + line[i]
print(new_line)    
    
