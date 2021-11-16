# psi pounds square inch
# kPa -> psi  1kPa = 0,145038 psi   1 psi  = 6.89476 kPa
# kPa -> mmhg 1kPA = 7.50062 mmhg   1 mmhg = 0.133322 kPa
# kPa -> atm  1kPa = 0.00986923 atm 1 atm  = 1.1325 kPa 
kpa = float(input("Enter the value in kPa: "))
CONST_PSI = 0.145038 
psi = CONST_PSI * kpa
print(psi)
CONST_MMHG = 7.50062
mmhg = CONST_MMHG * kpa
print(mmhg)
CONST_ATM = 0.00986923
atm = CONST_ATM * kpa
print(atm)
