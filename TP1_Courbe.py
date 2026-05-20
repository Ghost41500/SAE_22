    #Question 1 :

"""
import numpy as np
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)
"""
    #Question 2 : 

"""
import numpy as np
import matplotlib.pyplot as plt

# Génération du signal (question 1)
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Représentation graphique
plt.figure(figsize=(10, 4))
plt.plot(T, X1, color='blue', label='X1 = sin(2π × 2 × t)')

plt.title('Signal sinusoïdal X1 – F = 2 Hz, Amplitude = 1')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
"""
    #Question 3 :  

"""
import numpy as np
import matplotlib.pyplot as plt

# Signal X1 (question 1)
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Signal X2 : fréquence 5 Hz, amplitude 2
F2 = 5
X2 = 2 * np.sin(F2 * np.pi * 2 * T)
plt.figure(figsize=(10, 4))
plt.plot(T, X1, color='blue', label='X1 – F=2Hz, Amp=1')
plt.plot(T, X2, color='red', label='X2 – F=5Hz, Amp=2')
plt.title('Signaux X1 et X2')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
"""
    #Question 4 :

"""
import numpy as np
import matplotlib.pyplot as plt

# Signal X1 (question 1) :
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Signal X2 (Question 3) :
F2 = 5
X2 = 2 * np.sin(F2 * np.pi * 2 * T)

# Signal X3 (Question 4) :
X3 = X1 + X2

# Représentation graphique :
plt.figure(figsize=(10, 4))
plt.plot(T, X1, color='blue', label='X1 – F=2Hz, Amp=1')
plt.plot(T, X2, color='red', label='X2 – F=5Hz, Amp=2')
plt.plot(T, X3, color='green', label='X3 = X1 + X2')  
plt.title('Signaux X1, X2 et X3')   
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
"""
    #Question 5 : 

"""
import numpy as np
import matplotlib.pyplot as plt

# Signaux
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)
F2 = 5
X2 = 2 * np.sin(F2 * np.pi * 2 * T)
X3 = X1 + X2

# Affichage des trois signaux
plt.figure(figsize=(10, 4))
plt.plot(T, X1, color='blue', label='X1 – F=2Hz, Amp=1')
plt.plot(T, X2, color='red', label='X2 – F=5Hz, Amp=2')
plt.plot(T, X3, color='green', label='X3 = X1 + X2')

# Vérification sur quelques points : on marque t = 0, 0.25, 0.5, 0.75
points = [0, 0.25, 0.5, 0.75]
for t_val in points:
    idx = np.argmin(np.abs(T - t_val))  # trouve l'indice le plus proche
    plt.plot(T[idx], X1[idx], 'bo', markersize=8)
    plt.plot(T[idx], X2[idx], 'ro', markersize=8)
    plt.plot(T[idx], X3[idx], 'go', markersize=8)
    # Affiche les valeurs sur le graphe
    plt.annotate(f'X3={X3[idx]:.2f}', xy=(T[idx], X3[idx]),
                 xytext=(T[idx]+0.01, X3[idx]+0.15), fontsize=8, color='green')

plt.title('Signaux X1, X2 et X3 avec vérification de quelques points')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Vérification numérique dans le terminal
print("Vérification numérique sur quelques points :")
print(f"{'t':>6} | {'X1':>6} | {'X2':>6} | {'X1+X2':>8} | {'X3':>6} | {'Égaux ?':>8}")
print("-" * 55)
for t_val in points:
    idx = np.argmin(np.abs(T - t_val))
    egal = np.isclose(X1[idx] + X2[idx], X3[idx])
    print(f"{T[idx]:>6.2f} | {X1[idx]:>6.3f} | {X2[idx]:>6.3f} | "
          f"{X1[idx]+X2[idx]:>8.3f} | {X3[idx]:>6.3f} | {str(egal):>8}")
"""
    #Question 6 : 

"""
import numpy as np
import matplotlib.pyplot as plt
import random

# Signal X1
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Génération du bruit à différents niveaux
bruit_faible  = np.array([random.uniform(-0.1, 0.1) for _ in T])
bruit_moyen   = np.array([random.uniform(-0.5, 0.5) for _ in T])
bruit_fort    = np.array([random.uniform(-1.0, 1.0) for _ in T])

X1_bruit_faible = X1 + bruit_faible
X1_bruit_moyen  = X1 + bruit_moyen
X1_bruit_fort   = X1 + bruit_fort

# Affichage
fig, axes = plt.subplots(3, 1, figsize=(10, 8))

axes[0].plot(T, X1, color='blue', label='X1 original', linewidth=1)
axes[0].plot(T, X1_bruit_faible, color='orange', label='Bruit faible (±0.1)', linewidth=0.8)
axes[0].set_title('Bruit faible')
axes[0].legend()
axes[0].grid(True)

axes[1].plot(T, X1, color='blue', label='X1 original', linewidth=1)
axes[1].plot(T, X1_bruit_moyen, color='orange', label='Bruit moyen (±0.5)', linewidth=0.8)
axes[1].set_title('Bruit moyen')
axes[1].legend()
axes[1].grid(True)

axes[2].plot(T, X1, color='blue', label='X1 original', linewidth=1)
axes[2].plot(T, X1_bruit_fort, color='orange', label='Bruit fort (±1.0)', linewidth=0.8)
axes[2].set_title('Bruit fort')
axes[2].legend()
axes[2].grid(True)

plt.xlabel('Temps (s)')
plt.tight_layout()
plt.show()
"""
    #Question 7 : 

"""

import numpy as np
import matplotlib.pyplot as plt

# Base de temps
T = np.linspace(0, 1, 1001)
F = 2

# Différents types de signaux
X_cos    = np.cos(2 * np.pi * F * T)               # Cosinus
X_abs    = np.abs(np.sin(2 * np.pi * F * T))        # Sinus redressé (valeur absolue)
X_carre  = np.sign(np.sin(2 * np.pi * F * T))       # Signal carré
X_dent   = 2 * (T * F - np.floor(T * F + 0.5))      # Signal dent de scie

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
"""