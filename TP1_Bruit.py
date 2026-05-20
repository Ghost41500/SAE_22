import numpy as np
import matplotlib.pyplot as plt
import random

# Signal X1
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Génération du bruit 
bruit_faible  = np.array([random.uniform(-0.1, 0.1) for _ in T])
bruit_moyen   = np.array([random.uniform(-0.5, 0.5) for _ in T])
bruit_fort    = np.array([random.uniform(-1.0, 1.0) for _ in T])

X1_bruit_faible = X1 + bruit_faible
X1_bruit_moyen  = X1 + bruit_moyen
X1_bruit_fort   = X1 + bruit_fort

# Affichage
fig, axes = plt.subplots(3, 1, figsize=(10, 8))

axes[0].plot(T, X1, color='red', label='X1 original', linewidth=1)
axes[0].plot(T, X1_bruit_faible, color='blue', label='Bruit faible (±0.1)', linewidth=0.8)
axes[0].set_title('Bruit faible')
axes[0].legend()
axes[0].grid(True)

axes[1].plot(T, X1, color='red', label='X1 original', linewidth=1)
axes[1].plot(T, X1_bruit_moyen, color='blue', label='Bruit moyen (±0.5)', linewidth=0.8)
axes[1].set_title('Bruit moyen')
axes[1].legend()
axes[1].grid(True)

axes[2].plot(T, X1, color='red', label='X1 original', linewidth=1)
axes[2].plot(T, X1_bruit_fort, color='blue', label='Bruit fort (±1.0)', linewidth=0.8)
axes[2].set_title('Bruit fort')
axes[2].legend()
axes[2].grid(True)

plt.xlabel('Temps (s)')
plt.tight_layout()
plt.show()