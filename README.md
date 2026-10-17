# La mappa logistica: una formula semplice che genera il caos

La **mappa logistica** (*logistic map*) è un modello matematico discreto e non lineare, introdotto per studiare l'evoluzione di popolazioni biologiche. È diventato uno degli esempi classici della teoria del caos deterministico.

La sua caratteristica più sorprendente è che una formula estremamente semplice può generare comportamenti che vanno dalla convergenza verso un valore stabile fino a oscillazioni periodiche e sequenze apparentemente casuali.

## 1. La formula matematica

La mappa logistica è definita dalla relazione ricorsiva:

$$\
\boxed{x\_{n+1}=r,x_n(1-x_n)}\
$$

dove:

- $x_n$ è lo stato del sistema all'iterazione $n$, normalmente compreso tra 0 e 1;
- $x\_{n+1}$ è lo stato all'iterazione successiva;
- $r$ è il parametro di controllo, che determina il comportamento dinamico del sistema.

Se interpretiamo $x_n$ come una popolazione normalizzata, il termine $r x_n$ rappresenta la crescita, mentre il fattore $(1-x_n)$ introduce un limite dovuto alle risorse disponibili.

La dinamica si ottiene applicando ripetutamente la stessa formula, usando ogni volta il risultato precedente come nuovo ingresso.

Per esempio, scegliendo $r=2.5$ e $x_0=0.2$:

$$\
x_1=2.5\cdot0.2\cdot0.8=0.4\
$$

$$\
x_2=2.5\cdot0.4\cdot0.6=0.6\
$$

$$\
x_3=2.5\cdot0.6\cdot0.4=0.6\
$$

Il sistema converge dunque a $0.6$, un valore fisso.

## 2. I diversi comportamenti al variare di $r$

Il parametro $r$ è la chiave per comprendere la mappa logistica. Mantenendo lo stesso valore iniziale $x_0$, basta modificarlo per ottenere dinamiche radicalmente diverse.

### A. Convergenza verso un punto fisso

Per $0\<r<3$, il sistema converge a un valore stabile, con alcune precisazioni per i casi limite e per le condizioni iniziali eccezionali.

Per $1\<r<3$, il punto fisso non nullo è:

$$\
\boxed{x^\*=1-\frac{1}{r}}\
$$

### B. Oscillazioni periodiche

Per valori di $r$ superiori a 3, il punto fisso non nullo perde stabilità e compare un ciclo di periodo 2: il sistema alterna due valori.

Aumentando ulteriormente $r$, si susseguono cicli di periodo 4, 8, 16 e così via.

Questo processo prende il nome di **cascata di raddoppiamento del periodo** (*period-doubling cascade*).

### C. Regime caotico

Intorno a:

$$\
r\_\infty \approx 3.5699456\
$$

si raggiunge il limite di accumulazione della cascata di raddoppiamento del periodo. Oltre questa soglia si trovano ampie regioni caotiche, alternate a finestre di periodicità.

Nel regime caotico, la sequenza può diventare aperiodica e fortemente sensibile alle condizioni iniziali.

Non tutti i valori di $r$ superiori alla soglia producono caos: esistono anche intervalli in cui ricompaiono comportamenti periodici.

## 3. Perché il comportamento sembra casuale?

La mappa logistica è un sistema **deterministico**: conoscendo esattamente $r$ e $x_0$, la sequenza successiva è interamente determinata.

Eppure, nel regime caotico, presenta alcune proprietà tipiche.

### 3.1 Sensibilità alle condizioni iniziali

Due valori iniziali quasi identici possono produrre sequenze molto diverse dopo poche decine di iterazioni.

Se la differenza iniziale è $\delta_0$, durante una fase di divergenza può verificarsi approssimativamente:

$$\
|\delta_n|\approx|\delta_0|e^{\lambda n}\
$$

dove $\lambda$ è l'esponente di Lyapunov.

Quando $\lambda>0$, piccole differenze tendono a crescere esponenzialmente, almeno finché questa approssimazione rimane valida.

Questa proprietà limita la prevedibilità pratica del sistema a lungo termine.

### 3.2 Aperiodicità

Nel regime caotico, la sequenza non si stabilizza necessariamente e non ripete un ciclo regolare. I valori possono apparire irregolari, pur essendo generati da una legge precisa.

### 3.3 Struttura nascosta

Il caos non equivale a una distribuzione completamente casuale. I valori sono vincolati dalla funzione:

$$\
f(x)=rx(1-x)\
$$

La distribuzione delle iterazioni può presentare strutture e regolarità statistiche.

### 3.4 Transizione attraverso biforcazioni

Il caos emerge attraverso una successione di cambiamenti qualitativi del sistema.

La cascata di raddoppiamenti del periodo è uno dei fenomeni più noti ed è caratterizzata dalla costante universale di Feigenbaum:

$$\
\boxed{\delta\approx4.6692016}\
$$

Questa costante descrive il rapporto limite tra le distanze successive dei parametri di biforcazione nella cascata.

## 4. Il diagramma di biforcazione

Il diagramma di biforcazione è una delle rappresentazioni visive più efficaci della mappa logistica.

Sull'asse orizzontale si riporta il parametro $r$; su quello verticale si riportano i valori di $x_n$, dopo aver eliminato le iterazioni iniziali transitorie.

Indicativamente:

- Una sola linea indica la convergenza verso un punto fisso.
- Due linee indicano un ciclo di periodo 2.
- Quattro linee indicano un ciclo di periodo 4.
- Una moltitudine di punti segnala una regione caotica.

La struttura si ramifica sempre più rapidamente fino alla comparsa del regime caotico, pur con alcune finestre di periodicità.

## 5. Un caso interessante: $r=4$

Per $r=4$, la ricorrenza diventa:

$$\
\boxed{x\_{n+1}=4x_n(1-x_n)}\
$$

È uno dei casi classici di dinamica caotica. Per quasi tutte le condizioni iniziali nell'intervallo $(0,1)$, la sequenza mostra sensibilità alle condizioni iniziali e un esponente di Lyapunov positivo, pari a:

$$\
\lambda=\ln 2\
$$

Esistono tuttavia condizioni iniziali eccezionali. Per esempio, se $x_0=0.5$, allora:

$$\
x_1=4\cdot0.5\cdot(1-0.5)=1\
$$

e successivamente:

$$\
x_2=4\cdot1\cdot(1-1)=0\
$$

Da quel momento la sequenza rimane a zero.

Queste eccezioni mostrano perché è scorretto affermare che ogni condizione iniziale produca caos.

## 6. Caos deterministico e numeri pseudo-casuali

È utile distinguere tre concetti:

| Concetto         | Significato                                                                           |
| ---------------- | ------------------------------------------------------------------------------------- |
| Determinismo     | La stessa condizione iniziale produce la stessa sequenza.                             |
| Caos             | La dinamica presenta sensibilità alle condizioni iniziali e altre proprietà caotiche. |
| Pseudo-casualità | Una sequenza appare casuale, ma è prodotta da un algoritmo deterministico.            |

La mappa logistica può generare sequenze dall'aspetto pseudo-casuale, ma **non è automaticamente un buon generatore di numeri casuali**.

Le sue correlazioni, la dipendenza dal parametro e la precisione finita dei calcolatori possono renderla inadatta, soprattutto per applicazioni crittografiche.

In un computer, inoltre, i valori sono rappresentati con precisione finita. Se lo stato appartiene a un insieme finito di valori e l'aggiornamento è deterministico, prima o poi la sequenza entrerà necessariamente in un ciclo.

## 7. In conclusione

La mappa logistica dimostra che **la complessità non richiede necessariamente formule complicate**.

Una semplice equazione quadratica, iterata nel tempo, può produrre:

- stabilità;
- periodicità;
- biforcazioni;
- caos deterministico;
- sensibilità alle condizioni iniziali.

Il suo interesse scientifico sta proprio nella convivenza tra semplicità della legge e imprevedibilità pratica dell'evoluzione.

La sequenza non è priva di regole: è la sensibilità della dinamica a rendere difficile prevederne l'andamento a lungo termine.

## 8. Possibili esperimenti

Un programma molto semplice può aiutare a esplorare la mappa logistica:

1. Scegliere un valore iniziale $x_0$ compreso tra 0 e 1.
2. Scegliere un parametro $r$.
3. Calcolare ripetutamente $x\_{n+1}=r x_n(1-x_n)$.
4. Visualizzare la sequenza in un grafico.
5. Ripetere l'esperimento modificando leggermente $x_0$ oppure $r$.

Confrontando i risultati si può osservare direttamente la transizione dalla stabilità al comportamento periodico e caotico.

