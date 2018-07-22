import matplotlib.pyplot as plt

days=[1,2,3,4,5,6,7]

sleep=[9,7,9,7,9,7,9]
eat=[3,3,3,3,3,3,3]
study=[2,4,2,4,2,4,2]
exercise=[0,1,1,1,1,1,0]
working=[0,8,8,8,8,8,0]
travel=[1,1,1,1,1,1,1]
other=[9,0,0,0,0,0,9]


plt.plot([],[], color="red", label="sleep")
plt.plot([],[], color="blue", label="eat")
plt.plot([],[], color="green", label="study")
plt.plot([],[], color="orange", label="exercise")
plt.plot([],[], color="purple", label="working")
plt.plot([],[], color="brown", label="travel")
plt.plot([],[], color="black", label="other")

plt.stackplot(days, eat, sleep, study, exercise, working, travel, other, colors=['red','blue','green','orange','purple','brown','black'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('TIYLE')
plt.legend()
plt.show()
