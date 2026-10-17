# Cifratura didattica mediante la mappa logistica

## 1. Introduzione

Il programma `cifraturacaos.py` illustra un metodo di **rimescolamento dei bit (*bit scrambling*) basato sulla mappa logistica**, un modello matematico non lineare utilizzato nello studio dei sistemi dinamici caotici. L'idea di base consiste nell'utilizzare una successione numerica generata da una funzione caotica per determinare un nuovo ordine dei bit di un messaggio.

Il programma dimostra tre concetti:

- **Caos deterministico:** una semplice formula matematica può generare successioni numeriche complesse.
- **Sensibilità alle condizioni iniziali:** piccole differenze nel valore iniziale possono modificare sensibilmente la successione generata.
- **Permutazione dei bit:** un messaggio può essere trasformato riordinando i suoi bit secondo una permutazione determinata dalla successione numerica.

L'esperimento mostra inoltre come una chiave iniziale differente possa produrre una permutazione diversa e rendere impossibile la ricostruzione corretta del messaggio applicando la procedura di decifratura con quella chiave errata.

**Importante:** si tratta di una dimostrazione didattica, non di un sistema crittografico sicuro per proteggere informazioni riservate.

## 2. La teoria matematica: la mappa logistica

Il sistema utilizza la mappa logistica, definita dalla relazione ricorsiva:

$$
\boxed{x_{n+1}=a\,x_n(1-x_n)}
$$

dove:

- $x_n$ è il valore della successione all'iterazione $n$;
- $x_{n+1}$ è il valore calcolato all'iterazione successiva;
- $x_0$ è la condizione iniziale;
- $a$ è il parametro di controllo della dinamica.

Nel programma viene utilizzato il valore:

$$
a=3.99
$$

Questo parametro si trova in una regione caotica della mappa logistica.

A ogni iterazione, il risultato precedente viene reinserito nella stessa formula. Si ottiene così una successione di valori che, nel regime caotico, può presentare un andamento irregolare e una forte sensibilità alle condizioni iniziali.

### 2.1 Sensibilità alle condizioni iniziali

Consideriamo due successioni generate con lo stesso parametro $a$, ma con condizioni iniziali leggermente differenti:

$$
x_0\neq y_0
$$

Le iterazioni successive sono determinate dalle relazioni:

$$
x_{n+1}=a\,x_n(1-x_n)
$$

$$
y_{n+1}=a\,y_n(1-y_n)
$$

La differenza tra i valori all'iterazione $n$ è:

$$
\Delta_n=|x_n-y_n|
$$

Nel regime caotico, una differenza iniziale molto piccola può amplificarsi rapidamente. In una prima fase, la crescita può essere approssimata da una legge esponenziale:

$$
\Delta_n\approx\Delta_0e^{\lambda n}
$$

dove $\lambda$ rappresenta l'esponente di Lyapunov.

Quando $\lambda>0$, il sistema presenta sensibilità alle condizioni iniziali.

Questa proprietà è spesso associata all'**effetto farfalla**: piccole variazioni dello stato iniziale possono produrre traiettorie molto differenti.

Nel programma, questa caratteristica viene utilizzata per illustrare perché una piccola variazione della chiave possa cambiare il rimescolamento dei bit.

## 3. La rappresentazione del messaggio in bit

Un computer rappresenta il testo attraverso sequenze di byte. Il programma converte quindi il messaggio originale in una successione di bit, ciascuno dei quali può assumere soltanto due valori:

$$
b_i\in\{0,1\}
$$

La funzione `string_to_bits(testo)` esegue questa conversione.

Per prima cosa, la stringa viene codificata in UTF-8:

```python
bytes_testo = testo.encode('utf-8')
```

Successivamente, ogni byte viene scomposto nei suoi otto bit, dal più significativo al meno significativo.

Per esempio, il carattere ASCII `A` corrisponde al valore decimale 65, ossia alla rappresentazione binaria:

$$
65=01000001_2
$$

Il carattere viene quindi rappresentato mediante otto bit.

Per un messaggio di $N$ byte, la sequenza risultante contiene:

$$
\boxed{N_{\text{bit}}=8N}
$$

bit.

La lunghezza della sequenza è importante perché determina il numero di valori della mappa logistica necessari per costruire la permutazione.

## 4. Generazione della permutazione caotica

La funzione `genera_permutazione(x0, a, n_bits)` costituisce il nucleo matematico del programma.

Il suo compito è generare una permutazione degli indici dei bit, utilizzando la successione prodotta dalla mappa logistica.

### 4.1 Condizione iniziale e transiente

Il calcolo parte dal valore iniziale $x_0$, che viene utilizzato come chiave.

Prima di generare i valori destinati alla permutazione, il programma esegue 100 iterazioni preliminari:

```python
for _ in range(100):
    x_curr = a * x_curr * (1 - x_curr)
```

Queste iterazioni costituiscono un transiente iniziale che il programma scarta prima di costruire la successione utilizzata per il rimescolamento.

Questa scelta è una procedura numerica del programma; non garantisce, da sola, l'eliminazione di ogni dipendenza dalla condizione iniziale.

### 4.2 Generazione della successione

Dopo le iterazioni preliminari, viene generato un valore per ciascun bit:

```python
for i in range(n_bits):
    x_curr = a * x_curr * (1 - x_curr)
    x[i] = x_curr
```

Si ottiene così un array:

$$
X=(x_0',x_1',\ldots,x_{N-1}')
$$

dove $N$ rappresenta il numero di bit del messaggio e i valori $x_i'$ sono quelli prodotti dalle iterazioni della mappa.

Per distinguerli dalla condizione iniziale della cifratura, si usa qui l'apice.

### 4.3 Ordinamento degli indici

Il passaggio decisivo è:

```python
perm_indices = np.argsort(x)
```

La funzione `np.argsort(x)` restituisce gli indici che ordinerebbero i valori dell'array in ordine crescente.

Per esempio, se:

$$
X=(0.7,\ 0.2,\ 0.9,\ 0.4)
$$

l'ordine crescente dei valori è:

$$
0.2,\ 0.4,\ 0.7,\ 0.9
$$

e gli indici corrispondenti sono:

$$
P=(1,\ 3,\ 0,\ 2)
$$

La sequenza degli indici rappresenta una permutazione delle posizioni originali.

Nel programma, l'ordinamento dei valori generati dalla mappa logistica determina quindi il nuovo ordine dei bit.

È importante precisare che la permutazione è **pseudo-casuale**, non una permutazione casuale crittograficamente garantita. La sua struttura dipende dalla successione numerica, dalla precisione dei calcoli e dalla condizione iniziale.

## 5. Cifratura: il rimescolamento dei bit

La funzione `cifra_scramble(testo, x0, a=3.99)` esegue la procedura di cifratura didattica.

Le operazioni principali sono:

1. Conversione del testo in una sequenza di bit.
2. Calcolo del numero totale di bit.
3. Generazione della permutazione attraverso la mappa logistica.
4. Riordinamento dei bit secondo gli indici ottenuti.

La trasformazione viene eseguita mediante:

```python
bits_cifrati = [bits_originali[i] for i in perm]
```

Indicando con $B$ la sequenza originale e con $P$ la permutazione, la trasformazione può essere scritta come:

$$
\boxed{C_i=B_{P_i}}
$$

dove:

- $B_i$ è il bit originale;
- $C_i$ è il bit nella posizione $i$ della sequenza rimescolata;
- $P_i$ indica la posizione originale del bit selezionato.

Il risultato è una sequenza di bit contenente gli stessi bit del messaggio originale, ma in un ordine diverso.

La funzione restituisce sia la sequenza rimescolata sia il numero totale di bit.

### 5.1 Che cosa cambia e che cosa rimane invariato?

La permutazione modifica le posizioni dei bit, ma non i loro valori.

Pertanto:

- il numero totale di bit rimane invariato;
- il numero di bit uguali a zero rimane invariato;
- il numero di bit uguali a uno rimane invariato;
- la lunghezza del messaggio in byte rimane invariata.

Questa proprietà distingue una semplice permutazione da una trasformazione che modifica anche i valori dei dati.

## 6. Decifratura: ricostruzione dell'ordine originale

Per recuperare il messaggio, il programma rigenera la stessa permutazione utilizzando gli stessi parametri della cifratura.

La funzione `decifra_scramble(bits_cifrati, x0, a=3.99)` calcola nuovamente:

```python
perm = genera_permutazione(x0, a, n_bits)
```

Successivamente, ricostruisce l'ordine originale mediante:

```python
bits_decifrati = [0] * n_bits

for orig_idx, perm_idx in enumerate(perm):
    bits_decifrati[perm_idx] = bits_cifrati[orig_idx]
```

In termini matematici, se la cifratura è definita da:

$$
C_i=B_{P_i}
$$

la decifratura ricostruisce:

$$
\boxed{B_{P_i}=C_i}
$$

In questo modo, ciascun bit cifrato viene riportato nella sua posizione originale.

Infine, la funzione `bits_to_string(bits)` ricompone i bit in gruppi di otto, ricostruisce i byte e li decodifica come testo UTF-8.

La decifratura riesce quando viene rigenerata esattamente la stessa permutazione utilizzata durante la cifratura.

## 7. Il ruolo della chiave

Nel programma, la chiave principale è la condizione iniziale $x_0$.

La cifratura e la decifratura devono utilizzare valori compatibili di:

- condizione iniziale $x_0$;
- parametro logistico $a$;
- lunghezza della sequenza da rimescolare.

Il parametro $a$ è impostato a $3.99$ per impostazione predefinita, mentre $x_0$ viene generato casualmente tramite:

```python
def delta_casuale():
    return random.randint(0, 999_999) / 1_000_000
```

La funzione genera un valore nell'intervallo:

$$
0\leq x_0\leq0.999999
$$

Nell'esempio, la chiave viene generata una sola volta e riutilizzata per la decifratura corretta.

### 7.1 Tentativo con una chiave errata

Il programma prova anche a decifrare il messaggio con una chiave leggermente diversa:

```python
chiave_errata_x0 = chiave_corretta_x0 + 0.0000000001
```

La differenza introdotta è:

$$
\Delta x_0=10^{-10}
$$

La nuova condizione iniziale genera una nuova successione numerica e può produrre una permutazione differente.

Quando la permutazione utilizzata per la decifratura non coincide con quella originale, i bit vengono ricollocati nelle posizioni sbagliate. Il risultato può essere un testo illeggibile.

Tuttavia, una differenza minima nella chiave non garantisce matematicamente che ogni bit venga spostato o che il testo risultante sia sempre totalmente illeggibile. Il risultato dipende dalle due permutazioni effettivamente generate.

## 8. Limiti crittografici del metodo

Questo esperimento è utile per studiare il caos deterministico e le permutazioni, ma **non deve essere utilizzato per proteggere dati reali**.

La sensibilità alle condizioni iniziali non è sufficiente a rendere sicuro un algoritmo crittografico.

I principali limiti sono i seguenti.

### 8.1 Il messaggio viene soltanto permutato

La procedura non modifica il valore dei bit, ma ne cambia soltanto l'ordine.

Di conseguenza, conserva il numero di zeri e di uni e non introduce, da sola, una trasformazione crittografica sufficientemente robusta.

### 8.2 La generazione della chiave non è crittograficamente sicura

Il programma utilizza il modulo `random`, che non è progettato per la generazione di chiavi crittografiche.

Inoltre, il valore iniziale viene estratto da un insieme di appena un milione di possibilità. Lo spazio delle chiavi è quindi troppo piccolo per offrire una protezione adeguata.

### 8.3 La precisione numerica è finita

I numeri utilizzati da Python e NumPy sono rappresentati con precisione finita.

Questo significa che le traiettorie numeriche non possiedono precisione infinita e che la sensibilità alle condizioni iniziali non implica una sicurezza crittografica.

### 8.4 Non sono garantite riservatezza e integrità

La procedura non fornisce un meccanismo di autenticazione del messaggio e non garantisce la sua integrità.

Per applicazioni reali è preferibile utilizzare algoritmi crittografici standard e implementazioni consolidate, come AES-GCM o ChaCha20-Poly1305.

## 9. Considerazioni finali

Il programma dimostra come una proprietà matematica della mappa logistica possa essere impiegata per generare una permutazione dei bit di un messaggio.

Il processo si basa su una catena di operazioni:

1. Il testo viene convertito in bit.
2. La mappa logistica genera una successione numerica.
3. L'ordinamento dei valori determina una permutazione degli indici.
4. I bit vengono rimescolati secondo tale permutazione.
5. La stessa permutazione permette di ricostruire il messaggio originale.

L'esperimento mette in relazione sistemi dinamici non lineari, caos deterministico, rappresentazione binaria dei dati e trasformazioni reversibili, ma ricordiamo che **una dinamica caotica può generare permutazioni complesse, ma il caos da solo non costituisce una garanzia di sicurezza crittografica**.
