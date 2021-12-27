import sys
if len(sys.argv) != 2:
    print("argv count Error! quit")
    quit()

def number(inline):
    temp = ""
    for j in range(0,len(inline)):   
        if str(inline[j]) != ',':
            temp = temp+inline[j]
        elif str(inline[j]) == ',':
            break
    return temp

def main():
    try: 
        fc = open(sys.argv[1])
        #lst = []
        #lst = fc.readlines()
        #print(lst)
        lst1= []
        line = fc.readline()
        while line != "":
            lst1.append(line)
            line = fc.readline()
        fc.close()
        # print(lst1)
        dict1 = {}
        for i in lst1:
                dict1[number(i)] = i
        # print(dict1)
        line_in = input("Enter number of element: ")
        while line_in != "":   
            for key, values in dict1.items():
                if int(line_in) == int(key):
                    print(key,values)
            line_in = input("Enter number of next element: ")
            if line_in == '' :
                quit()

    except IOError:
        print("Except OIError")
        quit()

if __name__ == '__main__':
    main()