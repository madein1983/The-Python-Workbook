a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
mn = min(a,b,c)
mx = max(a,b,c)
md = a+b+c-mn-mx
print(mn,md,mx)