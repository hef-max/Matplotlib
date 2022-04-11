import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [6,7,8,9,10]

plt.figure(1)
plt.plot(x,y)

# contoh2

PI = np.pi
sudut = np.linspace(0, 2*PI, 100)
radius = 5

x1 = radius * np.cos(sudut)
y1 = radius * np.sin(sudut)

plt.figure(2)
plt.plot(x1,y1)

plt.show()