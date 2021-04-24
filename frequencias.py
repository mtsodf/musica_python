import numpy as np
from math import *


dist = pow(2, 1.0/12)


esc_maior = [2, 1, 2, 2, 2, 1]
esc_acum_maior = [2, 0, 0, 0, 0, 0, 0]



notas = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


freq = np.zeros(len(notas))


pos = {}
for i,nota in enumerate(notas):
	pos[nota] = i

print pos

freq[pos["A"]] = 440.0

for i in range(len(freq)):
	pA = pos["A"]
	freq[i] = freq[pA] * pow(dist, i - pA)

print freq

t = np.arange(0, 0.1, .5/4400)



import matplotlib.pyplot as plt

C = freq[pos["C"]]
E = freq[pos["E"]]
G = freq[pos["G"]]
B = freq[pos["A#"]]

sp = np.fft.fft(np.sin(2*pi*C*t) + np.sin(2*pi*E*t) + np.sin(2*pi*G*t) + np.sin(2*pi*B*t))
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, sp.real)

#plt.plot(t, np.sin(2*pi*C*t) + np.sin(2*pi*E*t) + np.sin(2*pi*G*t) + np.sin(2*pi*B*t))

plt.show()