import matplotlib.pylab as plt
import numpy as np
import math

csv_path = 'data/archive.csv'
my_data = np.genfromtxt(csv_path, delimiter=',')

data = [0] * 50


for i in my_data:
    for j in i:
        if math.isnan(j) is False:
            data[int(j)] += 1

for i, k in enumerate(data):
    print str(i) + ': ' + str(k)

plt.bar(range(50), data, 1)
plt.show()