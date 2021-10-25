from random import randint
def curr_password():
  
        pass_length = randint(7,10)
        i = 0
        password = ""
        for i in range(pass_length-1):
            curr_ord = randint(48,126)
            password = password + chr(curr_ord)
        # print(password)
        return password

def main():
    
    curr_password()

if __name__ == "__main__":
    main()