from random import randint, random

def old_plate():
    plate = ""
    i = 0
    for i in range(0,3) :
        curr_ord = randint(65,90)
        plate = plate + chr(curr_ord)
    i = 0
    for i in range(0,3):
        curr_ord = randint(48,57)
        plate = plate + chr(curr_ord)
    print(plate)

def new_plate():
    plate = ""
    i = 0
    for i in range(0,4):
        curr_ord = randint(48,57)
        plate = plate + chr(curr_ord)
    i = 0
    for i in range(0,3) :
        curr_ord = randint(65,90)
        plate = plate + chr(curr_ord)

    print(plate)



def main():
    old_or_new = randint(0,1)
    if old_or_new == 0 :
        old_plate()
    else :
        new_plate()


if __name__ == "__main__":
    main()