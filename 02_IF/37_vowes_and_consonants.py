letter = str(input("Enter the letter: "))
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' :
    print("The letter %s is vowel" % letter)
elif letter == 'y' :
    print("The letter %s could be vowel or consonant" % letter)
else :
    print("The letter %s is consonant" % letter)
