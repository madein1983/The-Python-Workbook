
def allchars() :
    for i in range(0,500) :
        print("|_ ", i, " _|_ ",chr(i), "_|")

def pull_words(line_in):
    words_arr = []
    i = 0
    new_string = ""
    while i <= (len(line_in) - 1) :
        if (65 <= ord(line_in[i]) and ord(line_in[i]) <= 90) or  (97 <= ord(line_in[i]) and ord(line_in[i]) <= 122) or ord(line_in[i]) == 39 or ord(line_in[i]) == 32  :
            new_string = new_string + line_in[i]
        i +=1    
    print(new_string)
    return new_string

def string_to_list (new_string) : 
    new_list = new_string.split()
    print(new_list)    # this is common method but we will go further =>

def string_to_list_old_school(new_string) :
    i = 0
    new_list = []
    temp = ""
    while i <= (len(new_string)-1) :
        if new_string[i] != " " :
           temp = temp + new_string[i] 
        elif new_string[i] == " " :
           new_list.append(temp)
           temp =""
        i += 1
    print("and again old school", new_list)

def main():
    line_in = str(input("Enter sentence: "))
    # print(allchars())
    new_string = pull_words(line_in)
    string_to_list(new_string)
    # print(string.printable)
    string_to_list_old_school(new_string)
if __name__ == "__main__" :
    main()
    # Contraction include: don't isn't and wouldn't 