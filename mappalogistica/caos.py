# caos.py by Giorgio Ruffa (c)2026
#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import random

def delta_casuale():
    return random.randint(0, 999_999) / 1_000_000
    
def mappa_logistica(a, x0, n_passi):
    """Calcola la sequenza della mappa logistica."""
    x = np.zeros(n_passi)
    x[0] = x0
    for i in range(1, n_passi):
        x[i] = a * x[i-1] * (1 - x[i-1])
    return x

# Parametri della simulazione
a = 3.97          # Valore nel regime caotico (a > 3.57)
n_passi = 51     # Numero di iterazioni

# Due condizioni iniziali quasi identiche
x0_a = 0.5
# x0_b = 0.500001
x0_b = delta_casuale()

# Calcolo delle serie
serie_a = mappa_logistica(a, x0_a, n_passi)
serie_b = mappa_logistica(a, x0_b, n_passi)

# Creazione dei grafici
plt.figure(figsize=(12, 6))

# Grafico 1: Serie temporale caotica
plt.subplot(2, 1, 1)
plt.plot(serie_a, 'o-', color='tab:blue', linewidth=1.5, markersize=4, label=f'$x_0 = {x0_a}$')
plt.title(f'Comportamento Caotico della Mappa Logistica ($a = {a}$)', fontsize=14)
plt.ylabel('$x_n$', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right')

# Grafico 2: Sensibilità alle condizioni iniziali (Effetto Farfalla)
plt.subplot(2, 1, 2)
plt.plot(serie_a, 'o-', color='tab:blue', linewidth=1.5, markersize=4, label=f'$x_0 = {x0_a}$')
plt.plot(serie_b, 's--', color='tab:red', linewidth=1.5, markersize=4, label=f'$x_0 = {x0_b}$')
plt.title('Sensibilità alle Condizioni Iniziali (Divergenza delle traiettorie)', fontsize=14)
plt.xlabel('Iterazione ($n$)', fontsize=12)
plt.ylabel('$x_n$', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()
