import numpy as np
import matplotlib.pyplot as plt
import os
import csv

i = []
shift = []

with open('polystyrene_data.csv', mode='r', encoding='utf-8') as fichier:
    for ligne in fichier:
        data = ligne.split(',')
        shift.append(data[0])
        i.append(data[1])

plt.plot(shift, i)
plt.xlabel('Raman shift')
plt.ylabel('Intensité')
plt.show()
