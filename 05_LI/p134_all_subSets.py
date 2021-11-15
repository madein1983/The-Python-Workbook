def from_book(data) :
    sublists = [[]]
    for i in range(1,len(data)+1) :
        for j in range(0,len(data) - i + 1) :
            sublists.append(data[j:j+i])
            print((data[j:j+i]))
            
    return sublists

def main() :
    data = [1,2,3,4,5,6,7,8,9,0]
    from_book(data)
    print(len(data))
if __name__ == "__main__" :
    main()