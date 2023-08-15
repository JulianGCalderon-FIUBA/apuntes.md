## Función de Variable Aleatoria

Sea $Y = g(X)$ una función de variable aleatorio, siendo $X$ una V.A.D., $Y$ será discreta, con:

$$
\begin{align}
p_Y(y) = P(Y = y) = \sum_{x \in B} p_X(x) \\
\qquad  B =\{x \in \mathbb{R}: g(x) = y\}
\end{align}
$$

Si mi variable aleatoria no es discreta, entonces generalizamos:

$$
F_Y(y) = P(Y \leq y) = P(g(X) \leq y)
$$

## Truncamiento

Truncamiento consiste en encontrar una nueva función de densidad para el caso de probabilidad condicional. Podemos restringir la función para cuando $X\in A$, manteniendo las propiedades de una función de densidad.

$$
f_{X|X\in A}(x) \qquad F_{X|X\in A}(x) = P(X \leq x | x \in A)
$$

A partir de desarrollar la probabilidad condicional, obtenemos

$$
f_{X|X\in A}(x) = \frac{f_X(x)\ \mathbf{1}\{x \in A\}}{P(X \in A)}
$$

## Cuantil

Un cuantil de una variable aleatorio será el menor $x_\alpha$ tal que

$$
P(X \leq x_\alpha) = \alpha
$$

Es decir, buscamos un valor de $x$ tal que acumule a izquierda una probabilidad $\alpha$

$$
F_X(x_\alpha) \geq \alpha
$$
