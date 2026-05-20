    #Question 8 : 

""" 
import numpy as np
import matplotlib.pyplot as plt

# Signal X1
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Quantification
q = 0.5  # pas de quantification
X1q = q * np.round(X1 / q)  # signal quantifié

# Affichage
plt.figure(figsize=(10, 4))
plt.plot(T, X1,  color='blue',   label='X1 original (continu)')
plt.plot(T, X1q, color='red',    label=f'X1q quantifié (q = {q})')

plt.title(f'Signal X1 et signal quantifié X1q (pas q = {q})')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Afficher les niveaux de quantification en pointillés
niveaux = np.arange(-1, 1.1, q)
for n in niveaux:
    plt.axhline(y=n, color='gray', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()

# Affichage des niveaux possibles
print(f"Pas de quantification : q = {q}")
print(f"Niveaux possibles : {niveaux}")
"""
    #Question 9 : 

"""
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
"""
    #Question 10 : 

"""
import numpy as np
import matplotlib.pyplot as plt

# Signal X1
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Différentes valeurs de q
valeurs_q = [0.1, 0.25, 0.5, 1.0]

fig, axes = plt.subplots(len(valeurs_q), 2, figsize=(14, 10))

for i, q in enumerate(valeurs_q):
    X1q = q * np.round(X1 / q)
    E = X1 - X1q

    # Colonne gauche : signal original vs quantifié
    axes[i, 0].plot(T, X1,  color='blue', label='X1 original', linewidth=1)
    axes[i, 0].plot(T, X1q, color='red',  label=f'X1q (q={q})', linewidth=1)
    axes[i, 0].set_title(f'Signal quantifié – q = {q}')
    axes[i, 0].set_ylabel('Amplitude')
    axes[i, 0].legend(fontsize=8)
    axes[i, 0].grid(True)

    # Colonne droite : erreur de quantification
    axes[i, 1].plot(T, E, color='green', label=f'E = X1 - X1q')
    axes[i, 1].axhline(y= q/2, color='gray', linestyle='--', linewidth=1, label=f'+q/2 = +{q/2}')
    axes[i, 1].axhline(y=-q/2, color='gray', linestyle='--', linewidth=1, label=f'-q/2 = -{q/2}')
    axes[i, 1].set_title(f'Erreur de quantification – q = {q}')
    axes[i, 1].set_ylabel('Erreur')
    axes[i, 1].legend(fontsize=8)
    axes[i, 1].grid(True)

    # Affichage console
    print(f"q = {q} → erreur max = {E.max():.4f} | erreur min = {E.min():.4f} | borne théorique ±{q/2}")

axes[-1, 0].set_xlabel('Temps (s)')
axes[-1, 1].set_xlabel('Temps (s)')
plt.tight_layout()
plt.show()
"""
    #Question 11 : 

"""
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
"""