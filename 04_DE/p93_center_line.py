from math import ceil
def center(s,w):
    if len(s) >= w :
       return s
    else :
        right_and_left_indent = ceil(w - len(s))/2)
        s = (" "*right_and_left_indent+s+" "*right_and_left_indent)
        return s
def main() :
    w = int(input("Enter window width: "))
    s = str(input("Enter string line: "))
    new_s = center(s,w)
    print(new_s)
if __name__ == "__main__" :
    main()