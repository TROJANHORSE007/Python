x = int(input("enter a number "))
y = int(input("enter a number "))
count1 = 0
count2 =0
for i in range(x,y):
    if(i==2):
        count2+=1
    else:
        for j in range(2, i):
            if (i % j == 0):
                count1 += 1
    if (count1 == 0):
        count2 += 1
print("total prime number b/w x & y is  %d  "%count2)


