from random import randint 
from colorama import Fore, Back, init
init()

def initial_spread() :
    lotto = {}
    b_list = []
    i_list = []
    n_list = []
    g_list = []
    o_list = []

    bingo = "bingo"
    for i in bingo :
        if i == "b" :
            for j in range(1,16):
                b_list.append(j)
            lotto[i] = b_list
    for i in bingo :
        if i == "i" :
            for j in range(16,31):
                i_list.append(j)
            lotto[i] = i_list
    for i in bingo :
        if i == "n" :
            for j in range(31,46):
                n_list.append(j)
            lotto[i] = n_list
    for i in bingo :
        if i == "g" :
            for j in range(46,61):
                g_list.append(j)
            lotto[i] = g_list
    for i in bingo :
        if i == "o" :
            for j in range(61,75):
                o_list.append(j)
            lotto[i] = o_list
    print(lotto)
    return lotto

def randomize_card(column) :
    rand_col = []
    if column == "b":
        for k in range(1,50) :
            r = randint(1,15)
            if len(rand_col) < 5 and r not in rand_col :
                rand_col.append(r)
    elif column == "i":
        for k in range(1,45) :
            r = randint(16,30)
            if len(rand_col) < 5 and r not in rand_col :
                rand_col.append(r)
    elif column == "n":
        for k in range(1,45) :
            r = randint(31,45)
            if k == 3 :
                rand_col.append(0)
            if len(rand_col) < 5 and r not in rand_col :
                rand_col.append(r)
    elif column == "g":
        for k in range(1,45) :
            r = randint(46,60)
            if len(rand_col) < 5 and r not in rand_col :
                rand_col.append(r)
    elif column == "o":
        for k in range(1,45) :
            r = randint(61,75)
            if len(rand_col) < 5 and r not in rand_col :
                rand_col.append(r)
    return rand_col
    
def take_card(lotto) :
    b = randomize_card("b")
    i = randomize_card("i")
    n = randomize_card("n")
    g = randomize_card("g")
    o = randomize_card("o")
    print(Fore.GREEN + "B " + Fore.BLUE + " I " + Fore.CYAN + " N " + Fore.BLUE + " G " +Fore.RED + " O " )
    for m in range(0,len(b)):
        print(Fore.GREEN + str(b[m]), Fore.BLUE + str(i[m]), Fore.CYAN + str(n[m]),Fore.BLUE + str(g[m]), Fore.RED + str(o[m]))
    return b,i,n,g,o

def main():
    lotto = initial_spread()
    print(lotto)
    take_card(lotto)

if __name__ == "__main__" :
    main()








