from math import floor
a = int(input(" Enter number more than 2: "))
factor = 2

while  factor <= a :
        if (a % factor) == 0 :
            print(factor, " простой множитель числа ", a)
            a = floor(a/factor)
        else :
            factor += 1