car_num = str(input("Enter the plate number: "))
car_num = car_num.upper()


if 6 > len(car_num) or len(car_num) > 7 :
    print("You entered a wrong number")
elif len(car_num) == 6 \
     and "A" <= car_num[0] and car_num[0] <= "Z" \
     and "A" <= car_num[1] and car_num[1] <= "Z" \
     and "A" <= car_num[2] and car_num[2] <= "Z" \
     and  0  <= int(car_num[3]) and int(car_num[3]) <=  9  \
     and  0  <= int(car_num[4]) and int(car_num[4]) <=  9  \
     and  0  <= int(car_num[5]) and int(car_num[5]) <=  9  :

    print("The car plate is 6th numbered old-style shit")

elif len(car_num) == 7 \
    and 0 <= int(car_num[0]) and int(car_num[0]) <= 9 \
    and 0 <= int(car_num[1]) and int(car_num[1]) <= 9 \
    and 0 <= int(car_num[2]) and int(car_num[2]) <= 9 \
    and 0 <= int(car_num[3]) and int(car_num[3]) <= 9 \
    and "A" <= car_num[4] and car_num[4] <= "Z" \
    and "A" <= car_num[5] and car_num[5] <= "Z" \
    and "A" <= car_num[6] and car_num[6] <= "Z" :
    
    print("The car plate is 7th numbered new-style shit")


else :
    print("O_O")
    print(len(car_num))