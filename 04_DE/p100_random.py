from random import randint
def password():
    pass_length = randint(7,10)
    i = 0
    password = ""
    for i in range(pass_length-1):
        curr_ord = randint(33,126)
        password = password + chr(curr_ord)
    print(password)

def main():
    password()

if __name__ == "__main__":
    main()