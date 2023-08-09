> [!note]
> $A$**, Principio del buen orden:** Todo subconjunto no vacío de $\mathbb{N}$ tiene un primer elemento

> [!note]
> $B$**, Principio de inducción:** Sea $p(n)$ una proposición tal que para cada $n \in \mathbb{N}$ verifica:
> 
> - $\exists n_0 \in \mathbb{N}: p(n_0) \text{ es verdadera}$
> - $n \geq n_0: p(n) \to p(n + 1) \text{ es verdadera}$
> 
> Entonces $p(n)$ es verdadera $\forall n \geq n_0$

Los principios no se pueden probar, por eso se llaman principios. Si tomamos uno como un axioma, entonces el otro se transforma en un teorema.

## Prueba de $A \to B$

Supongamos que $B$ falsa, entonces es falso que $p(n) \text{ es verdadera},\ \forall n\geq n_0$. Luego $\exists n \geq n_0: p(n) \text{es falsa}$.

Definimos $F = \{n \in \mathbb{N}: p(n) \text{ es falsa}\} \neq \emptyset$, como suponemos $B$ falsa, entonces este conjunto no es vacío.

Por $A$, existe un primer elemento $F: n_1 \geq n_0$. Luego, por definición de $n_1$, $p(n_1 - 1)$ es verdadera. Debido a $B$, $p(n_1 -1 +1) = p(n_1)$ es verdadera. Pero $p(n_1)$ es falsa por $F$. Llegamos a una contradicción, por lo que $B$ debe ser verdadera si suponemos $A$.

## Inducción Fuerte

El principio de inducción fuerte se utiliza en situaciones donde la situación débil no es suficiente para una demostración. Ambos son verdaderos, dado el principio del buen orden (y viceversa)

Sea $p(n)$ una proposición tal que para cada $n \in \mathbb{N}$ verifica:

- $\forall n:n_0 \leq n \leq n_0 +j,\  p(n) \text{ es verdadera}$
- $\forall k\geq  n_0 + j: p(i) \text{ es verdadera }\forall i \in [a, k] \to p(k+1) \text{ es verdadera}$

Entonces $p(n)$ es verdadera $\forall n \geq n_0$
