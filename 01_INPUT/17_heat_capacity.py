# heat capacity C 
# total sum requiered enrgy q  
# m - mass of the material
# dT - required delta temperature
# q = m*C*dT
# FOR  WATER specific heat capacity equal to 4,186 J/gramm*t   dencity of water 1 gramm/ml

# request mass of water
m = int(input("Enter the mass in millilitres: "))
dT1 = int(input("Enter the start temperature: ")) 
dT2 = int(input("Enter the end of temperature: "))
time_to_heat = int(input("Enter the time you need to heat the water: "))
energyJ = m*4.186*(dT2-dT1)
print(energyJ, "J")
# Formula Joules to KWatt/hour 
# P(W) = E(J) / t(s)
kWtt = energyJ/time_to_heat
print(kWtt)
