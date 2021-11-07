def countRange(list_in, min_range,max_range) :
    print(list_in.count(5))
    counter = 0
    for i in range (0, len(list_in)) :
        if min_range <= list_in[i] and list_in[i] < max_range :
           counter +=1 
    print("Total matches: ",counter)

def main() :
    list_in = list()
    line_in = str(input("Enter the elements of list: "))
    list_in.append(line_in)
    while line_in != "" :
        line_in = str(input("Enter the elements of list: "))
        if line_in != "" :
            list_in.append(line_in)
    min_range = input("Enter lower edge: ")
    max_range = input("Enter upper edge: ")
    print(line_in)
    countRange(list_in, min_range,max_range)
    # list_in = [1,5,5,2.3,10,12,55,55,61,92]
    # min_range = 10
    # max_range = 50

if __name__ == "__main__" :
    main()