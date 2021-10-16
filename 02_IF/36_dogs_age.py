# 
dogs_age_in = int(input("Enter the dogs age: "))
if dogs_age_in == 1 :
    print("The human's equivalent of dogs age", dogs_age_in," is 10,5 year.")
elif dogs_age_in == 2 :
    print("The human's equivalent of dogs age", dogs_age_in," is 21 year.")
elif dogs_age_in < 0 :
    print ("You made a mistake, please repeat")
else :
    the_humans_age_equi = (dogs_age_in - 2)*4
    print ("The human's equivalent of dogs age ", dogs_age_in," is ", the_humans_age_equi)