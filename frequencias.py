import numpy as np
from math import *




dist = pow(2, 1.0/12)

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