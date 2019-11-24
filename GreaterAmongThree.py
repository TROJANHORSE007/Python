x = int(input("enter a number"))
y = int(input("enter a number"))
z = int(input("enter a number"))
if(x>y and x>z):
    print("%d is greater"%x)
elif(y>z and y>x):
    print("%d is greater"%y)
else:
    print("%d is greater"%z)