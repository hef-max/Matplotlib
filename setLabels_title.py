import matplotlib.pyplot as plt
import numpy as np

def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi * t + np.deg2rad(theta))
    return t,y

amplitudo = 1
frekuensi = 1
tAkhir = 4
theta = 0

t,y = sinusGenerator(amplitudo, frekuensi, tAkhir, theta)


# cara mengeluarkan simbol" math

judul = 'Grafik Sinusoidal\n'
rumus = r'$ \mathcal{y} = A.sin(2 \omega t + \theta)$' + '\n'
parameter = r'A = ' + str(amplitudo) + ' cm, '
parameter2 = r'$ \omega = $' + str(frekuensi) + r'$ \mathit{Hz} $' + ', '
parameter3 = r'$ \theta = $' + str(theta) + r'$^0$'


# membuat plot
plt.plot(t,y)
# membuat labels [HARUS DIBAWA plt.plot()]
plt.title(judul + rumus + parameter + parameter2 + parameter3)

plt.xlabel('waktu(s)')
plt.ylabel('amplitudo(cm)')

# menampilkan
plt.show()