#!/usr/bin/env python3
# 
# Questo programma mostra, a scopo didattico, come le proprietà caotiche 
# della mappa logistica ($x_{n+1} = a \cdot x_n (1 - x_n)$) possano essere 
# utilizzate in crittografia. Si adotta qui una delle tecniche più 
# classiche: la permutazione caotica (scrambling/shuffle) dei bit (o dei 
# caratteri) guidata dalla sequenza caotica.
# 
# Come funziona lo script:
# 
# - Conversione in Bit: La stringa viene convertita in una sequenza continua 
# di bit ($0$ e $1$).
# 
# - Generazione della Permutazione Caotica (genera_permutazione):
# A partire dal seme $x_0$, la mappa logistica $x_{n+1} = a \cdot x_n (1 - x_n)$ 
# genera $N$ numeri reali caotici tra $0$ e $1$.   
# 
# - Con np.argsort(x) otteniamo l'ordine posizionale di questi numeri. Poiché 
# il sistema è caotico, questo ordine è imprevedibile e appare completamente casuale.
# 
# - Rimescolamento (Scrambling): I bit della stringa vengono spostati secondo 
# la nuova mappa di indici generata.
# 
# - Decifratura e Sensibilità: Per ricomporre i bit nell'ordine originario occorre 
# conoscere esattamente $x_0$. Se la chiave differisce anche soltanto della 
# milionesima cifra decimale (es. 0.5432198766 invece di 0.5432198765), 
# la mappa produce una permutazione completamente diversa, rendendo il testo 
# totalmente illeggibile.
# 
import numpy as np
import random

def delta_casuale():
    return random.randint(0, 999_999) / 1_000_000

def genera_permutazione(x0, a, n_bits):
    """
    Genera un vettore di indici permutati basato sulla sequenza caotica 
    della mappa logistica per n_bits.
    """
    # Array per memorizzare i valori caotici
    x = np.zeros(n_bits)
    x_curr = x0
    
    # Scartiamo le prime iterazioni (transiente) per eliminare dipendenze iniziali
    for _ in range(100):
        x_curr = a * x_curr * (1 - x_curr)
        
    # Generiamo un valore caotico unico per ogni bit
    for i in range(n_bits):
        x_curr = a * x_curr * (1 - x_curr)
        x[i] = x_curr
        
    # argsort restituisce gli indici che ordinerebbero l'array 'x'.
    # Questo genera una permutazione pseudo-casuali e univoca degli indici [0, n_bits-1].
    perm_indices = np.argsort(x)
    return perm_indices


def string_to_bits(testo):
    """Converte una stringa ASCII/UTF-8 in una lista di bit (0 e 1)."""
    bytes_testo = testo.encode('utf-8')
    bits = []
    for byte in bytes_testo:
        # Estrae gli 8 bit di ciascun byte
        bits.extend([(byte >> i) & 1 for i in reversed(range(8))])
    return bits


def bits_to_string(bits):
    """Converte una lista di bit (0 e 1) di lunghezza multipla di 8 in stringa."""
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i+8]
        byte_val = 0
        for b in byte_bits:
            byte_val = (byte_val << 1) | b
        bytes_list.append(byte_val)
    return bytes(bytes_list).decode('utf-8', errors='replace')


def cifra_scramble(testo, x0, a=3.99):
    """Cifra la stringa rimescolando i suoi bit tramite la mappa logistica."""
    bits_originali = string_to_bits(testo)
    n_bits = len(bits_originali)
    
    # Indici di permutazione caotica
    perm = genera_permutazione(x0, a, n_bits)
    
    # Rimescola i bit in base all'ordine caotico
    bits_cifrati = [bits_originali[i] for i in perm]
    return bits_cifrati, n_bits


def decifra_scramble(bits_cifrati, x0, a=3.99):
    """Decifra i bit rimescolati riapplicando la permutazione inversa."""
    n_bits = len(bits_cifrati)
    
    # Rigenera esattamente la stessa permutazione grazie al valore chiave x0
    perm = genera_permutazione(x0, a, n_bits)
    
    # Inversione della permutazione
    bits_decifrati = [0] * n_bits
    for orig_idx, perm_idx in enumerate(perm):
        bits_decifrati[perm_idx] = bits_cifrati[orig_idx]
        
    return bits_to_string(bits_decifrati)


# =====================================================================
# ESEMPIO PRATICO E DIMOSTRAZIONE DIDATTICA
# =====================================================================

messaggio_originale = "Quel ramo del lago di Como, che volge a mezzogiorno, tra due catene non interrotte di monti, tutto a seni e a golfi, a seconda dello sporgere e del rientrare di quelli, vien, quasi a un tratto, a ristringersi, e a prender corso e figura di fiume."
# chiave_corretta_x0 = 0.5432198765
chiave_corretta_x0 = delta_casuale()
parametro_a = 3.99  # Regime fortemente caotico

print("=== MESSAGGIO ORIGINALE ===")
print(messaggio_originale)
print()

# 1. Cifratura
bits_cifrati, n_bits = cifra_scramble(messaggio_originale, chiave_corretta_x0, parametro_a)

# Rappresentazione visiva dei bit rimescolati
str_bits_cifrati = "".join(str(b) for b in bits_cifrati[:128]) + "..."
print("=== CIFRATURA ===")
print(f"Totale bit rimescolati: {n_bits}")
print(f"Primi 128 bit del testo cifrato: {str_bits_cifrati}")
print()

# 2. Decifratura con la CHIAVE CORRETTA
testo_decifrato = decifra_scramble(bits_cifrati, chiave_corretta_x0, parametro_a)
print("=== DECIFRATURA CON CHIAVE CORRETTA ===")
print(f"Chiave x0: {chiave_corretta_x0}")
print(f"Risultato: {testo_decifrato}")
print()

# 3. Tentativo di Decifratura con CHIAVE ERRATA (anche solo per 1e-10)
# chiave_errata_x0 = 0.5432198766  # Differenza infinitesima (0.0000000001)
chiave_errata_x0 = chiave_corretta_x0 + 0.0000000001
testo_decifrato_errato = decifra_scramble(bits_cifrati, chiave_errata_x0, parametro_a)

print("=== TENTATIVO CON CHIAVE ERRATA (Effetto Farfalla) ===")
print(f"Chiave errata x0: {chiave_errata_x0}")
print(f"Risultato: {testo_decifrato_errato}")
