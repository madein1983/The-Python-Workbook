import sys
NUM_OF_LINES = 10

if len(sys.argv) != 2 :
    print("there is two  arguments needed!")
    quit()

try:
    inf = open(sys.argv[1],"r")
    # file_opened = True
    line = inf.readline()
    num = 0
    while num < NUM_OF_LINES and line != "":
        line = line.rstrip()
        num +=1
        print(line)
        line = inf.readline()
    inf.close()

except IOError:
    print("IOError. Exit")
    quit()