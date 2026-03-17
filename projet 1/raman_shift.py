import numpy as np
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path1 = os.path.join(base_dir, "essai_10min_C2.TXT")
path2 = os.path.join(base_dir, "essai_10min_C4.TXT")
path3 = os.path.join(base_dir, "essai_10min_C3_essai2.TXT")
path4 = os.path.join(base_dir, "ethanol_final.TXT")
path5 = os.path.join(base_dir, "mercure_prise2.TXT")

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

# #premier pic
# print('premier pic')
# print(np.where(intensite == max(intensite[600:800]))[0])
# print(max(intensite[600:800]))
# #deuxieme pic
# print('deuxieme pic')
# print(np.where(intensite == max(intensite[800:1000]))[0])
# print(max(intensite[800:1000]))
# #troisieme pic
# print('troisieme pic')
# print(np.where(intensite == max(intensite[1166:1175]))[0])
# print(max(intensite[1166:1175]))
# #quatrieme pic
# print('quatrieme pic')
# print(np.where(intensite == max(intensite[1175:1193]))[0])
# print(max(intensite[1175:1193]))

#ethanol
file4 = open(path4, "r")
line4 = file4.readline()
pixels_données4 = []
intensite_données4 = []

i = 0
for line4 in file4:
    i += 1
    if i > 0:
        words = line4.split(",")
        if len(words) == 3:
            pixels_données4.append(float(words[1]))
            intensite_données4.append(float(words[2].replace('\n', '')))

pixels4 = np.array(pixels_données4)
intensite4 = np.array(intensite_données4)

longueurs4 = 0.0738*pixels4 + 621.88
shift4 = (1/632.8 - 1/longueurs4)*10**7
longueurs3 = 0.0738*pixels3 + 621.88
shift3 = (1/632.8 - 1/longueurs3)*10**7
longueurs2 = 0.0738*pixels2 + 621.88
shift2 = (1/632.8 - 1/longueurs2)*10**7
longueurs = 0.0738*pixels + 621.88
shift = (1/632.8 - 1/longueurs)*10**7


plt.figure()
plt.gca().invert_xaxis()
plt.plot((shift3[670:690]), (intensite3[670:690]), label='C3')
plt.plot((shift2[670:690]), (intensite2[670:690]), label='C4')
plt.plot((shift[670:690]), (intensite[670:690]), label='C2')
plt.legend()
plt.xlabel('Raman shift [$cm^{-1}$]')
plt.ylabel('Intensité [u. ar.]')
plt.show()

plt.figure()
plt.gca().invert_xaxis()
plt.plot((shift4[500:1300]), (intensite4[500:1300]), label='C3')
plt.legend()
plt.xlabel('Raman shift [$cm^{-1}$]')
plt.ylabel('Intensité [u. ar.]')
plt.show()

#mercure 2
file5 = open(path5, "r")
line5 = file5.readline()
pixels_données5 = []
intensite_données5 = []

i = 0
for line5 in file5:
    i += 1
    if i > 0:
        words = line5.split(",")
        if len(words) == 3:
            pixels_données5.append(float(words[1]))
            intensite_données5.append(float(words[2].replace('\n', '')))

pixels5 = np.array(pixels_données5)
intensite5 = np.array(intensite_données5)

plt.figure()
plt.plot((pixels5), (intensite5), label='C3')
plt.legend()
plt.xlabel('Raman shift [$cm^{-1}$]')
plt.ylabel('Intensité [u. ar.]')
plt.show()