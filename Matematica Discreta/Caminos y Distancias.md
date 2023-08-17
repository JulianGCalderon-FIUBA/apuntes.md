---
title: Caminos y Distancias
---

## Caminos

Un $v_0{-}v_q$ camino es una sucesión alternada de vértices y aristas para viajar desde $v_0$ a $v_q$

$$
v_0e_1v_1e_2v_2\cdots e_qv_q, \quad \Psi(e_k) = \{v_{k-1}, v_k\} \ \forall k=1,2, \cdots, q
$$

- Un camino es cerrado si $v_0 = v_q$, de lo contrario es un camino abierto
- Un camino abierto que no repite aristas es un recorrido *(trail)*
- Un camino abierto que no repite vértices es un camino simple *(path)*
- Un camino cerrado que no repite aristas es un circuito *(circuit)*
- Un camino cerrado que no repite vértices intermedios se llama ciclo. *(cicle)*

## Longitud de un Camino

La longitud de un camino es la cantidad de aristas que tiene la sucesión. El camino trivial tiene longitud 0.

La distancia entre dos vértices es infinita si no hay un camino entre ellos, y es la longitud de un camino de longitud mínima cuando están conectados. Se denota $d(u,v)$, como la longitud de un $u{-}v$ camino geodésico (mínimo).

Podremos demostrar que la longitud mínima $d(u,v)$ entre dos vértices es una métrica, a partir de los axiomas de:

1. Unicidad de Distancia Nula: $d(u,v) = 0 \iff u = 0$.
2. Simetría: $d(u,v) = d(v,u)$
3. Desigualdad Triangular: $d(u,w) \leq d(u,v) + d(v,w)$

## Grafos Conexos

Un grafo es conexo si para cualquier par de vértices $u,v$ existe un $u{-}v$ camino. En caso contrario es disconexo.

La componente conexa maximal de un vértice es el conjunto de todos los vértices que están conectados con un camino. Existe un camino trivial que conecta todos los vértices consigo mismo. Un grafo conexo tiene una sola componente conexa.

Si un grafo es conexo, la distancia entre cualquier par de vértices es de a lo sumo $n - 1$, ya que si es mayor, entonces se estaría repitiendo algún vértice (no sería el camino mínimo). Luego, podemos verificar que un grafo es conexo a partir de $A_G$.

$$
\begin{gathered}
G \text{ es conexo} \iff \\
\forall v_i, v_j \in V(G),\forall i,j,\exists k \in N_0, k \in [0, n-1]: A_G^k(i,j) > 0 \iff \\
\sum_{k=0}^{n-1} A_G^k(i,j) > 0 \iff \\
(I_n + A_G)^{n-1}(i,j) > 0
\end{gathered}
$$

### Cortes

Definimos el conjunto de aristas $S$ como un corte de $G$, y con eliminar las aristas de $S$ de $G$, entonces el grafo se vuelve disconexo. Un corte es mínimo es no existe otro corte de cardinal menor. Un corte es minimal si no otro existe un corte contenido en el mismo. El cardinal del mínimo corte se denomina **arista-conectividad**: $\lambda(G)$.

De la misma forma, definimos un corte de vértices. Conjunto de vértices que, al eliminarlos, vuelve al grafo disconexo. El cardinal del mínimo corte se denomina **vértice-conectividad:** $\lambda'(G)$. Definimos la vértice-conectividad de $K_n$ como $n-1$. Esto es arbitrario, ya que no existe ningún vértice que al eliminarlo vuelva a un grafo completo, disconexo.

Los cortes de vértices son más fuertes que los cortes de aristas. Esto se debe a que podremos encontrar un corte de vértices de igual tamaño que un corte de aristas, si eliminamos todos los vértices incidentes sobre estas aristas.

$$
\lambda'(G) \leq \lambda(G)
$$

## Excentricidad

La excentricidad de un vértice es la máxima longitud hasta cualquier vértice, se define

$$
e(v_1) = \max\{d(v_1, x): x \in V(G)\}
$$

- El radio $R(G)$ será la mínima excentricidad. Más formalmente, $R(G) = \min \{e(v): v \in V(G)\}$. Se sobreentiende que no tendremos en cuenta el camino trivial.
- El diámetro $\Phi(G)$ como la máxima excentricidad. Más formalmente, $R(G) = \max \{d(u,v): u,v \in V(G)\}$
- El centro de un grafo $C(G)$ es el conjunto de vértices con mínima excentricidad
- La periferia de un grafo $P(G)$ es el conjunto de vértices con máxima excentricidad
- La cintura $g(G)$ de un grafo es de la longitud mínima de sus ciclos, si es un grafo acíclico, se define como infinito.
- La circunferencia $\text{cir}(G)$ de un grafo es de la longitud máxima de sus ciclos, si es un grafo acíclico, se define como infinito.

Un vértice puede no estar ni en el centro ni en la periferia de un grafo. En un grafo conexo, se verifica que $R(G) \leq \Phi(G) \leq 2R(G)$

## Separaciones

Sea $G$ un grafo conexo y $s,t$ dos vértices del grafo, entonces dos o más $s{-}t$ paths son de arista-disjuntos si no comparten aristas. De igual forma, son vértice-disjuntos si no comparten vértices, excepto los extremos.

Un conjunto de aristas (o vértices) separa $s$ de $t$ si su remoción destruye todo path entre $s$ y $t$.

La máxima cantidad de caminos **arista-disjuntos** o **vértice-disjuntos** es igual a la mínima cantidad de aristas o vértices que separan ambos vértices.
