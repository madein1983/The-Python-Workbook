
phrase = input ("Enter the phrase: ")
shift = int(input("Enter the shift number: "))

# i = 0
new_phrase = ""
# print(chr)

for char in phrase :
    if  "a" <= char and char <= "z" :
        if shift > ord("z") - ord(char) :
            new_position = ord("a") + (shift - (ord("z") - ord(char)) - 1)
            new_phrase += chr(new_position)
        else :
            position = ord(char)
            new_position = position + shift
            new_phrase += chr(new_position)
         
    if "A" <= char and char <= "Z" :
        if shift > ord("Z") - ord(char) :
            new_position = ord("A") + (shift - (ord("Z") - ord(char))-1) 
            new_phrase += chr(new_position)
        else :
            position = ord(char)
            new_position = position + shift
            new_phrase += chr(new_position)

print(new_phrase)

print(ord("x"))
print(ord("y"))
print(ord("z"))
print(ord("a"))