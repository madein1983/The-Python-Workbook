def calc_m(ax,ay):
    
    print("sum of X: ",sum(ax))
    print("sum of Y: ",sum(ay))

    sum_of_mult_x_and_y = 0
    for i in range(0,len(ax)) :
        sum_of_mult_x_and_y = sum_of_mult_x_and_y + ax[i]*ay[i]
    print("sum_of_mult_x_and_y: ",sum_of_mult_x_and_y)
    sum_of_sq_of_x = 0
    for i in range(0,len(ay)):
        sum_of_sq_of_x = sum_of_sq_of_x + ax[i]**2
    print("sum_of_sq_of_x", sum_of_sq_of_x)
    m = (sum_of_mult_x_and_y - ((sum(ax)*sum(ay))/len(ax)))/ (sum_of_sq_of_x -(sum(ax)**2)/len(ax))
    print("M = ",m)
    return m

def calc_b(ax,ay,m) :
    print(sum(ay))
    print(sum(ax))
    print(m)
    b = sum(ay) - (sum(ax)*m)
    print("The b is equal: ",b)
    return b


def main():
    ax =list()
    ay = list()
    x = float(input("Enter x(Enter to exit): "))
    ax.append(x)
    y = float(input("Enter y(Enter to exit): "))
    ay.append(y)
    while x != "":
        
            
        x = input("Enter x(Enter to exit): ")
        if x == "":
            break
        ax.append(float(x))
        y = input("Enter y(Enter to exit): ")
        if y == "":
            break
        ay.append(float(y))
    print(ax)
    print(ay)
    m = calc_m(ax,ay)
    print("m: ", m)
    b = calc_b(ax,ay,m)
    print("The equation is: y = {}*x + {}".format(m,b))


if __name__ == "__main__" :
    main()