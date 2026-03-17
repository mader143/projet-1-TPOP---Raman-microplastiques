import numpy as np
import matplotlib.pyplot as plt
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
path1 = os.path.join(base_dir, "ethanol_1goutte2.TXT")
path2 = os.path.join(base_dir, "ethanol_3goutte.TXT")
path3 = os.path.join(base_dir, "ethanol_5goutte.TXT")

#C2
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

#C4

file2 = open(path2, "r")
line2 = file2.readline()
pixels_données2 = []
intensite_données2 = []

i = 0
for line2 in file2:
    i += 1
    if i > 0:
        words = line2.split(",")
        if len(words) == 3:
            pixels_données2.append(float(words[1]))
            intensite_données2.append(float(words[2].replace('\n', '')))

pixels2 = np.array(pixels_données2)
intensite2 = np.array(intensite_données2)

#C3

file3 = open(path3, "r")
line3 = file3.readline()
pixels_données3 = []
intensite_données3 = []

i = 0
for line3 in file3:
    i += 1
    if i > 0:
        words = line3.split(",")
        if len(words) == 3:
            pixels_données3.append(float(words[1]))
            intensite_données3.append(float(words[2].replace('\n', '')))

pixels3 = np.array(pixels_données3)
intensite3 = np.array(intensite_données3)

longueurs3 = 0.0738*pixels3 + 621.88
shift3 = (1/632.8 - 1/longueurs3)*10**7
longueurs2 = 0.0738*pixels2 + 621.88
shift2 = (1/632.8 - 1/longueurs2)*10**7
longueurs = 0.0738*pixels + 621.88
shift = (1/632.8 - 1/longueurs)*10**7

#ajout de code pour normalisation?

plt.figure()
plt.gca().invert_xaxis()
plt.plot((shift3[670:690]), (intensite3[670:690]), label='C3')
plt.plot((shift2[670:690]), (intensite2[670:690]), label='C4')
plt.plot((shift[670:690]), (intensite[670:690]), label='C2')
plt.legend()
plt.xlabel('Raman shift [$cm^{-1}$]')
plt.ylabel('Intensité [u. ar.]')
plt.show()