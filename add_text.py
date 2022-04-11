import numpy as np
import matplotlib.pyplot as plt


def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi * t + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)

plt.plot(t1,y1)

#ket: plt.text(x,y, 'text')
plt.text(2,1, 'sin(0)')
plt.text(2,0.5, r'$ y = \mathcal{A} .sin(2 \omega t)$')
plt.text(2,0.4, r'$ \mathcal{A} = 1 cm, \omega = 1Hz$')

plt.show()