import matplotlib.pylab as plt
import numpy as np
import math

csv_path = 'data/archive.csv'
my_data = np.genfromtxt(csv_path, delimiter=',')

data = [0] * 50

print my_data.shape
for i in my_data[-150:, :]:
    for j in i:
        if math.isnan(j) is False:
            if data[int(j)] is None:
                data[int(j)] = 1
            else:
                data[int(j)] += 1

for i, k in enumerate(data):
    print str(i) + ': ' + str(k)

print sum(data)

plt.bar(range(50), data, 1)
plt.show()