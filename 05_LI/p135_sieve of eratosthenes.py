def list_of_simple_num(num_in) :
    full_list = []
    for i in range (0,num_in+1) :
        full_list.append(i)
    full_list[1] = 0
    full_list[2] = 0
    p = 2
    while p < num_in :
        for i in range(p*2, num_in+1, p) :
            full_list[i] = 0
        # full_list.remove(i)
        p = p + 1
        while p < num_in and full_list[p] == 0 :
            p = p + 1
    print("The list of simple numbers is: ")
    # simpl_nums_list = []
    for i in full_list :
        if full_list[i] !=0 :
            print(i)
            # simpl_nums_list.append(i)
    # print(simpl_nums_list)
def main() :
    num_in = int(input("Enter the upper number: "))
    list_of_simple_num(num_in)
    
if __name__ == "__main__" :
    main()