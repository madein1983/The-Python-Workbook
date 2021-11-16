import sys
import random

animals = ['Cat', 'Dog', 'Parot', 'Tiger','Dolphin', 'Elephant', 'Bird', 'Mouse','Fish', 'Panda']
for i in animals :
    if (i[len(i)-1] == 't') :
        print(i) 

print("\n")
numbers = []
k = 0
while k < 15 :
    randomNumber = random.randrange(1,20)
    numbers.append(randomNumber)
    if (randomNumber > 10) :
        print("Это число из списка больше десяти: " + str(randomNumber))
        k = k + 1
print(numbers)    