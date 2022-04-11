import matplotlib.pyplot as plt
import numpy as np


# membuat data
sudut = np.arange(0, 360, 1)
y = np.sin(np.deg2rad(sudut))

plt.plot(sudut,y)
plt.ylabel("magnitudo")
plt.xlabel("sudut")

plt.yticks([-1,0,1])
plt.xticks([0, 180, 360], [r'${0}^o$', r'${180}^o$', r'${360}^o$'])
plt.show()