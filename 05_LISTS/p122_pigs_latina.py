def  vowel(word) :
    word = word + "way"
    return(word)

def consonant(word):
    i = 0
    prefix = ""
    while word[i] != "a" and word[i] != "e" and word[i] != "i" and word[i] != "o" and word[i] != "u" and word[i] != "i" :
        prefix = prefix + word[i]
        i +=1
    new_word = word[len(prefix):] + prefix + "ay"
    return new_word

def pigs_latina(line_in) :
    in_arr = list()
    out_arr = []
    in_arr = line_in.split()
    # print(in_arr)
    word = ""
    for i in range(0,len(in_arr)) :
        word = in_arr[i]
        word = word.lower()
        if word[0] == "a" and word[0] == "e" and word[0] == "i" and word[0] == "o" and word[0] == "u" and word[0] == "y" :
            new_word = vowel(word)
            out_arr.append(new_word)
        elif word[0] != "a" and word[0] != "e" and word[0] != "i" and word[0] != "o" and word[0] != "u" and word[0] != "y" :
            new_word = consonant(word)
            out_arr.append(new_word)
    # print(out_arr)
    line_out = ""
    for i in range(0, len(out_arr)) :
        line_out = line_out + " " + out_arr[i]
    print(line_out)

def main() :
    line_in = str(input("Enter phrase: "))
    pigs_latina(line_in)
if __name__ == "__main__" :
    main()