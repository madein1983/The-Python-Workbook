import sys
from random import randint
def first_lett_capit(word):
    new_word = ""
    for i in range(0,len(word)):
        if i == 0 :
            new_word = word[0].upper()
        if i != 0 :
            new_word = new_word + word[i]
    print(new_word)
    return new_word
def main():
    if len(sys.argv) != 2 :
        print("argv len error")
    file_container = open(sys.argv[1])
    lines = []
    lines = file_container.readlines()
    file_container.close()
    # print(line[155],line[54654])
    # 10: 3+7 4+6 5+5  # 9:  3+6 4+5  # 8:  3+5 4+4 
    words_3_7_char = []
    for i in lines :
        if 3 <= len(i[:-2]) and len(i[:-2]) <= 5 :
            # print(i[:-2])
            words_3_7_char.append(i[:-2])
    # print(words_3_7_char,len(words_3_7_char))
    first_word_index = randint(0,len(words_3_7_char))
    first_word = words_3_7_char[first_word_index]
    second_word_index = randint(0,len(words_3_7_char))
    second_word = words_3_7_char[second_word_index]
    # print(first_word)
    final_password = first_lett_capit(first_word)
    sum_of_length = len(first_word) + len(second_word)
    
    while  sum_of_length < 6 and sum_of_length > 10:
        second_word_index = randint(0,len(words_3_7_char))
        second_word = words_3_7_char[second_word_index]
    final_password = first_lett_capit(first_word) + first_lett_capit(second_word)
    print(final_password)
if __name__ == "__main__":
    main()