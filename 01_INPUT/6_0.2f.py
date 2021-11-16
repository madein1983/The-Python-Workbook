## 8/13/20210 9:53
# taxes
sum = float(input("Please enter the pay sum: "))
tax_rate = 0.2
chay_rate = 0.20
tax = sum*tax_rate
chay = (sum-tax)*chay_rate

print ("Налог от суммы платежа: ", "%.2f" %tax)
print ("Размер чаевых:  ", "%.2f" %chay)
out = tax + chay
doxod = sum - out
print ("Чистая прибыль: ", "%.2f" %doxod)



##FROM BOOK##
TAX_RATE = 0.05
TIP_RATE = 0.18
cost = float(input("Введите сумму счета: "))
taxb = cost * TAX_RATE
tip = cost * TIP_RATE
total = cost + taxb + tip
# отобразим результат
print ("Налог составит - %.2f, чаевые - %.2f общая сумма заказа: %.2f" % (taxb, tip,total))



