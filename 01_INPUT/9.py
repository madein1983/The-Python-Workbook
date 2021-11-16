## Сложные проценты
#
percent = 0.04
deposit = float(input("Введите сумму депозита: "))
annual_sum1y = deposit + deposit*percent
annual_sum2y = annual_sum1y + annual_sum1y * percent
annual_sum3y = annual_sum2y + annual_sum2y * percent
print("Сумма после 1-го года депозита" , annual_sum1y)
print("Сумма после 2-го года депозита" , annual_sum2y)
print("Сумма после 3-го года депозита" , annual_sum3y)
