
def isSubList (list_of_items,sub_list) :
    index_arr = []
    counter = 0
    for i in range(0,len(sub_list)) :
        for j in range(0,len(list_of_items)) :
            if sub_list[i] == list_of_items[j] :
                list_of_items.index(sub_list[i])
                index_arr.append(list_of_items.index(list_of_items[j]))
    for k in range(0,len(index_arr)-1) :
        if index_arr[k+1] - index_arr[k] == 1 :
            counter += 1
    if counter == len(index_arr)-1 :
        print("list of intems include sub_list")
    else :
        print("list of intems NOT include sub_list")
    print(index_arr)

def main ():
    # empty one and more elements
    # list_of_items = list()
    # sub_list = list()
    # line_in =" "
    # i = 0
    # while line_in != "" :
    #     line_in = input("Enter big list element(Enter to exit): ")
    #     if line_in != "" :
    #        list_of_items.append(line_in)
    #     i += 1
    # list_of_items = [1,2,3,4,5,6,7,8,9,10,11,12]
    # sub_list = [3,4,5,6,7,8,9,10]
    list_of_items = ["volvo", "WV", "GM", "TOYOTA"]
    sub_list = ["WV", "TOYOTA"]
    print(list_of_items)
    # line_in = " "
    # i = 0
    # while line_in != "" :
    #     line_in = input("Enter small list element(Enter to exit): ")
    #     if line_in != "" :
    #         sub_list.append(line_in)
    #     i += 1
    print(sub_list)
    if len(sub_list) == 0 :
        print("The list is empty! ")
    elif len(sub_list) == 1 :
        print("The list contain only one item")
    else :
        print("The sub_list contain {}".format(len(sub_list)))
    isSubList(list_of_items,sub_list)
if __name__ == "__main__" :
    main()