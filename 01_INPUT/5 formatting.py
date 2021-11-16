## 8/13/2021 9:45pm
lower_1_litr_cost = 0.1
greater_1_litr_cost = 0.25
count_1less_litr = int(input("Введите количество бутылок объемом один или меньше литра: "))
count_1greater_litr = int(input("Введите количество бутылок объемом один или более литра: "))
sum_to_earn = (lower_1_litr_cost*count_1less_litr) + (greater_1_litr_cost*count_1greater_litr)
print ("$", "%.2f"  % sum_to_earn)