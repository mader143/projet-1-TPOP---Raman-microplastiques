import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import find_peaks

# 1. Chargement des données
base_dir = os.path.dirname(os.path.abspath(__file__))
path1 = os.path.join(base_dir, "ethanol_final.TXT")

pixels_données = []
intensite_données = []

with open(path1, "r") as f:
    next(f)
    for line in f:
        words = line.split(",")
        if len(words) == 3:
            pixels_données.append(float(words[1]))
            intensite_données.append(float(words[2]))

pixels = np.array(pixels_données)
intensite = np.array(intensite_données)

# 2. Conversion en Shift Raman
longueurs = 0.0738 * pixels + 621.88
shift = (1/632.8 - 1/longueurs) * 10**7

# 3. Sélection de la plage de travail
s_range = shift[500:1200]
i_range = intensite[500:1200]

# 4. Redressement
coeffs = np.polyfit(s_range, i_range, 2)
baseline = np.polyval(coeffs, s_range)
intensite_redressee = i_range - baseline
intensite_redressee -= np.min(intensite_redressee)

# 5. Détection des pics
# Ajustez 'height' (hauteur min) et 'distance' (espace min entre pics) selon vos données
peaks, properties = find_peaks(intensite_redressee, height=np.max(intensite_redressee)*0.15, distance=20)
peaks = [160, 256, 278, 395, 510]

# 6. Affichage
plt.figure(figsize=(10, 6))
plt.plot(s_range, intensite_redressee, color='blue', label='Spectre redressé')

# Ajout des étiquettes sur chaque pic trouvé
for p in peaks:
    x_pos = s_range[p]
    y_pos = intensite_redressee[p]
    
    # Label au-dessus du pic avec la valeur du shift
    plt.annotate(f'{x_pos:.1f}', 
                 xy=(x_pos, y_pos), 
                 xytext=(0, 10), 
                 textcoords='offset points', 
                 ha='center', 
                 fontsize=9, 
                 fontweight='bold',
                 color='black',
                 arrowprops=dict(arrowstyle='->', color='black', lw=0.5))

plt.xlabel("Raman shift ($cm^{-1}$)")
plt.ylabel("Intensité [u. arb.]")
plt.grid(True, alpha=0.3)
plt.show()