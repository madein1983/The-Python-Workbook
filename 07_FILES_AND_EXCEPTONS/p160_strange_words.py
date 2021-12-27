import sys

if len(sys.argv) != 2 :
    print("argv count Error")
    quit()
try :
    file_container = open(sys.argv[1])
    lines_from_files = []
    lines_from_files = file_container.readlines()
    file_container.close()
    ei_word = []
    for i in lines_from_files:
        for j in range(0,len(i)) :
            if (i[j].upper() == "E" and  i[j+1].upper() == "I") or (i[j].upper() == "I" and  i[j+1].upper() == "E"):
                ei_word.append(i[:-2])
    #print(ei_word)
    
    new_file = open("p160_ei_word.txt","w")
    for i in ei_word:
        i = i+"\n"
        new_file.write(i)
    new_file.close()

    correct_spell = []
    incorrect_spell = []
    for i in ei_word:
        for j in range(0, len(i)-2): 
            if i[j].upper() == "C" and i[j+1].upper() == "E" and i[j+2].upper() == "I":
                correct_spell.append(i)
            if i[j].upper() == "C" and i[j+1].upper() == "I" and i[j+2].upper() == "E":
                incorrect_spell.append(i)
    print(correct_spell, incorrect_spell)
    

except IOError:
    print("IOError")
    quit()