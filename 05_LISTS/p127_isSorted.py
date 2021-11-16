

def isSorted(list_in) :
    print(min(list_in), max(list_in)) 
    if len(list_in) == 0 or len(list_in) == 1 :
        print("List is too short!")
    elif min(list_in) == list_in[0] and max(list_in) == list_in[len(list_in)-1]:
        print("List sorted ascendetly")
    elif max(list_in) == list_in[0] and min(list_in) == list_in[len(list_in)-1]:
        print("List sorted descendently")
    else :
        print("list unsorted")



def main() :
    list_in = list()
    line_in = str(input("Enter the elements of list: "))
    list_in.append(line_in)
    while line_in != "" :
        line_in = str(input("Enter the elements of list: "))
        if line_in != "" :
            list_in.append(line_in)
    print(list_in)
    print(line_in)
    isSorted(list_in)

if __name__ == "__main__" :
    main()