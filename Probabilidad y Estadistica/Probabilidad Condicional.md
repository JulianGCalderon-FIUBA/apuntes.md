---
title: Probabilidad Condicional
---

Sea un espacio muestral y $A, B \in \mathscr A$ con $P(B) > 0$, la probabilidad condicional de $A$ dado que $B$ ha ocurrido está definida por

$$
P(A |B) = \frac{P(A\cap B)}{P(B)}
$$

## Propiedades

1. $0 \leq P(A|B) \leq 1, \quad \forall A \in \mathscr A$
2. $P(\Omega|B) = 1$
3. Si $A \cap C = \emptyset$, entonces $P(A\cup C | B) = P(A|B) + P(C | B)$
4. Si $P(B) > 0$, entonces
	1. $P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$
	2. $P(A \cap B \cap C) = P (A|B\cap C) \cdot \underbrace{P(B|C) \cdot P(C)}_{P(B\cap C)}$

## Particiones

Decimos que los eventos $B_1, B_2, \cdots, B_k$ es una partición de $\Omega$ si

1. $B_i \cap B_j = \emptyset, \quad \forall i \neq j$
2. $\cup_{i=1}^k B_i = \Omega$

Es decir, divido todo $\Omega$ en $k$ conjuntos mutuamente excluyentes dos a dos.

## Fórmula de Probabilidad Total

Sea el conjunto de eventos $B$ una partición de $\Omega$, entonces

$$
P(A) = \sum_{i=1}^k P(A|B_i)P(B_i)
$$

## Teorema de Bayes

Sea el conjunto de eventos $B$ una partición de $\Omega$, y $A$ un evento de probabilidad positiva. Entonces

$$
P(B_i|A) = \frac{P(A|B_i) P(B_i)}{\sum_{j=1}^k P(A|B_j)P(B_j)} = \frac{P(A|B_i) P(B_i)}{P(A)}
$$

## Diagrama de Árbol

Un diagrama de árbol es una forma gráfica de mostrar los distintos resultados del experimento aleatorio. Cada ramificación del árbol contiene, a su vez, distintos eventos que pueden resultar de él.

![[Probabilidad Condicional 1.png|450]]

Podemos ver que los elementos de nuestra álgebra de eventos son $A, B, C, D$. A su vez, $A,B$ es una partición de $\Omega$. Por lo que los eventos $C, D$ se pueden escribir en función de sus probabilidades respecto a $A,B$, a partir del teorema de Bayes.
