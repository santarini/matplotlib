import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[3,6,7,4,5,6,9]

plt.scatter(x,y, label="stuff", color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('TIYLE')
plt.legend()
plt.show()
