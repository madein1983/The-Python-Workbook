def reverseLookup(dict_of_pairs, line_in) :
    # Create list of keys    
    keys = []
    for key in dict_of_pairs :
        if dict_of_pairs[key] :
            keys.append(key)
    print("The list of keys is: ", keys)
    # Append the key to list after matched value of key and incoming variable
    resulting_key_list = []
    for key in dict_of_pairs :
        if dict_of_pairs[key] == line_in :
            resulting_key_list.append(key)
    print("The list resulting_key_list is: ", resulting_key_list)

    if line_in in dict_of_pairs.keys() or line_in in dict_of_pairs.values():
       print("It's in!")
       result = True

    else :
       print("Nope")
       result = False

    for i in dict_of_pairs :
        print("All values is: ", i, " : ", dict_of_pairs[i])

    return result




def main() :
    line_in = input("Enter key value: ")
    dict_of_pairs = {"First Name" : "Joan" , "Second Name" : "Ginger" , "Age" : "37"} 
    reverseLookup(dict_of_pairs,line_in)


if __name__ == "__main__" :
    main()