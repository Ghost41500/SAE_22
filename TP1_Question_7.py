import numpy as np
import matplotlib.pyplot as plt

# Base de temps
T = np.linspace(0, 1, 1001)
F = 2

# Différents types de signaux
X_cos    = np.cos(2 * np.pi * F * T)              
X_abs    = np.abs(np.sin(2 * np.pi * F * T))        
X_carre  = np.sign(np.sin(2 * np.pi * F * T))        
X_dent   = 2 * (T * F - np.floor(T * F + 0.5))      

# Affichage
fig, axes = plt.subplots(4, 1, figsize=(10, 10))

axes[0].plot(T, X_cos, color='blue', label='Cosinus – cos(2π×2×t)')
axes[0].set_title('Signal Cosinus')
axes[0].legend()
axes[0].grid(True)
axes[0].set_ylabel('Amplitude')

axes[1].plot(T, X_abs, color='red', label='Sinus redressé – |sin(2π×2×t)|')
axes[1].set_title('Signal Sinus redressé (abs)')
axes[1].legend()
axes[1].grid(True)
axes[1].set_ylabel('Amplitude')

axes[2].plot(T, X_carre, color='green', label='Signal carré – sign(sin(2π×2×t))')
axes[2].set_title('Signal Carré')
axes[2].legend()
axes[2].grid(True)
axes[2].set_ylabel('Amplitude')

axes[3].plot(T, X_dent, color='purple', label='Dent de scie')
axes[3].set_title('Signal Dent de scie')
axes[3].legend()
axes[3].grid(True)
axes[3].set_ylabel('Amplitude')

plt.xlabel('Temps (s)')
plt.tight_layout()
plt.show()