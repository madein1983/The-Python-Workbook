import sys
stringIn = input('Enter fifteen characters: ')
if len(stringIn) < 15 :
 print ("Ошибка! Введите пятнадцать или более символов")
else :
 #print ('good seaman')   
# вывести два последних символа этой строки 
 xout = stringIn[-3:]
 print("Два предпоследних символа введенной Вами строки: " + xout[:2])
# вывести 5й символ этой строки
 yout = stringIn[4]
 print ("Пятый символ ввведенной Вами строки: " + yout)
# вывод второй половины строки
 halfOfstringIn  = round (len(stringIn)/2)
 zout = stringIn[halfOfstringIn:] 
 print("Половина введенной Вами строки: " + zout)
# вся строка кроме последних трех символов
 print ("Вся строка кроме последних трех символов: "+ stringIn[:-3])