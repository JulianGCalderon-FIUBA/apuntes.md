---
title: Probabilidad
---

## Definiciones

- **Experimento Aleatorio:** Conozco todos los posibles resultados, pero no sé cuál va a ocurrir.
- **Espacio Muestral $\Omega$:** Conjunto de resultados posibles del experimento aleatorio.
- **Evento $A \in \Omega$:** Resultado particular del experimento.
- **Frecuencia Relativa:** Cuantas veces ocurre un evento particular en un número determinado de eventos.
- **Espacio Equiprobable:** Todos los elementos del espacio muestral tienen la misma probabilidad de ocurrir.

$$
P(A) = \lim_{n\to\infty} \frac{\#A}{n}
$$

## Laplace

En un espacio equiprobable se puede calcular la probabilidad de $A$ a partir de un conteo de eventos.

$$
P(A) = \frac{\#A}{\#\Omega}
$$

## Definición Axiomática de Probabilidad

$$
P(A) : \Omega \to [0,1]
$$

### Axiomas

1. $0 \leq P(A) \leq 1, \quad \forall A\in \mathscr A$
2. $P(\Omega) = 1$
3. $A, B \ /\  A\cap B = \emptyset \implies P(A\cup B) = P(A) + P(B)$
4. $A_1 \geq A_2 \geq A_3 \geq\cdots \  / \ \cap_{i=1}^\infty A_i = \emptyset \implies \lim_{n\to\infty} P(A_n) = 0$

### Propiedades

$$
P(\overline A) = 1 - P(A) \tag{1}
$$

$$
P(A \cup B) = P(A) + P(B) - P(A\cap B) \tag{2}
$$

$$
\begin{align}
P(A \cup B \cup C) &= P(A) + P(B) + P(C) \\
&- P(A\cap B) - P(A\cap C) - P(B\cap C) \\
&+ P(A \cap B \cap C)
\end{align} \tag{3}$$

## Álgebra de Eventos

**Álgebra de Eventos: $\mathscr A$:** Conjunto de eventos a los que le puedo calcular su probabilidad.

Dado $\Omega$, entonces $\mathscr A$ es álgebra de eventos si:

1. $\Omega \in \mathscr A$
2. Si $B \in \mathscr A$, entonces $\overline B \in \mathscr A$
3. Si $A, B \in \mathscr A$, entonces $A \cup B \in \mathscr A$
4. Si $(A_n)_{n \geq 1}$ es sucesión de $\mathscr A$, entonces $\cup_{i=1}^\infty A_i \in \mathscr A$

### Propiedades

1. $\emptyset \in \mathscr A$
2. $\cup_{i=1}^n A_i \in \mathscr A$
3. $\cap_{i=1}^n A_i \in \mathscr A$

### Teorema 1

Sea $(A_n)_{n \geq 1}$ una sucesión eventos tal que $A_n \subset A_{n+1}$ y $A = \cup_{i=1}^\infty A_i$, luego

$$

P(A) = \lim_{n\to\infty}P(A_n)

$$

### Teorema 2

Sea $(A_n)_{n \geq 1}$ una sucesión eventos tal que $A_n \supset A_{n+1}$ y $A = \cap_{i=1}^\infty A_i$, luego

$$

P(A) = \lim_{n\to\infty}P(A_n)

$$

### Teorema ($\sigma$-aditividad)

Sea $A = \cup_{i=1}^\infty A_i \in \mathscr A$, con los eventos $A_i$ mutuamente excluyentes dos a dos, entonces

$$

P(A) = P(\cup_{i=1}^\infty A_i) = \sum_{i=1}^\infty P(A_i)

$$
