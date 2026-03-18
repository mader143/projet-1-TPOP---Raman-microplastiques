import numpy as np
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path1 = os.path.join(base_dir, "eau_lait_c2.TXT")

file1 = open(path1, "r")
line1 = file1.readline()

pixels_données = []
intensite_données = []

i = 0
for line1 in file1:
    i += 1
    if i > 0:
        words = line1.split(",")
        if len(words) == 3:
            pixels_données.append(float(words[1]))
            intensite_données.append(float(words[2].replace('\n', '')))

pixels = np.array(pixels_données)
intensite = np.array(intensite_données)

longueurs = 0.0738*pixels + 621.88
shift = (1/632.8 - 1/longueurs)*10**7

plt.figure()
plt.gca().invert_xaxis()
plt.plot((shift[675:682]), (intensite[675:682]), label='Eau et lait')
plt.legend()
plt.xlabel('Raman shift [$cm^{-1}$]')
plt.ylabel('Intensité [u. ar.]')
plt.show()