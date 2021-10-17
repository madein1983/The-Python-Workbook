line  = input("Enter the binary for example 0100101: ")
i = 0
num = 0
print("Long: ", len(line))
for i in range(len(line)) :
    
     if line[i] == "0" or line[i] == "1" :
         print("iteration is ", i, " | ", end="")
         curr = int(line[i]) * int(pow(2,len(line)-i-1))
         print("int(line[i])", int(line[i]), " * ","int(pow(2,len(line)-i-1) ", int(pow(2,len(line)-1) ), "curr is: ", curr)  
         num = curr + num
         
print("DEC" , num) 
       

