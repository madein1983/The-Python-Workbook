def up_case(s):
    l = ""
    i = 0
    while i <= (len(s)-1):
        if (ord("a") <= ord(s[i]) and ord(s[i]) <= ord("z")) and s[i-1] == " " : # ord("a")=97 ord("z")=122
            t = ord(s[i])-32 
            l = l + chr(t)
        else :
             l = l + s[i]    
        i += 1
    return l

def ordy(x) :
    j = 0
    while j <= x :
        print(j," ",chr(j))
        j += 1


def main():
    s = input("Enter text: ")
    # print(len(s))
    # new_line = up_case(s)
    # print(new_line)
    x = int(input(" Enter from 0 to 255: "))
    ordy(x)
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    # s[i] == "i" and i!=0 and (s[i-1] == " "  or s[i-1]== "." or s[i-1]== "!" or s[i-1]== "?" or s[i-1]== ";" or s[i-1]== "," ) :
    #         l += "I"
    #     elif
    
    
    # l = ""
    # print(l)
    # for j in range(len(s)):
    #     l = l+" "
    # print(l)
    # 