## Espectro de un Grafo

Sea $G$ un grafo, entonces definimos su espectro $\sigma(G)$ como el espectro de su matriz de adyacencia, $\sigma(A_G)$.

El espectro de un grafo es un invariante, pero no lo caracteriza. Dos grafos no isomorfos pueden tener el mismo espectro (aunque no es tan fácil de encontrar)

Un $C_4 + N_1$ tiene el mismo espectro que un $K_{4,1}$, pero no son isomorfos. Trivialmente, uno es conexo y el otro no.

Notemos que la matriz de adyacencia depende del etiquetado de sus vértices, sin embargo, el espectro no depende de él. Sean $A, B$ dos matrices de adyacencia para dos grafos $G, H$ isomorfos. Entonces las matrices $A, B$ son semejantes (la misma permutación de vértices que define el isomorfismo, puede definir el cambio de las matrices). Si dos matrices son semejantes, comparten el mismo espectro. Además, una matriz simétrica es semejante a su matriz diagonal.

$$
G \sim H \iff A_G \sim A_H
$$

La suma de autovalores de la matriz de adyacencia será, por ser cuadrada, la traza de la misma.

$$
\sum_{k=1}^n \lambda_k = 0
$$

Recordemos también que sea $p$ un polinomio y $P$, su polinomio de matrices asociado, entonces si $\lambda$ es autovalor de $A$, $p(\lambda)$ es autovalor de $P(A)$. Esto implica que si $\lambda$ es autovalor de $A$, $\lambda^n$ es autovalor de $A^n$.

Luego, la suma de los autovalores de $A^2$ es la suma de ciclos de longitud dos, cada uno contado dos veces.

$$
\sum_{k=1}^n \lambda_k^2 = 2m
$$

De igual forma, la suma de los autovalores de $A^3$ es la suma de triángulos, cada uno se cuenta tres veces (una por cada vértice), y cada uno tiene dos orientaciones, luego cada uno se cuenta 6 veces, entonces sea $\tau$ la cantidad de triángulos en $G$

$$
\sum_{k=1}^n \lambda_k^3 = 6\tau
$$

La matriz $J$, completa con unos, tiene $n-1$ autovalores de valor $0$, y un solo autovalor de multiplicidad de valor $n$. A partir de estas definiciones, podremos definir el espectro de $K_n$. Su matriz de adyacencia será $J - I$, luego definimos el polinomio $p(\lambda) = \lambda -1$, y su polinomio matricial asociado $P(A) = A - I$. Entonces, $A_{K_n} = J - I = P(J)$. Luego, el espectro de $K_n$ será $\sigma(G) = \{-1\ (\text{orden }n-1), n-1\}$.

De forma similar, se demuestra que:

- El espectro de un bipartito $K_{r,s}$ será $\sigma(G) = \{\pm\sqrt{rs}, 0 (r+s - 2)\}$.
- El espectro de un path $P_n$ será $\sigma(G) = \{2\cos(k\pi/(n+1)), k = 1,2,\cdots, n\}$.
- El espectro de un cubo $Q_3$, será $\sigma(G) = \{-3, 3, 1(3), -1(3)\}$.
