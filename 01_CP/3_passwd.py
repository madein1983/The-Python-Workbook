import sys 
import getpass
logins = []
passwords = []
while True :
 loginIn = input("Введите Ваш логин от пяти до десяти символов: ") 
 if (len(loginIn) < 5 or len(loginIn) > 10) :
    logins.append(loginIn)
    print("Не правильный ввод. Ваш логин должен быть не менее пяти, но не более десяти символов. Повторите ввод:")  
 else :
    print("Ваш логин: " + loginIn)
    logins.append(loginIn)
    print("List logins") 
    print(logins)
    while True :
       passwordIn = getpass.getpass('Password:')
       #passwordIn = input(pswd)
       if (len(passwordIn) < 8 ) :
           passwords.append(passwordIn)
           print ("Длина пароля не должна быть менее восьми символов. Повторите ввод:")
       else :
           print ("Ваш пароль: " + passwordIn)
           passwords.append(passwordIn)
           print("List passwords") 
           print(passwords)
           exit()


  
