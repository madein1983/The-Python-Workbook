length_of_wave = float(input("Enter the wavelength:  456:  "))
if length_of_wave <380 or length_of_wave > 750 :
    wave = "out of range"
elif 380 <= length_of_wave and length_of_wave < 450 :
    wave = "violet"
elif 450 <= length_of_wave and length_of_wave < 495 :
    wave = "blue"
elif 495 <= length_of_wave and length_of_wave < 570 :
    wave = "green"
elif 570 <= length_of_wave and length_of_wave < 590 :
    wave = "yellow"
elif 590 <= length_of_wave and length_of_wave < 620 :
    wave = "orange"
elif 620 <=length_of_wave and length_of_wave < 750 :
    wave = "red"
else :
    print("Something goes wrong!")
print(wave)


