
from colorama import Fore, Back, Style, init
init()
from termcolor import colored

 # Hello World!

def unique(line_in) :
    list1 = []
    for i in range(0,len(line_in)) :
        list1.append(line_in[i])
    set1 = set(list1)
    print(line_in)
    print(Style.NORMAL + "The lenght of len(line_in): ", len(line_in))
    print(list1)
    print(Style.NORMAL + "The length of list1 is: ", len(list1))
    print(set1)
    print(Style.BRIGHT + "The length of set1 is: ", len(set1))
    print(Fore.RED + Back.WHITE + 'The unique symbols are ', len(set1))
    
    # Available formatting constants are:
    # Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Style: DIM, NORMAL, BRIGHT, RESET_ALL
    print(colored('Hello, World!', 'blue', 'on_yellow'))
    print(Style.RESET_ALL)
    print("normal")

def unique_from_book(line_in) :
    characters = {}
    for ch in line_in :
        characters[ch] = True
    print("The line contain", len(characters), " unique symbols!")


def main() :
    line_in = str(input("Enter string: "))
    unique(line_in)
    unique_from_book(line_in)

if __name__ == "__main__" :
    main()