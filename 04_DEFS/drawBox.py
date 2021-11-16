def drawBox () :
    print("************")
    print("*          *")
    print("*          *")
    print("*          *")
    print("*          *")
    print("************")

drawBox()

width = int(input("Enter height: "))
height = int(input("Enter width:  "))
outline = str(input("Enter outline char: "))
fill = str(input("Enter the fill char: "))
def drawBox1(width,height,outline,fill) :
    if width <2 or height < 2 :
        print("It's imposiible to draw.")
        quit()
    print("*"*width)
    for i in range(width) :
        print (outline + fill * (width-2) + outline)
    print("*"*width)

drawBox1(width, height,outline,fill)


