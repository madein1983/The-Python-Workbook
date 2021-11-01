# Sentence for result checking: Is it crazy how saying sentences backwards createes backwards sentences saying how crazy it is
def is_string_palindrome(line_in):
    temp = []
    temp_rev = []
    temp = line_in.split()
    print("Print temp 1",temp)
    temp2 = temp.copy()
    temp2.reverse()
    print("Print temp 2",temp2)

    # let's find length of list
    #   
    length = 0  
    for i in temp :
        length +=1
    print("Length is: ",length)

    count = 0
    if length % 2 == 0 :
        for i in range(0,length//2) :
            if temp[i] == temp2[i] :
                count +=1
            print(temp[i], temp2[i])
        print("The amount of matches is: ", count )
        if count == length // 2 :
            return True
        else :
            return False

def main() :
    line_in = str(input("Enter sentence: "))
    result = is_string_palindrome(line_in)
    print(result)
if __name__ == "__main__" :
    main()