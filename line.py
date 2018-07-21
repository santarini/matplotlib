import matplotlib.pyplot as plt

x = [1,2,3]
y = [4,3,7]

x2 = [1, 2, 3]
y2 = [12, 15, 12]

plt.plot(x,y, label='First Line')
plt.plot(x2,y2, label='Second Line')

plt.xlabel('Ballin so hard')
plt.ylabel('Mofos wanna find me')
plt.title('TIYLE')
plt.legend()

plt.show()
