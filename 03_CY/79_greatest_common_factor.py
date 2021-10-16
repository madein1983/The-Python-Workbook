
x = int(input("Enter 1 number: "))
y = int(input("Enter 2 number: "))

if x > y :
    grtst_cmn_fctr = y
else :
    grtst_cmn_fctr = x

while (x % grtst_cmn_fctr) != 0 or (y % grtst_cmn_fctr) != 0 :
      grtst_cmn_fctr -= 1
print(grtst_cmn_fctr)
