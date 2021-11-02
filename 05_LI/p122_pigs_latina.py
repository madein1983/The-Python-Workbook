def  vowel(temp) :
    temp = temp + "way"
    print(temp)

def consonant(temp):
    word = ""
    for i in range(0,len(temp)):
        if temp[i] == "b" or temp[i] == "c" or temp[i] == "d" or temp[i] == "f" or temp[i] == "g" or temp[i] == "j" or temp[i] == "k" \
            or temp[i] == "l" or temp[i] == "n" or temp[i] == "o" or temp[i] == "p" or temp[i] == "r" or temp[i] == "s" or temp[i] == "t" \
            or temp[i] == "v" or temp[i] == "w" or temp[i] == "x" or temp[i] == "y" or temp[i] == "z":
            prefix = temp[0:i]                           #  1
        else :#                                             2  because of this four lines i ...................... ;)
            break#                                          3
    word =  temp[len(prefix):len(temp)] + prefix + "ay"#    4 
    print(word)
def pigs_latina(line_in) :

    in_arr = list()
    in_arr = line_in.split()
    print(in_arr)
    temp = ""
    for i in range(0,len(in_arr)) :
        temp = in_arr[i]
        temp = temp.lower()
        if temp[0] == "a" or temp[0] == "e" or temp[0] == "i" or temp[0] == "o" or temp[0] == "u" or temp[0] == "y" :
            print("vowel: ",temp)
            vowel(temp)
        elif temp[0] == "b" or temp[0] == "c" or temp[0] == "d" or temp[0] == "f" or temp[0] == "g" or temp[0] == "j" or temp[0] == "k" \
            or temp[0] == "l" or temp[0] == "n" or temp[0] == "o" or temp[0] == "p" or temp[0] == "r" or temp[0] == "s" or temp[0] == "t" \
                or temp[0] == "v" or temp[0] == "w" or temp[0] == "x" or temp[0] == "z" :
            print("consonant: ", temp)
            consonant(temp)
            

def main() :
    line_in = str(input("Enter phrase: "))
    pigs_latina(line_in)

if __name__ == "__main__" :
    main()