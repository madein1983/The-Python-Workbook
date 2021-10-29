def p110sorted_modified(arr) :
    arr.sort()
    print("Прямой порядок: ", arr)
    arr.pop()
    # for i in arr :
    #     print(i)
    arr.reverse()
    print("Обратный порядок: ", arr)
    arr.pop()
    arr.reverse()
    print("Фин.удал-е экстр.: ",arr)
    # for i in arr :
    #     print(i)
def main():
    arr =[]
    counter = 0
    line_in = int(input("Enter value(0 - to exit): "))
    arr.append(line_in) 
    while line_in != 0 :
        line_in = int(input("Enter value(0 - to exit): "))
        if line_in != 0 :
            arr.append(line_in) 
            counter += 1
        if counter < 4 and line_in == 0 :
             print("The total number should be four or more!")
    p110sorted_modified(arr)
if __name__ == "__main__" :
    main()