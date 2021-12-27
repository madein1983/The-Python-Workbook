    
inline = "12,122"    
    
temp = ""
for j in range(0,len(inline)):   
    
    if inline[j] != ',':
        print(inline[j])
        temp = temp+inline[j]
    elif inline[j] == ',':
        break
print("temp is: ",temp)
