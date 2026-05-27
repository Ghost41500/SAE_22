
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import resample
from scipy.signal import spectrogram
from IPython.display import Audio 


# ============================================================
# 1) Transformation du fichier wav en valeurs exploitables en python
# ============================================================

# === Paramètres ===
fichier_entree = "SAE_Projet/Fichier_Audio_SAE22_Projet.wav" # à déposer dans le même dossier

# === Lecture du fichier .wav ===
Fe_in, x = wavfile.read(fichier_entree)
print("Fréquence d'échantillonnage d'origine :", Fe_in, "Hz")
print("Type de données :", x.dtype)

# === Conversion en float32 dans [-1, 1] ===
if x.dtype == np.int16:
    x = x.astype(np.float32) / 32768.0
elif x.dtype == np.int32:
    x = x.astype(np.float32) / 2147483648.0
elif x.dtype == np.float32:
    x = x.astype(np.float32)
else:
    raise ValueError("Format audio non géré")

# === Si stéréo → on passe en mono (moyenne des canaux) ===
if x.ndim == 2:
    x = x.mean(axis=1)

print("Signal mono, normalisé dans [-1, 1], longueur :", len(x))



# ============================================================
# 3) RÉ-ÉCHANTILLONNAGE À PLUSIEURS FE
# ============================================================

Fe_list = [4000, 6000, 8000, 10000]

for Fe_out in Fe_list:
    x_res = resample_signal(x, Fe_ref, Fe_out)
    fichier_sortie = f"voix_resample_{Fe_out}Hz.wav"
    x_int16 = np.int16(np.clip(x_res, -1, 1) * 32767)
    wavfile.write(fichier_sortie, Fe_out, x_int16)
    print(f"Fichier écrit : {fichier_sortie}")

# Exemple d'écoute dans Jupyter :
Audio("voix_resample_8000Hz.wav")



# ============================================================
# 4) QUANTIFICATION UNIFORME
# ============================================================

def quantification_uniforme(x, Nbits):
    x_sat = np.clip(x, -1, 1 - 2**(-Nbits))
    Q = 2 / (2**Nbits)
    indices = np.floor((x_sat + 1) / Q)
    x_q = indices * Q - 1 + Q/2
    return x_q