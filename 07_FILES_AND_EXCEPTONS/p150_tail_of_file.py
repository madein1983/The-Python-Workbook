import sys

if len(sys.argv) != 2 :
    print("count of argv != 2 quit()")
    quit()

file_cont = open(sys.argv[1],"r")

line_in = file_cont.readline()
while line_in != "" :
    
