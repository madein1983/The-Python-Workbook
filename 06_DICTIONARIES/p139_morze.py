


#  You can always depend on me when you need it

def morze_converter(line_in) :
    morze = { "A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", \
              "J" : ".---", "K" : "-.-","L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.", "Q" : "--.-", "R" : ".-.", \
              "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-", "Y" : "-.--", "Z" : "--..", "0" : "-----", \
              "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..", \
              "9" : "----."  }
    line_out = ""
    for i in range(0,len(line_in)) :
        for j in morze :
            if line_in[i] == j :
               line_out = line_out + " " + str(morze.get(j))
        
    print(line_out)



def main() :
    line_in = input("Enter text: ")
    line_in = line_in.upper()
    morze_converter(line_in)


if __name__ == "__main__" :
    main()