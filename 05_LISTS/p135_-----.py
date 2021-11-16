def list_of_simple_num(num_in) :
    full_list = []
    for i in range (2,num_in+1) :
        full_list.append(i)
    # print("The full list                  ",full_list)
    p = 2
    for i in range(2, num_in+1, p) :
        # full_list[i] = 0
        full_list.remove(i)
    # full_list.remove(full_list[0])
    # print("After removed even numbers:    ",full_list)
    simpl_num_list = []
    
    for j in full_list :
        if num_in % j != 0 :
            simpl_num_list.append(j)
    print("The list of simple numbers is: ", simpl_num_list)

def main() :
    num_in = int(input("Enter the upper number: "))
    list_of_simple_num(num_in)
    
if __name__ == "__main__" :
    main()