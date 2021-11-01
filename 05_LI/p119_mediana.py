from math import ceil

def sum(fl_arr) :
    s = 0
    for i in fl_arr :
        s = s + i
    print("The sum is: ", s) 

def length(fl_arr):
    length = 0
    for i in fl_arr :
        length +=1
    print("The list length is: ", length)
    return length

def mediana(fl_arr):
    l = length(fl_arr)
    if l % 2 != 0 :
       mediana_index = ceil(l / 2)-1
       print ("Mediana is: ", fl_arr[mediana_index])
    else :
       mediana = (fl_arr[l//2] + fl_arr[(l//2) + 1])
       print("Mediana is: ", mediana)

def main():
    fl_arr = []
    line_in = input(" Enter values(Enter to exit: ") 
    if line_in.isnumeric() :
         fl_arr.append(float(line_in))
    
    while line_in != "" :
        line_in = input("Enter values(Enter to exit: ")
        if line_in.isnumeric() :
            fl_arr.append(float(line_in))
    
    print("Initial list: ", fl_arr)
    fl_arr.sort() # sort ascending
    print("Ascending sorted list: ",fl_arr)
    fl_arr.sort(reverse=True) # reverse list descending
    print("Descending sorted list:",fl_arr)
    
    sum(fl_arr)
    length(fl_arr)
    mediana(fl_arr)


if __name__ == "__main__":
    main()
