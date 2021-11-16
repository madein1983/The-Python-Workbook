i = 1 
j = 1
for i in range(11) :
    for j in range(11) :
        element = i*j
        if j == 10 :
            print("", element, "")
        else :
            print("", element, "", end="")