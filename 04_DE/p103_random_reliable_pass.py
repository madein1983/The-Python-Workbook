# Random reliable password generator 
from p100_random import curr_password
import p102_reliable_pass
def main() :
    rely = True
    counter = 0
    while rely != False :
        passw = curr_password()
        # print(passw)
        check = p102_reliable_pass.reliable(passw)
        if check :
            print(passw," is reliable password")
            counter +=1
            rely = False
        else :
            # print(passw," is NOT reliable password")
            counter +=1
    print("Attempts: ", counter)
if __name__ == "__main__" :
    main() 