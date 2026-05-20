    #Question 12 : 

"""
import numpy as np
import matplotlib.pyplot as plt

# Signal X1 continu
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Échantillonnage : Te = 20 ms = 0.02 s
Te = 0.02
T_ech = np.arange(0, 1, Te)        # instants d'échantillonnage
X1ech = np.sin(F * np.pi * 2 * T_ech)  # valeurs du signal à ces instants

# Affichage
plt.figure(figsize=(10, 4))
plt.plot(T, X1, color='blue', label='X1 continu', linewidth=1)
plt.plot(T_ech, X1ech, 'ro', label=f'X1ech échantillonné (Te={Te*1000:.0f} ms)', markersize=6)

plt.title('Signal continu X1 et signal échantillonné X1ech')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Informations console
print(f"Période d'échantillonnage : Te = {Te*1000} ms")
print(f"Fréquence d'échantillonnage : Fe = {1/Te} Hz")
print(f"Nombre d'échantillons : {len(T_ech)}")
print(f"Premiers échantillons : {X1ech[:5].round(4)}")
"""
    #Question 13 : 

"""
import numpy as np
import matplotlib.pyplot as plt

# Signal X1 continu
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Différentes périodes d'échantillonnage
periodes = [0.01, 0.02, 0.05, 0.1]  # 10ms, 20ms, 50ms, 100ms

fig, axes = plt.subplots(len(periodes), 1, figsize=(10, 10))

for i, Te in enumerate(periodes):
    T_ech  = np.arange(0, 1, Te)
    X1ech  = np.sin(F * np.pi * 2 * T_ech)

    axes[i].plot(T_ech, X1ech, 'ro', markersize=5, label=f'X1ech (Te={Te*1000:.0f} ms)')
    axes[i].set_title(f'Te = {Te*1000:.0f} ms – Fe = {1/Te:.0f} Hz – {len(T_ech)} échantillons')
    axes[i].set_ylabel('Amplitude')
    axes[i].legend(fontsize=8)
    axes[i].grid(True)
    axes[i].set_ylim(-1.5, 1.5)

    print(f"Te={Te*1000:.0f}ms | Fe={1/Te:.0f}Hz | {len(T_ech)} échantillons")

axes[-1].set_xlabel('Temps (s)')
plt.tight_layout()
plt.show()
"""
    #Question 15 :

"""
import numpy as np
import matplotlib.pyplot as plt

# Signal X1 continu
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)

# Te maximal selon Shannon : Te = 1/(2*F) = 250 ms
Te_max = 1 / (2 * F)  # = 0.25 s
T_ech  = np.arange(0, 1, Te_max)
X1ech  = np.sin(F * np.pi * 2 * T_ech)

# Affichage
plt.figure(figsize=(10, 4))
plt.plot(T, X1, color='blue', label='X1 continu', linewidth=1)
plt.plot(T_ech, X1ech, 'ro', markersize=10, label=f'X1ech (Te={Te_max*1000:.0f} ms – limite Shannon)')

plt.title(f'X1 échantillonné à la limite de Shannon – Te = {Te_max*1000:.0f} ms, Fe = {1/Te_max:.0f} Hz')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print(f"Te max = {Te_max*1000:.0f} ms")
print(f"Fe min = {1/Te_max:.0f} Hz")
print(f"Nombre d'échantillons : {len(T_ech)}")
print(f"Valeurs échantillonnées : {X1ech.round(4)}")
"""
    #Question 16 : 

"""
import numpy as np
import matplotlib.pyplot as plt

# Signaux X1 et X2
F1 = 2
F2 = 5
T = np.linspace(0, 1, 1001)
X1 = np.sin(F1 * np.pi * 2 * T)
X2 = 2 * np.sin(F2 * np.pi * 2 * T)
X3 = X1 + X2

# Échantillonnage de X3 : Te = 20 ms
Te = 0.02
T_ech  = np.arange(0, 1, Te)
X3ech  = np.sin(F1 * np.pi * 2 * T_ech) + 2 * np.sin(F2 * np.pi * 2 * T_ech)

# Affichage
plt.figure(figsize=(10, 4))
plt.plot(T, X3, color='green', label='X3 continu', linewidth=1)
plt.plot(T_ech, X3ech, 'ro', markersize=6, label=f'X3ech échantillonné (Te={Te*1000:.0f} ms)')

plt.title(f'Signal continu X3 et signal échantillonné X3ech (Te={Te*1000:.0f} ms)')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Informations console
print(f"Période d'échantillonnage : Te = {Te*1000} ms")
print(f"Fréquence d'échantillonnage : Fe = {1/Te} Hz")
print(f"Nombre d'échantillons : {len(T_ech)}")
print(f"Fréquence max dans X3 : {F2} Hz")
print(f"Condition Shannon : Fe={1/Te} Hz > 2×{F2}={2*F2} Hz → {1/Te > 2*F2}")
"""
    #Question 18 : 

"""
import numpy as np
import matplotlib.pyplot as plt

# Signaux
F1 = 2
F2 = 5
T = np.linspace(0, 1, 1001)
X1 = np.sin(F1 * np.pi * 2 * T)
X2 = 2 * np.sin(F2 * np.pi * 2 * T)
X3 = X1 + X2

# Te maximal selon Shannon pour X3 : Te = 1/(2*Fmax) = 1/10 = 100 ms
Te_max = 1 / (2 * F2)  # = 0.1 s
T_ech  = np.arange(0, 1, Te_max)
X3ech  = np.sin(F1 * np.pi * 2 * T_ech) + 2 * np.sin(F2 * np.pi * 2 * T_ech)

# Affichage
plt.figure(figsize=(10, 4))
plt.plot(T, X3, color='green', label='X3 continu', linewidth=1)
plt.plot(T_ech, X3ech, 'ro', markersize=10, label=f'X3ech (Te={Te_max*1000:.0f} ms – limite Shannon)')

plt.title(f'X3 échantillonné à la limite de Shannon – Te={Te_max*1000:.0f} ms, Fe={1/Te_max:.0f} Hz')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print(f"Te max = {Te_max*1000:.0f} ms")
print(f"Fe min = {1/Te_max:.0f} Hz")
print(f"Nombre d'échantillons : {len(T_ech)}")
print(f"Valeurs échantillonnées : {X3ech.round(4)}")
"""