import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Configuration des chemins
base_dir = os.path.dirname(os.path.abspath(__file__))
paths = [
    os.path.join(base_dir, "ethanol_1goutte2.TXT"),
    os.path.join(base_dir, "ethanol_3goutte.TXT"),
    os.path.join(base_dir, "ethanol_5goutte.TXT")
]

def load_data(path):
    pixels, intensite = [], []
    if not os.path.exists(path):
        print(f"Fichier introuvable : {path}")
        return np.array([]), np.array([])
    with open(path, "r") as f:
        next(f)  # Sauter l'en-tête
        for line in f:
            words = line.split(",")
            if len(words) == 3:
                pixels.append(float(words[1]))
                intensite.append(float(words[2]))
    return np.array(pixels), np.array(intensite)

# 2. Chargement des données brutes
px1, int1 = load_data(paths[0])
px2, int2 = load_data(paths[1])
px3, int3 = load_data(paths[2])

# 3. Calcul du Shift Raman
def get_shift(px):
    if px.size == 0: return px
    longueurs = 0.0738 * px + 621.88
    return (1/632.8 - 1/longueurs) * 10**7

shift1, shift2, shift3 = get_shift(px1), get_shift(px2), get_shift(px3)

# 4. Sélection de la plage de visualisation [1200:1300]
start, end = 1200, 1300

# Extraction des segments pour le calcul du min/max
seg1 = int1[start:end]
seg2 = int2[start:end]
seg3 = int3[start:end]

# 5. NORMALISATION GLOBALE (basée sur la zone affichée)
# On fusionne les trois segments pour trouver les bornes 0 et 1 de la zone
tous_segments = np.concatenate([seg1, seg2, seg3])
global_min = np.min(tous_segments)
global_max = np.max(tous_segments)

# Application de la normalisation 0-1 sur les segments
int1_norm = (seg1 - global_min) / (global_max - global_min)
int2_norm = (seg2 - global_min) / (global_max - global_min)
int3_norm = (seg3 - global_min) / (global_max - global_min)

# 6. Affichage
plt.figure(figsize=(10, 6))

plt.plot(shift3[start:end], int3_norm, label='5 gouttes de lait', color='cornflowerblue', linewidth=2.5)
plt.plot(shift2[start:end], int2_norm, label='3 gouttes de lait', color='violet', linewidth=2.5)
plt.plot(shift1[start:end], int1_norm, label='1 goutte de lait', color='lightcoral', linewidth=2.5)

# Configuration des axes
plt.ylim(-0.02, 1.02) # Pour bien voir le 0 et le 1
plt.legend()
plt.xlabel('Raman shift [$cm^{-1}$]')
plt.ylabel('Intensité normalisée [u. arb.]')
plt.grid(True, alpha=0.3)

plt.show()