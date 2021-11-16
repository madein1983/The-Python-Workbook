str_arr = []
line_in = str(input("Введите слова(пустой ввод для выхода: "))
str_arr.append(line_in)
while line_in != "" :
    if line_in not in str_arr :
        str_arr.append(line_in)
    line_in = str(input("Введите слова(пустой ввод для выхода: "))
print(str_arr)
for i in str_arr :
    print(i)