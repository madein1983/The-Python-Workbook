def erudite(line) :
    e_dict = {"A":"1","B":"3","C":"3","D":"2","E":"1","F":"4","G":"2","H":"4","I":"1","J":"8","K":"5","L":"1","M":"3", "N":"1","O":"1",\
              "P ":"3","Q":"10","R":"1","S":"1","T":"1","U":"1","V":"4","W":"4","X":"8","Y":"4","Z":"10"}
    line = line.upper()
    sum = 0
    print(e_dict.keys())
    print(e_dict.values()) # it gets all keys
    
    for i in line :
        # print(e_dict[i]) # !!!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!!!!!!!!!!! it gets values
        if i in e_dict :
           sum = sum + int(e_dict.get(i))
    print(sum)

def main():
    # line = input("Enter word: ")
    line = "qwerty"
    erudite(line)

if __name__ == "__main__" :
    main()