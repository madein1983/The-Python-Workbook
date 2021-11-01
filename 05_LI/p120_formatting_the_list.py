def main() :
    str_arr = []
    str_in = str(input("Enter words( Enter to exit: "))
    str_arr.append(str_in)
    
    while str_in != "" :
        str_in = str(input("Enter words( Enter to exit: "))
        if str_in != "" :
            str_arr.append(str_in)
    
    if len(str_arr) == 1 :
        print(str_arr, len(str_arr))
    elif len(str_arr) == 2 :
        print(str_arr[0] + " и " + str_arr[1])
    elif len(str_arr) > 2 :
       temp = ""
       for i in range(0, len(str_arr)-2 ) :
            temp = temp + str(str_arr[i])+", "
       temp = temp + str(str_arr[len(str_arr)-2]) + " и " + str(str_arr[len(str_arr)-1])
       print(temp)

if __name__ == "__main__" :
    main()
