import p107_imported_79
x = float(input("Enter numerator: "))
y = float(input("Enter denominator: "))

z = p107_imported_79.max_common_denominator(x,y)
new_x = x/z
new_y = y/z
print("Greatest common factor is:", z, "The new numerator is: ", new_x,"the new denominator is: ",new_y)
