    #Question 19 : 
"""
import numpy as np
import matplotlib.pyplot as plt

# Signal X1 continu
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Étape 1 : Échantillonnage (Te = 20 ms)
Te = 0.02
T_ech  = np.arange(0, 1, Te)
X1ech  = np.sin(F * np.pi * 2 * T_ech)

# Étape 2 : Quantification du signal échantillonné (q = 0.2)
q = 0.2
X1echq = q * np.round(X1ech / q)

# Affichage sur une figure unique
plt.figure(figsize=(10, 5))
plt.plot(T, X1, color='blue', label='X1 continu', linewidth=1)
plt.plot(T_ech, X1ech,  'ro', markersize=6, label=f'X1ech (Te={Te*1000:.0f} ms)')
plt.plot(T_ech, X1echq, 'gs', markersize=6, label=f'X1echq (q={q})')

plt.title(f'X1 continu, échantillonné (Te={Te*1000:.0f} ms) et quantifié (q={q})')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Affichage console
print(f"Période d'échantillonnage : Te = {Te*1000} ms → {len(T_ech)} échantillons")
print(f"Pas de quantification     : q  = {q}")
print(f"\n{'t (s)':>6} | {'X1ech':>7} | {'X1echq':>7} | {'Erreur':>7}")
print("-" * 38)
for i in range(len(T_ech)):
    print(f"{T_ech[i]:>6.3f} | {X1ech[i]:>7.4f} | {X1echq[i]:>7.4f} | {X1ech[i]-X1echq[i]:>7.4f}")
"""
    #Question 20 : 

"""
import numpy as np
import matplotlib.pyplot as plt

# Signal X1 continu
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Échantillonnage (Te = 20 ms)
Te = 0.02
T_ech  = np.arange(0, 1, Te)
X1ech  = np.sin(F * np.pi * 2 * T_ech)

# Quantification (q = 0.2)
q = 0.2
X1echq = q * np.round(X1ech / q)

# Erreur de quantification
E = X1ech - X1echq

# Affichage sur 3 sous-graphes
fig, axes = plt.subplots(3, 1, figsize=(10, 9))

# Graphe 1 : X1ech
axes[0].stem(T_ech, X1ech, linefmt='r-', markerfmt='ro', basefmt='k-', label='X1ech')
axes[0].set_title(f'Signal échantillonné X1ech (Te={Te*1000:.0f} ms)')
axes[0].set_ylabel('Amplitude')
axes[0].legend()
axes[0].grid(True)

# Graphe 2 : X1echq
axes[1].stem(T_ech, X1echq, linefmt='g-', markerfmt='gs', basefmt='k-', label=f'X1echq (q={q})')
axes[1].set_title(f'Signal échantillonné et quantifié X1echq (q={q})')
axes[1].set_ylabel('Amplitude')
axes[1].legend()
axes[1].grid(True)

# Graphe 3 : Erreur
axes[2].stem(T_ech, E, linefmt='b-', markerfmt='bd', basefmt='k-', label='E = X1ech - X1echq')
axes[2].axhline(y= q/2, color='gray', linestyle='--', linewidth=1, label=f'+q/2 = +{q/2}')
axes[2].axhline(y=-q/2, color='gray', linestyle='--', linewidth=1, label=f'-q/2 = -{q/2}')
axes[2].set_title('Erreur de quantification E = X1ech - X1echq')
axes[2].set_ylabel('Erreur')
axes[2].set_xlabel('Temps (s)')
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.show()

# Valeurs caractéristiques
print(f"Erreur maximale  : {E.max():.4f}")
print(f"Erreur minimale  : {E.min():.4f}")
print(f"Erreur moyenne   : {E.mean():.4f}")
print(f"Borne théorique  : ±q/2 = ±{q/2}")
"""
#Question 21 : 

"""
import numpy as np
import matplotlib.pyplot as plt

# Signal X1 continu
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

periodes = [0.01, 0.02, 0.05, 0.1]  # 10, 20, 50, 100 ms
q = 0.2

fig, axes = plt.subplots(len(periodes), 1, figsize=(10, 10))
fig.suptitle(f'Effet de Te sur l\'erreur (q fixe = {q})', fontsize=13)

for i, Te in enumerate(periodes):
    T_ech  = np.arange(0, 1, Te)
    X1ech  = np.sin(F * np.pi * 2 * T_ech)
    X1echq = q * np.round(X1ech / q)
    E      = X1ech - X1echq

    axes[i].stem(T_ech, E, linefmt='b-', markerfmt='bd', basefmt='k-',
                 label=f'Erreur – Te={Te*1000:.0f}ms ({len(T_ech)} échantillons)')
    axes[i].axhline(y= q/2, color='gray', linestyle='--', linewidth=1)
    axes[i].axhline(y=-q/2, color='gray', linestyle='--', linewidth=1)
    axes[i].set_ylabel('Erreur')
    axes[i].set_ylim(-0.2, 0.2)
    axes[i].legend(fontsize=8)
    axes[i].grid(True)
    print(f"Te={Te*1000:.0f}ms | nb échantillons={len(T_ech):>3} | "
          f"erreur max={E.max():.4f} | erreur min={E.min():.4f} | moyenne={E.mean():.4f}")

axes[-1].set_xlabel('Temps (s)')
plt.tight_layout()
plt.show()

Te = 0.02
T_ech  = np.arange(0, 1, Te)
X1ech  = np.sin(F * np.pi * 2 * T_ech)

valeurs_q = [0.1, 0.2, 0.5, 1.0]

fig2, axes2 = plt.subplots(len(valeurs_q), 1, figsize=(10, 10))
fig2.suptitle(f'Effet de q sur l\'erreur (Te fixe = {Te*1000:.0f} ms)', fontsize=13)

print("\n")
for i, q in enumerate(valeurs_q):
    X1echq = q * np.round(X1ech / q)
    E      = X1ech - X1echq

    axes2[i].stem(T_ech, E, linefmt='r-', markerfmt='rs', basefmt='k-',
                  label=f'Erreur – q={q} | borne théorique ±{q/2}')
    axes2[i].axhline(y= q/2, color='gray', linestyle='--', linewidth=1)
    axes2[i].axhline(y=-q/2, color='gray', linestyle='--', linewidth=1)
    axes2[i].set_ylabel('Erreur')
    axes2[i].set_ylim(-0.6, 0.6)
    axes2[i].legend(fontsize=8)
    axes2[i].grid(True)
    print(f"q={q:.1f} | erreur max={E.max():.4f} | erreur min={E.min():.4f} | "
          f"borne théorique ±{q/2}")

axes2[-1].set_xlabel('Temps (s)')
plt.tight_layout()
plt.show()
"""
    #Question 22 : 

"""
import numpy as np
import matplotlib.pyplot as plt

# Signal X1 continu
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Échantillonnage (Te = 20 ms)
Te = 0.02
T_ech  = np.arange(0, 1, Te)
X1ech  = np.sin(F * np.pi * 2 * T_ech)

# Quantification (q = 0.2)
q = 0.2
X1echq = q * np.round(X1ech / q)
print("=" * 55)
print("   VALEURS NUMÉRIQUES ENREGISTRÉES EN MÉMOIRE (décimal)")
print("=" * 55)
print(f"{'Index':>6} | {'t (s)':>6} | {'X1echq':>8} | {'Binaire (8 bits)':>18}")
print("-" * 55)

# Conversion en entier sur 8 bits (valeurs entre -1 et +1 → entre -128 et +127)
def to_binary_8bit(val, q, amp=1):
    # Normalisation entre 0 et 255 pour stockage 8 bits non signé
    val_norm = int(round((val + amp) / (2 * amp) * 255))
    val_norm = np.clip(val_norm, 0, 255)
    return format(val_norm, '08b')

for i in range(len(T_ech)):
    binaire = to_binary_8bit(X1echq[i], q)
    print(f"{i:>6} | {T_ech[i]:>6.3f} | {X1echq[i]:>8.4f} | {binaire:>18}")

print("\n")
print("=" * 40)
print("   RÉSUMÉ – COÛT MÉMOIRE")
print("=" * 40)
nb_echantillons = len(T_ech)
bits_par_echantillon = 8
total_bits  = nb_echantillons * bits_par_echantillon
total_bytes = total_bits / 8
print(f"Nombre d'échantillons : {nb_echantillons}")
print(f"Bits par échantillon  : {bits_par_echantillon} bits")
print(f"Total bits            : {total_bits} bits")
print(f"Total octets          : {total_bytes:.0f} octets")

plt.figure(figsize=(12, 4))
plt.step(T_ech, X1echq, where='mid', color='red',  label='X1echq (valeurs quantifiées)', linewidth=1.5)
plt.plot(T,     X1,     color='blue', label='X1 continu', linewidth=1, alpha=0.5)

for i in range(len(T_ech)):
    binaire = to_binary_8bit(X1echq[i], q)
    plt.annotate(binaire, xy=(T_ech[i], X1echq[i]),
                 xytext=(T_ech[i], X1echq[i] + 0.12),
                 fontsize=5, ha='center', color='darkgreen', rotation=90)

plt.title('Valeurs numériques en mémoire – X1echq avec code binaire 8 bits')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
"""