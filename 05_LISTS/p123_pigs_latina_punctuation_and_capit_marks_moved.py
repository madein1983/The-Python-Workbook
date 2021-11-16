# test phrase:  Good day, Mister Fix! Outta fill!
# difference
# punctuation ranges 33 - 47 58-64 91-96 123 ->
def move_punctuation_marks(new_word) :
    moved_punctuation = ""
    cut = ""
    for i in range(0,len(new_word)):
        if (33 <= ord(new_word[i]) and ord(new_word[i]) <= 47) or (58 <= ord(new_word[i]) and ord(new_word[i]) <= 64) or ( 91 <= ord(new_word[i]) \
            and ord(new_word[i]) <= 96 ) or (123 < ord(new_word[i])) :
            cut = cut + new_word[i]
        else :
            moved_punctuation = moved_punctuation + new_word[i]
    moved_punctuation = moved_punctuation + cut
    new_word = moved_punctuation
    return new_word
# difference
def cap_the_first_letter(new_word) :
    capitalized_new_word = ""
    for i in range(0,len(new_word)) :
        if i == 0 :
            capitalized_new_word = capitalized_new_word + new_word[i].upper()
        else :
            capitalized_new_word = capitalized_new_word + new_word[i]
    new_word = capitalized_new_word
    return new_word
# difference
def  vowel(word) :
    # difference
    word = (word + "way").lower()
    new_word = cap_the_first_letter(word)
    new_word = move_punctuation_marks(new_word)
 # difference
    return new_word

def consonant(word):
    i = 0
    prefix = ""
    while word[i] != "a" and word[i] != "e" and word[i] != "i" and word[i] != "o" and word[i] != "u" and word[i] != "i" :
        prefix = prefix + word[i]
        i +=1
    #Good day, Mister Fix! Outta fill!
    new_word = (word[len(prefix):] + prefix + "ay").lower()
# difference
    new_word = cap_the_first_letter(new_word)
    new_word = move_punctuation_marks(new_word)
# difference
    return new_word

def pigs_latina(line_in) :
    in_arr = list()
    out_arr = []
    in_arr = line_in.split()
    print(in_arr)
    word = ""
    for i in range(0,len(in_arr)) :
        word = in_arr[i]
        if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] == "y" :
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