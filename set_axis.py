import numpy as np
import matplotlib.pyplot as plt

def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi * t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)

# make plot
plt.plot(t,y)

# setting axis, min sama max
# ket: axis([Xmin, Xmax, Ymin, Ymax])
plt.axis([0,4,-1,1]) # kamu bisa menggunkan ini untuk menempelkan ke dinding atau tidak

# menampilkan
plt.show()