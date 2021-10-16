#TEN EVEN NUMBERS
import random
#for x in range(20): ## while NUmbOfEven is -lt 10 do
#    randomNumber= random.randrange(10, 1000)
#    if randomNumber % 2 == 0:
#        print ("The random number", randomNumber, "is even.")
#        ## here place some var to increment for example NumbOfEevn
#    elif randomNumber % 2 != 0:
#        print ("The random number", randomNumber, "is odd.")

odd = 0
while odd <= 9:
    randomNumber= random.randrange(10, 100)
    if randomNumber % 2 == 0:
        print ("The random number", randomNumber, "is even.")
        ## here place some var to increment for example NumbOfEevn
        odd = odd + 1
    elif randomNumber % 2 != 0:
        ##print ("The random number", random_number, "is odd.")
        print ("odd")
