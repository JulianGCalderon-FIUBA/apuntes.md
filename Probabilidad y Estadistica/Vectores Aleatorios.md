---
title: Vectores Aleatorios
---

Sea $(\Omega, \mathscr A, P)$ un espacio muestral, se dice que $X = (X_1, X_2, \cdots, X_n)$ es un vector aleatorio de dimensión $n$, si para cada $J = 1, \cdots, n$, $X_j: \Omega \to \mathbb{R}$ es una variable aleatoria.

Para todo $x = (x_1, \cdots, x_n) \in \mathbb{R}^n$ se tendrá que

$$
X^{-1}((-\infty, x_1), (-\infty, x_2), \cdots, (-\infty, x_n)) \in \mathscr A
$$

Un vector aleatorio es un vector formado por variables aleatorias.

## Función de Distribución

Sea $\Bbb X = (X_1, \cdots,X_n)$ un vector aleatorio continuo de dimensión $n$, entonces definimos la función de distribución como

$$
F_{\Bbb X}(x) = P(X_1 \leq x_1, \cdots, X_n \leq x_n)
$$

### Propiedades con $\Bbb X = (X,Y)$

1. $\lim\limits_{x,y \to \infty} F_{\Bbb X}(x) = 1, \lim\limits_{x \to -\infty} F_{\Bbb X}(x) = 0, \lim\limits_{y \to -\infty} F_{\Bbb X}(x) = 0$
2. $F_{\Bbb X}(x)$ es monótona no decreciente en cada variable
3. $F_{\Bbb X}(x)$ es continua a derecha en cada variable
4. $P((x,y) \in (a_1, b_1) \times (a_2, b_2)) = F_{\Bbb X}(b_1, b_2)- F_{\Bbb X}(b_1, a_2) F_{\Bbb X}(a_1, b_2) + F_{\Bbb X}(a_1, a_2)$

## Función de Probabilidad

Sean $X, Y$ dos variables aleatorias discretas, la probabilidad conjunta se define para cada par de números $(x,y)$ como

$$
P_{x,y}(x,y) = P(X = x, Y = y)
$$

Además, debe cumplirse que la probabilidad sea positiva, y la sumatoria de todas las probabilidades es $1$.

Se define la **probabilidad marginal** como la probabilidad de que una de las variables tome un valor particular se define como.

$$
P_X(x) = \sum_y^{n_y} P(X = x, Y=y)
$$

$$
P_Y(y) = \sum_x^{n_x} P(X = x, Y=y)
$$

En general, para un conjunto $A$. Entonces la probabilidad se calcula de la siguiente manera

$$
P((x,y) \in A) = {\sum\sum}_{(x,y) \in A} P_{x,y}(x,y)
$$

## Función de Densidad

Para un vector aleatorio continuo, se define función de densidad a una función que satisface

1. $f_{x,y}(x,y) \geq 0$
2. $\int_{-\infty}^\infty\int_{-\infty}^\infty f_{x,y}(x,y) dxdy = 1$

Entonces, para cualquier conjunto $A$

$$
P((x,y) \in A) = \iint_A f_{x,y}(x,y) dxdy
$$

Las funciones de **densidad marginal** de $X, Y$ serán

$$
f_X(x) = \int_{-\infty}^\infty f_{x,y}(x,y) dy
$$

$$
f_Y(y) = \int_{-\infty}^\infty f_{x,y}(x,y) dx
$$

## Independencia

Sea $(X,Y)$ un vector aleatorio, las variables aleatorias $X, Y$ son independientes si y solo si

$$
P(X \in A \cap Y \in B) = P(X \in A) P(Y \in B)\quad \forall A,B
$$

### Propiedades

1. Se dice que $X_1, \cdots, X_n$ son variables aleatorias independientes si y solo si

	$$
    F_{X_1, \cdots, X_n}(x_1, \cdots x_n) = F_{X_1}(x_1) \cdots F_{X_n}(x_n)
    $$

2. Para el caso de variables aleatorias discretas, son independientes si y solo si

	$$
    P_{X_1, \cdots, X_n}(x_1, \cdots x_n) = P_{X_1}(x_1) \cdots P_{X_n}(x_n)
    $$

3. Para el caso de variables aleatorias continuas, son independientes si y solo si (vale para casi todo $x_1, \cdots, x_n$)

$$
f_{X_1, \cdots, X_n}(x_1, \cdots x_n) = f_{X_1}(x_1) \cdots f_{X_n}(x_n)
$$
