from colorama import Fore, init
init()


def anagram(line) :
    line = line.upper()
    temp = ""
    for i in range(0, len(line)) :
        if ord("A") < ord(line[i]) and ord(line[i]) < ord("Z") :
            temp = temp + line[i]
    print(temp)
    dict0 = {}
    for j in line :
        if j in dict0 :
            dict0[j] = dict0[j] + 1
        else :
            dict0[j] = 1
    print(dict0)
    return dict0

def main() :
    
    line1 = input("line1: ")
    line2 = input("line2: ")
    
    l1 = anagram(line1)
    l2 = anagram(line2)
    
    if l1 == l2 :
        print(Fore.YELLOW + "this sentences are anagrams")
    else :
        print(Fore.GREEN + "they are NOT")

if __name__ == "__main__" :
    main()