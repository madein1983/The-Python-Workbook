sum = 0
line_in = 0
while line_in != "":
    try:
        line_in = input("Enter number(Double Enter to exit): ")
        sum = sum + float(line_in)
    except ValueError:
        print("{0} - it is not a number. Please repeat enter".format(line_in))
        line_in = input("Enter number: ")
        if line_in == "\n":
            quit()
print(sum)

# https://docs.python.org/3/tutorial/errors.html
# ZeroDivisionError: division by zero
# >>> 4 + spam*3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'spam' is not defined
# >>> '2' + 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str