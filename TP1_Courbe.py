import numpy as np
import matplotlib.pyplot as plt
import random 

# Signal X1 (question 1) :
F = 2
T = np.linspace(0, 1, 1001)
X1 = np.sin(F * np.pi * 2 * T)
 
# Signal X2 (Question 3) :
F2 = 5
X2 = 2 * np.sin(F2 * np.pi * 2 * T)

#Signal X3 (Question 4) :
X3 = X1+X2

# Représentation graphique (Question 2 et 3) :
plt.figure(figsize=(10, 4))
plt.plot(T, X1, color='blue', label='X1 – F=2Hz, Amp=1')
plt.plot(T, X2, color='red', label='X2 – F=5Hz, Amp=2')
plt.plot(T, X3, color='green', label='X3 = X1 + X2')    
points = [0, 0.25, 0.5, 0.75]
for t_val in points:
    idx = np.argmin(np.abs(T - t_val))   
    plt.plot(T[idx], X1[idx], 'bo', markersize=8)
    plt.plot(T[idx], X2[idx], 'ro', markersize=8)
    plt.plot(T[idx], X3[idx], 'go', markersize=8)
plt.title('Signaux X1, X2 et X3')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()