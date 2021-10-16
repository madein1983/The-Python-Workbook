#import random
from random import randint

#bet = int(input("Enter the number: "))

#win = random.randint(0,38)
win = randint(0,37)
if win == 1 or  win == 3 or  win == 5 or  win == 7 or  win == 9 or  win == 12 or  win == 14 or  win == 16 or  win == 18 or  win == 19 \
   or  win == 21 or  win == 23 or  win == 25 or  win == 27 or  win == 30 or  win == 32 or  win == 34 or  win == 36 :
    color = "Red"
    
elif  win == 2 or  win == 4 or  win == 6 or  win == 8 or win == 10 or  win == 11 or  win == 13 or  win == 15 or  win == 17 \
     or  win == 20 or  win == 22 or  win == 24 or  win == 26 or  win == 28 or  win ==29  or  win == 31 or  win == 33 or  win == 35 :
    color = "Black"

if win == 0 or win == 38 :
    isEven = ""
elif (win % 2) == 0 :
    isEven = "Even"
elif  (win % 2) != 0 :
    isEven = "Odd"
else :
    print("O_O-1")
    
if 1 <= win and win <= 18 :
    range = "From 1 to 18"
elif 19 <= win and win <= 36 :
    range = "From 19 to 36"
elif win == 0 or win == 37 :
    range = ""
else  :
    print("O_O-2")

if win == 0 :
    print ("The win number is: ", win)
    print ("The win bet is:", win)
elif win == 37 :
    print ("The win number is: 00 ")
    print ("The win bet is: 00")
elif 1 <= win and win <= 36 :
    print ("The win number is: ", win)
    print ("The win bet is:", color) 
    print ("The win bet is:", isEven) 
    print ("The win bet is:", range) 
else :
    print("O_O-3")
