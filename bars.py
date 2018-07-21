import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [3,7,2,8,9]

x2 = [1,3,5,7,9]
y2 = [4,9,2,5,6]

plt.bar(x,y, label="bars1", color="blue")
plt.bar(x2,y2, label="bars2", color="orange")

plt.xlabel('x')
plt.ylabel('y')
plt.title('TITLE')
plt.legend()
plt.show()
