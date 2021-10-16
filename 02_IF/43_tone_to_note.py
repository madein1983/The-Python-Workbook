FREQ_C4 = 261.63
FREQ_D4 = 239.66
FREQ_E4 = 329.63
FREQ_F4 = 349.23
FREQ_G4 = 392.00
FREQ_A4 = 440.00
FREQ_B4 = 493.88 
DELTA   =   1

frq = float(input("Enter the frequiency in Herz, for example 655.32: "))

if (FREQ_C4 - DELTA) <= frq and frq <= (FREQ_C4 + 1)  :
    note = "C4"
elif (FREQ_D4 - DELTA) <= frq and frq <= (FREQ_D4 + 1) :
    note = "D4"
elif (FREQ_E4 - DELTA) <= frq and frq <= (FREQ_E4 + 1) :
    note = "E4"
elif (FREQ_F4 - DELTA) <= frq and frq <= (FREQ_F4 + 1) :
    note = "F4"
elif (FREQ_G4 - DELTA) <= frq and frq <= (FREQ_G4 + 1) :
    note = "G4"
elif (FREQ_A4 - DELTA) <= frq and frq <= (FREQ_A4 + 1) :
    note ="A4"
elif (FREQ_B4 - DELTA) <= frq and frq <= (FREQ_B4 + 1) :
    note = "B4"
else :
    note = "there is no such note in this range!"

print ("Entered frequency corresponds to ", note)
