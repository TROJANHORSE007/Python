import matplotlib.pyplot as plt
a = [4,6,45,1,5,5,6,3,8,7,4]
b = [4,6,7,8,6,3,2,1,45,4,6]
plt.xlabel("time")
plt.ylabel("Distace")
plt.plot(a,b,'*', color='red')
plt.show()