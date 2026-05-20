import numpy as np
import matplotlib.pyplot as plt

# Signal X1
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Quantification
q = 0.5
X1q = q * np.round(X1 / q)

# Erreur de quantification
E = X1 - X1q

# Affichage sur 3 sous-graphes
fig, axes = plt.subplots(3, 1, figsize=(10, 8))

# Graphe 1 : X1 original
axes[0].plot(T, X1, color='blue', label='X1 original')
axes[0].set_title('Signal original X1')
axes[0].set_ylabel('Amplitude')
axes[0].legend()
axes[0].grid(True)

# Graphe 2 : X1q quantifié
axes[1].plot(T, X1q, color='red', label=f'X1q quantifié (q={q})')
axes[1].set_title('Signal quantifié X1q')
axes[1].set_ylabel('Amplitude')
axes[1].legend()
axes[1].grid(True)

# Graphe 3 : Erreur de quantification
axes[2].plot(T, E, color='green', label='E = X1 - X1q')
axes[2].axhline(y=q/2,  color='gray', linestyle='--', linewidth=1, label=f'+q/2 = +{q/2}')
axes[2].axhline(y=-q/2, color='gray', linestyle='--', linewidth=1, label=f'-q/2 = -{q/2}')
axes[2].set_title('Erreur de quantification E = X1 - X1q')
axes[2].set_ylabel('Erreur')
axes[2].set_xlabel('Temps (s)')
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.show()

# Valeurs caractéristiques de l'erreur
print(f"Erreur maximale  : {E.max():.4f}")
print(f"Erreur minimale  : {E.min():.4f}")
print(f"Erreur moyenne   : {E.mean():.4f}")
print(f"Borne théorique  : ±q/2 = ±{q/2}")