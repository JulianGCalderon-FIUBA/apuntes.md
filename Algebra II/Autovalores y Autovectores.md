Vamos a buscar los vectores $v$ de $\Bbb  V$ tal que $T(v) = \lambda\ v$. Es decir, las rectas que pasadas por la transformación lineal, llegan a la misma recta.

Sea $A$ una matriz de $\Bbb K^{n\times n}$, y $x_0 \in \Bbb K^n$. Entonces podemos encontrar sucesiones de la forma:

$$
\begin{align*}
x_0 &= x_0\\
x_1 &= Ax_0\\
x_2 &= Ax_1 = A^2 x_0\\
\vdots &= \vdots\\
x_n &= Ax_{n-1} = A^nx_0\\
\end{align*}
$$

Las matrices mas fáciles de potenciar son las matrices diagonales.

$$
D = \text{diag}(\lambda_1,\lambda_2,\cdots,\lambda_n)
$$

$$
D^k = \text{diag}(\lambda_1^k,\lambda_2^k, \cdots, \lambda_n^k)
$$

Otras matrices fáciles de potenciar son aquellas que puedan ser factorizadas de la siguiente forma, siendo $D$ una matriz diagonal.

$$
A = Q\ D\ Q^{-1}
$$

$$
A^n = Q\ D^n\ Q^{-1}
$$

## Definición

Sea $A \in \Bbb K^{n \times n}$, un **autovalor** de $A$ es un escalar $\lambda \in \Bbb K$ tal que existe $v \in \Bbb K^n$ no nulo tal que $Av = \lambda v$. Se dice que $v$ es **autovector** de $A$.

Para encontrar estos elementos, primero buscamos $\lambda$ tal que $\text{det}(\lambda I - A) = 0$. Los autovectores asociados a cada $\lambda$ son $v \in \text{null}(\lambda I - A)$.

Definimos el polinomio característico de $A$ de grado $n$, $P_A(\lambda) = \text{det}(\lambda I - A)$.

Se le denomina **multiplicidad algebraica** de $\lambda_0$ a la multiplicidad de $\lambda_0$ como raíz del polinomio caracteristico.

Se le denomina **multiplicidad geométrica** de $\lambda_0$ a la dimensión del autoespacio asociado.

## Diagonalización

Se cumple entonces que $A = Q\ D\ Q^{-1}$, si cada columna de $Q$ es un autovector $A$ asociado al autovalor $\lambda$, correspondiente en la matriz diagonal $D$. Además, podemos encontrar un subespacio de los autovectores de $A$ asociados a $\lambda_0$. Este autoespacio se denomina $S_{\lambda = \lambda_0}$

Como existen infinitos autovectores para un mismo autovalor, entonces esa factorización no es única.

Encontramos que una matriz $A \in \Bbb K^{n\times n}$ puede ser factorizada como una matriz diagonal, si existen $n$ autovalores $\lambda$ distintos en $\Bbb K$. Si los autovalores se repiten, entonces basta con encontrar $n$ autovectores linealmente independientes, asociados a los autovalores encontrados. Es decir, se debe cumplir para cada autovalor que su multiplicidad algebraica sea igual a su multiplicidad geométrica.

## Propiedades

- $\text{det}(A) = \prod_{i = 0}^n \lambda_i$. (Se consideran los autovalores con repetición)
- $\text{tr}(A) = \sum_{i=1}^n \lambda_i$. (Se consideran los autovalores con repetición)
- Si $\lambda$ es autovalor de $A$ asociado al autovector $v$:
	- $(\lambda^k + t)$ es autovalor de $(A^k + tI)$ asociado al autovector $v$
	- Si $A$ es inversible, entonces $\frac 1\lambda$ es autovalor de $A^-1$ asociado al autovector $v$
- Si $\lambda$ es autovalor de $A$, entonces es autovalor de $A^T$
- La multiplicidad algebraica es siempre mayor o igual que la multiplicidad geométrica.

## Semejanza

Sean $A, B$ dos matrices de mismas dimensiones, se dice que $A$ es semejante a $B$ $(A \sim B)$ Si existe $Q$ tal que $A = Q\ B\ Q^{-1}$

- Es reflexiva: $A \sim A$
- Es simétrica: Si $A \sim B$, entonces $B \sim A$
- Es transitiva: Si $A \sim B$ y $B \sim C$, entonces $A \sim C$
- Si $\Bbb V$ es un espacio vectorial de dimension $n$. $B$ y $B'$ siendo bases de $\Bbb V$. Entonces podemos escribir una transformación lineal respecto a ambas bases

	$$
    [T]_{B'}^{B'} = M_{B}^{B'}\cdot [T]_B^B\cdot (M_{B}^{B'})^{-1}
    $$

	Podemos concluir que todas la representación de una transformación lineal con respecto a una misma base son semejantes entre si.

- Si $A \sim B$, entonces $A, B$ tienen los mismos autovalores, con la misma multiplicidad tanto algebraica como geométrica.

	$$
    A = P J P^{-1} \qquad B = R J R^{-1}
    $$

	$$
	A = \underbrace{PR^{-1}}_{Q} \ B\  \underbrace{P^{-1} R}_{Q^{-1}}
	$$

## Invariantes

Un subespacio $S \subseteq \Bbb K^n$ es un **subespacio invariante** de $A$ $(A\text{-invariante})$ si para todo vector $v \in S$, $Av \in S$.

Sabemos que todo autoespacio de $A$ es un subespacio $A\text{-invariante}$. Pero el reciproco no es cierto, hay subespacios invariantes de $A$ que no son autoespacios del mismo.

Un subespacio $S \subseteq \Bbb V$ es un **subespacio invariante** de $T:\Bbb V\to \Bbb V$ o $(T\text{-invariante})$ si para todo vector $v\in S$, se cumple que $T(v) \in S$

El núcleo y la imagen de una transformación lineal es un subespacio $T\text{-invariante}$.

## Transformación Lineal

Dados $\Bbb V {-} \Bbb K$ un espacio vectorial y $T: \Bbb V \to \Bbb V$ una transformacion lineal. Un autovalor de $T$ es un escalar $\lambda \in \Bbb K$ tal que existe $v \in \Bbb K^n$ no nulo que cumple $T(v) = \lambda v$

Se dice que $v$ es **autovector** de $T$ asociado a $\lambda$.

Llamamos **autoespacio** de $T$ asociado a $\lambda$ al subespacio $S_\lambda = \{v\in \Bbb V, T(v) = \lambda v\}$

Esta definición no tiene ninguna novedad, ya que se extiende de la definición original de autovalores y autovectores. Siempre podemos pensar una transformación lineal como un producto matricial entre la matriz asociada y el elemento a transformar.

Se le llama **polinomio característico** de $T$ a $P_T(\lambda) = \text{det}(\lambda I - [T]_B^B)$, donde $B$ es cualquier base de $\Bbb V$.

### Propiedades

- Si $T$ es una transformacion lineal no inyectiva (tiene nulo), $\lambda = 0$ es autovalor de $T$, siendo su autoespacio asociado el subespacio $Nu(T)$
- Sea $(D - \lambda I):\Bbb C^\infty \to \Bbb C^\infty$. Sabemos que $Nu(D - \lambda I) = gen\{e^{\lambda x}\}$. Entonces aplicando la propiedad anterior, $\lambda = 0$ es autovalor de ese operador, y el autoespacio asociado es $S = gen\{e^{\lambda x}\}$
- Sea $D:\Bbb C^\infty\to\Bbb C^\infty$, sabemos que $\lambda \in \mathbb{R}$ es autovalor de $D$, y para cada $\lambda$, su autoespacio asociado es $S = gen\{e^{\lambda x}\}$
- Si existe una base de $\Bbb V$ formada por autovectores de $T$, entonces $T$ es diagonalizables. La matriz $[T]_B^B$ sera una matriz diagonal. (propiedad de semejanza)

## Matrices de Jordan

Si una matriz $A \in \Bbb C^{3 \times 3}$ no es diagonalizable, podemos encontrar matrices de jordan similares a una matriz diagonal, tal que $A \sim J_i$

Llamamos $V_1, V_2, V_3$ las columnas de $Q$

### Caso 1

Si $A$ tiene un autovalor de multiplicidad algebraica $2$ y multiplicidad geometrica $1$. Llamamos $\lambda_1$ al autovalor de multiplicidad algebraica $2$, y $\lambda_2$ al autovalor de multiplicidad algebraica $1$.

$$
A_1 = 

Q
\begin{bmatrix}

\lambda_1 & 1 & 0 \\
0 & \lambda_1 & 0 \\
0 & 0 & \lambda_2

\end{bmatrix}
Q^{-1}
$$

Siendo $V_1, V_3$ los autovectores asociados a $\lambda_1, \lambda_2$.

$V_2$ el vector que cumple con el sistema $: (A - \lambda_1I)V_2 = V_1$

### Caso 2

Si $A$ tiene un autovalor de multiplicidad algebraica $3$ y multiplicidad geométrica $1$. Llamamos $\lambda$ al único autovalor

$$
A_2 = 

Q
\begin{bmatrix}

\lambda & 1 & 0 \\
0 & \lambda & 1 \\
0 & 0 & \lambda

\end{bmatrix}
Q^{-1}
$$

Siendo $V_1$ el autovector asociado a $\lambda$

$V_2$ el vector que cumple con el sistema $:(A - \lambda I)V_2 = V_1$

$V_3$ el vector que cumple con el sistema $: (A- \lambda I)V_3 = V_2$

En este caso, debemos elegir el $V_2$ que pertenezca a la imagen de $A- \lambda I$

### Caso 3

Si $A$ tiene un autovalor de multiplicidad algebraica $3$ y multiplicidad geométrica $2$. Llamamos $\lambda$ al único autovalor

$$
A_3 = 

Q
\begin{bmatrix}

\lambda & 0 & 0 \\
0 & \lambda & 1 \\
0 & 0 & \lambda

\end{bmatrix}
Q^{-1}
$$

Siendo $V_1$ un autovector asociado a $\lambda$

$V_2$ otro autovector asociado a $\lambda$

$V_3$ el vector que cumple con el sistema $: (A- \lambda I)V_3 = V_2$

En este caso, debemos elegir el $V_2$ que perteneza a la imagen de $A- \lambda I$
