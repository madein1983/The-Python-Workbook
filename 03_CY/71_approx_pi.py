peee = 3
even_flag = 1

for i in range(2,32,2) :
    if even_flag % 2 != 0 :
        current = (4/(i*(i+1)*(i+2)))
        peee = peee + current
        print(peee)
        even_flag += 1
    else :
        current = (4/(i*(i+1)*(i+2)))
        peee = peee - current
        print(peee)
        even_flag += 1