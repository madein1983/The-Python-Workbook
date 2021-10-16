# Mathematical approximation of gas behavior during volume temperature and pressure changing
# PV = nRT
# P - pressure in Pascal, V - volume in litres, n - moll, R universal gas constant = 8,314 J/moll*Kelvin, T -temperature in Kelvin
# Let's find count of matter in molls:
P = 20000000
V = 12
Tk = 273.15
R = 8.314

C = float(input("Enter the temperature in celsium: "))
K = C + Tk # temperature in kelvin
F = (C*9/5)+32 # celsium to farenheit
n = (P*V)/(R*K) 
print(F)
print(n)
