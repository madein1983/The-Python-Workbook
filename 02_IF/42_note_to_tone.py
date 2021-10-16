FREQ_C4 = 261.63
FREQ_D4 = 239.66
FREQ_E4 = 329.63
FREQ_F4 = 349.23
FREQ_G4 = 392.00
FREQ_A4 = 440.00
FREQ_B4 = 493.88

name = input("Enter the name of note, for example E4: ")
note = name[0]
octave = float(name[1])
if note == "C" :
    freq = FREQ_C4
elif note == "D" :
    freq = FREQ_D4
elif note == "E" :
    freq = FREQ_E4 
elif note == "F" :
    freq = FREQ_F4
elif note == "G" :
    freq = FREQ_G4
elif note == "A" :
    freq = FREQ_A4
elif note == "B" :
    freq = FREQ_B4
else :
    freq = "100000"

freq_of_octave = freq/2**(4-octave)
print(" The note freqiency is: %.2f" % freq_of_octave)