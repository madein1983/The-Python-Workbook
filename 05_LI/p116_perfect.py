from p115_list_of_personal_denomi import list_of_denumerators

def perfect_numbers(temp_arr_for_check, line_in):
    sum = 0
    for i in temp_arr_for_check :
        sum += i
    if sum == line_in :
        return True
    else :
        return False

def from_1_to_1000() :
    for i in range(1,100000) :
        temp_arr = list_of_denumerators(i)
        temp_res = perfect_numbers(temp_arr,i)
        if temp_res :
            print(i)


def main():
    line_in = int(input("Enter number IN P116: "))
    list_of_denumerators(line_in)
    print(list_of_denumerators(line_in),"we backed into the main program ")
    is_perfect_number = perfect_numbers(list_of_denumerators(line_in),line_in)
    print(is_perfect_number)
    from_1_to_1000()

if __name__ == "__main__" :
    main()

