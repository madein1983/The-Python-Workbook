x = float(input("Enter x: "))
guess = x / 2
eps = pow(10,-12)
i = 0

while guess-new_guess  > eps :
    new_guess = 0.5*(guess+(x/2))
    guess = (guess + x/guess)/2