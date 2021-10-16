from math import pow

f = int(input("Enter the frequiency: "))

if 3*pow(10,9) > f :
    cathegory = "radiowaves"
elif 3*pow(10,9) < f and f < 3*pow(10,12) :
    cathegory = "microwaves"
elif 3*pow(10,12) < f and f < 4.3*pow(10,14) :
    cathegory = "infrared radiation"
elif 4.3*pow(10,14) < f and f < 7.5*pow(10,14) :
    cathegory = "visible radiation"
elif 7.5*pow(10,14) < f and f < 3*pow(10,17) :
    cathegory ="ultra violet radiation"
elif 3*pow(10,17) < f and f < 3*pow(10,19) :
    cathegory ="x-ray radiation"
elif 3*pow(10,17) < f :
    cathegory = "Y - radiation "
print(cathegory)

# >>> import sys
# >>> sys.float_info
# sys.floatinfo(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2
# 250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsil
# on=2.2204460492503131e-16, radix=2, rounds=1)

# import sys
# sys.float_info.max
# Output:
# 1.7976931348623157e+308