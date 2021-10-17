from random import randint
j = 0
the_max = randint(1,100)

for i in range(1,100) :
    curr_rand = randint(1,99)
    #print(i," : ", curr_rand)
    if curr_rand > the_max :
        the_max = curr_rand
        j += 1 
        if i >= 10 :
            print (i," | ",the_max, "<= Updat max")
        else :
            print (i,"  | ",the_max, "<= Updat max")

print (j)