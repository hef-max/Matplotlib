import numpy as np
import matplotlib.pyplot as plt

#urutan
 # 1. memebuat data
 # 2. membuat plot
 # 3. menampilkan plot

# dataset
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])
y2 = np.array([36,49,64,81,100])

# abstraksi
plt.plot(x,y)
plt.plot(y,y2)


# menampilkan
plt.show()
