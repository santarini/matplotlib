import matplotlib.pyplot as plt

data_set = [3,45,67,89,29,30,54,78,34,21,56,89,65,43,78,5,38,29,16,83,94,38,68,73,92,43,25,36,84,87,73,61,11]

bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(data_set, bins, histtype='bar', rwidth=0.8, cumulative=True)

plt.xlabel('x')
plt.ylabel('y')
plt.title('TIYLE')
plt.legend()
plt.show()
