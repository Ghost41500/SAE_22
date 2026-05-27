import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import resample, spectrogram

# ============================================================
# CONFIGURATION - Modifier le nom du fichier ici
# ============================================================

FICHIER_ENTREE = "SAE_Projet/Fichier_Audio_SAE22_Projet.wav" # ton fichier audio
DOSSIER_SORTIE = "SAE_Projet/"  # dossier où seront sauvegardés les fichiers générés

import os
os.makedirs(DOSSIER_SORTIE, exist_ok=True)

# ============================================================
# PARTIE 1 : Lecture et normalisation du fichier WAV
# ============================================================

Fe_in, x = wavfile.read(FICHIER_ENTREE)
print("=" * 50)
print("PARTIE 1 - Lecture du fichier audio")
print("=" * 50)
print(f"Fréquence d'échantillonnage d'origine : {Fe_in} Hz")
print(f"Type de données : {x.dtype}")

# Conversion en float32 dans [-1, 1]
if x.dtype == np.int16:
    x = x.astype(np.float32) / 32768.0
elif x.dtype == np.int32:
    x = x.astype(np.float32) / 2147483648.0
elif x.dtype == np.float32:
    x = x.astype(np.float32)
else:
    raise ValueError("Format audio non géré")

# Si stéréo → mono
if x.ndim == 2:
    x = x.mean(axis=1)

duree = len(x) / Fe_in
print(f"Signal mono, normalisé dans [-1, 1]")
print(f"Longueur : {len(x)} échantillons ({duree:.2f} secondes)")

# Affichage du signal original
plt.figure(figsize=(12, 3))
t = np.linspace(0, duree, len(x))
plt.plot(t, x, color='steelblue', linewidth=0.5)
plt.title("Signal audio original")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.savefig(DOSSIER_SORTIE + "signal_original.png", dpi=150)
plt.show()
print("→ Graphe sauvegardé : signal_original.png\n")


# ============================================================
# PARTIE 2 : Fonction de ré-échantillonnage
# ============================================================

Fe_ref = Fe_in  # fréquence de référence

def resample_signal(x, Fe_in, Fe_out):
    """Ré-échantillonne le signal x de Fe_in vers Fe_out."""
    nb_samples = int(len(x) * Fe_out / Fe_in)
    return resample(x, nb_samples)


# ============================================================
# PARTIE 3 : Expérimentations d'échantillonnage (Phase 2 projet)
# ============================================================

print("=" * 50)
print("PARTIE 3 - Ré-échantillonnage à différentes Fe")
print("=" * 50)

Fe_list = [4000, 8000, 44100]

fig, axes = plt.subplots(len(Fe_list), 1, figsize=(12, 2.5 * len(Fe_list)))

for i, Fe_out in enumerate(Fe_list):
    x_res = resample_signal(x, Fe_ref, Fe_out)

    # Sauvegarde du fichier WAV
    fichier_sortie = DOSSIER_SORTIE + f"voix_resample_{Fe_out}Hz.wav"
    x_int16 = np.int16(np.clip(x_res, -1, 1) * 32767)
    wavfile.write(fichier_sortie, Fe_out, x_int16)

    # Débit binaire pour ce ré-échantillonnage (16 bits, mono)
    debit = Fe_out * 16
    print(f"Fe = {Fe_out} Hz → fichier : {fichier_sortie} | Débit : {debit} bit/s ({debit/1000:.1f} kbit/s)")

    # Affichage du signal
    t_res = np.linspace(0, duree, len(x_res))
    axes[i].plot(t_res, x_res, linewidth=0.5, color='darkorange')
    axes[i].set_title(f"Fe = {Fe_out} Hz — Débit = {debit/1000:.0f} kbit/s")
    axes[i].set_ylabel("Amplitude")
    axes[i].set_xlabel("Temps (s)")

plt.tight_layout()
plt.savefig(DOSSIER_SORTIE + "comparaison_echantillonnage.png", dpi=150)
plt.show()
print("→ Graphe sauvegardé : comparaison_echantillonnage.png\n")


# ============================================================
# PARTIE 3b : Spectres pour chaque fréquence d'échantillonnage
# ============================================================

print("Génération des spectres...")
fig, axes = plt.subplots(len(Fe_list), 1, figsize=(12, 2.5 * len(Fe_list)))

for i, Fe_out in enumerate(Fe_list):
    x_res = resample_signal(x, Fe_ref, Fe_out)
    f, t_spec, Sxx = spectrogram(x_res, fs=Fe_out, nperseg=256)
    axes[i].pcolormesh(t_spec, f, 10 * np.log10(Sxx + 1e-10), shading='gouraud', cmap='inferno')
    axes[i].set_title(f"Spectre — Fe = {Fe_out} Hz")
    axes[i].set_ylabel("Fréquence (Hz)")
    axes[i].set_xlabel("Temps (s)")

plt.tight_layout()
plt.savefig(DOSSIER_SORTIE + "spectres_echantillonnage.png", dpi=150)
plt.show()
print("→ Graphe sauvegardé : spectres_echantillonnage.png\n")


# ============================================================
# PARTIE 4 : Quantification uniforme (Phase 3 projet)
# ============================================================

def quantification_uniforme(x, Nbits):
    """Quantifie le signal x sur Nbits bits."""
    x_sat = np.clip(x, -1, 1 - 2**(-Nbits))
    Q = 2 / (2**Nbits)
    indices = np.floor((x_sat + 1) / Q)
    x_q = indices * Q - 1 + Q / 2
    return x_q

print("=" * 50)
print("PARTIE 4 - Quantification sur différents nombres de bits")
print("=" * 50)

# On fixe une Fe pour les expériences de quantification
Fe_quant = 8000
x_8k = resample_signal(x, Fe_ref, Fe_quant)

Nbits_list = [2, 4, 8, 16]

fig, axes = plt.subplots(len(Nbits_list), 2, figsize=(14, 3 * len(Nbits_list)))

for i, Nbits in enumerate(Nbits_list):
    x_q = quantification_uniforme(x_8k, Nbits)
    erreur = x_8k - x_q
    bruit_rms = np.sqrt(np.mean(erreur**2))
    signal_rms = np.sqrt(np.mean(x_8k**2))
    snr = 20 * np.log10(signal_rms / (bruit_rms + 1e-10))

    # Sauvegarde WAV quantifié
    fichier_q = DOSSIER_SORTIE + f"voix_quant_{Nbits}bits.wav"
    x_int16 = np.int16(np.clip(x_q, -1, 1) * 32767)
    wavfile.write(fichier_q, Fe_quant, x_int16)

    debit = Fe_quant * Nbits
    print(f"N = {Nbits} bits → {2**Nbits} niveaux | Débit : {debit/1000:.1f} kbit/s | SNR ≈ {snr:.1f} dB | {fichier_q}")

    t_q = np.linspace(0, len(x_8k)/Fe_quant, len(x_8k))

    # Signal quantifié
    axes[i, 0].plot(t_q[:500], x_8k[:500], label="Original", linewidth=1, color='steelblue')
    axes[i, 0].plot(t_q[:500], x_q[:500], label=f"Quantifié {Nbits} bits", linewidth=1, color='tomato', linestyle='--')
    axes[i, 0].set_title(f"Signal quantifié — {Nbits} bits ({2**Nbits} niveaux)")
    axes[i, 0].legend(fontsize=8)
    axes[i, 0].set_ylabel("Amplitude")

    # Erreur de quantification
    axes[i, 1].plot(t_q[:500], erreur[:500], color='green', linewidth=0.8)
    axes[i, 1].set_title(f"Erreur de quantification — {Nbits} bits | SNR = {snr:.1f} dB")
    axes[i, 1].set_ylabel("Erreur")

plt.tight_layout()
plt.savefig(DOSSIER_SORTIE + "comparaison_quantification.png", dpi=150)
plt.show()
print("→ Graphe sauvegardé : comparaison_quantification.png\n")


# ============================================================
# PARTIE 5 : Contraintes réseau — débit ≤ 64 kbit/s (Phase 4 projet)
# ============================================================

print("=" * 50)
print("PARTIE 5 - Analyse des débits (contrainte 64 kbit/s)")
print("=" * 50)
print(f"{'Fe (Hz)':<12} {'Bits':<8} {'Débit (kbit/s)':<18} {'OK ≤ 64 kbit/s'}")
print("-" * 55)

Fe_test    = [4000,8000,44100]
Nbits_test = [2, 4, 8, 16]

meilleurs = []
for Fe in Fe_test:
    for Nb in Nbits_test:
        debit_kb = (Fe * Nb) / 1000
        ok = "✓" if debit_kb <= 64 else "✗"
        print(f"{Fe:<12} {Nb:<8} {debit_kb:<18.1f} {ok}")
        if debit_kb <= 64:
            meilleurs.append((Fe, Nb, debit_kb))

print()
print("→ Meilleurs couples qualité/débit dans la contrainte 64 kbit/s :")
# On trie par débit décroissant pour trouver le meilleur
meilleurs.sort(key=lambda x: x[2], reverse=True)
for Fe, Nb, d in meilleurs[:3]:
    print(f"   Fe = {Fe} Hz, {Nb} bits → {d:.1f} kbit/s")

print()
print("=" * 50)
print("RECOMMANDATION WAVESTREAM")
print("=" * 50)
print("→ Pour la VOIX      : Fe = 8000 Hz, 8 bits → 64 kbit/s (standard téléphonie)")
print("→ Pour la MUSIQUE   : Fe = 16000 Hz, 4 bits → 64 kbit/s (compromis acceptable)")
print("=" * 50)
print("\nTous les fichiers WAV et graphes ont été générés avec succès !")
