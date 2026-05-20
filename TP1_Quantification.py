import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(0, 1, 1001)
q = 0.5  # pas de quantification

# Définition des signaux
signaux = {
    'Cosinus F=3Hz, Amp=1'     : np.cos(2 * np.pi * 3 * T),
    'Carré F=2Hz'              : np.sign(np.sin(2 * np.pi * 2 * T)),
    'Sinus redressé F=4Hz'     : np.abs(np.sin(2 * np.pi * 4 * T)),
    'Sinus bruité F=2Hz'       : np.sin(2 * np.pi * 2 * T) + np.random.uniform(-0.3, 0.3, len(T)),
}

fig, axes = plt.subplots(len(signaux), 2, figsize=(14, 12))

for i, (nom, X) in enumerate(signaux.items()):
    Xq = q * np.round(X / q)
    E  = X - Xq

    # Colonne gauche : signal original vs quantifié
    axes[i, 0].plot(T, X,  color='blue', label='Original',       linewidth=1)
    axes[i, 0].plot(T, Xq, color='red',  label=f'Quantifié q={q}', linewidth=1)
    axes[i, 0].set_title(nom)
    axes[i, 0].set_ylabel('Amplitude')
    axes[i, 0].legend(fontsize=8)
    axes[i, 0].grid(True)

    # Colonne droite : erreur
    axes[i, 1].plot(T, E, color='green', label='Erreur E = X - Xq')
    axes[i, 1].axhline(y= q/2, color='gray', linestyle='--', linewidth=1, label=f'+q/2={q/2}')
    axes[i, 1].axhline(y=-q/2, color='gray', linestyle='--', linewidth=1, label=f'-q/2={-q/2}')
    axes[i, 1].set_title(f'Erreur – {nom}')
    axes[i, 1].set_ylabel('Erreur')
    axes[i, 1].legend(fontsize=8)
    axes[i, 1].grid(True)

    print(f"{nom} → erreur max={E.max():.4f} | erreur min={E.min():.4f}")

axes[-1, 0].set_xlabel('Temps (s)')
axes[-1, 1].set_xlabel('Temps (s)')
plt.tight_layout()
plt.show()