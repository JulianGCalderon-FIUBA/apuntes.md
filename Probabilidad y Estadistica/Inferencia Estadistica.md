Una inferencia consiste en construir un modelo sobre la base de datos experimentales y extraer conclusiones

Definimos **poblacion** como la totalidad de los resultados experimentales

Al realizar el experimento una cierta cantidad de veces obtenemos un conjunto de datos, esto se denomina **muestra**.

A partir de la muestra, podemos analizar el comportamiento de la poblacion

## Muestra

Definimos muestra como una variable aleatoria $X$, definida sobre $(\Omega, \mathcal A, P)$ con distribucion desconocida (al menos parcialmente) $F_X(x) = P(X \leq x)$

Esta variable aleatoria representa lo que llamamos un **observable** del experimento aleatorio

Si poseemos una muestra infinita, esto se puede respresentar como una sucesion infinita de variables aleatorias $X_1, X_2, X_3, \cdots$, todas identicamente distribuidas a $X$

Por lo que la funcion de conjunto se define de la siguiente forma

$$
F_{X_1, \cdots, X_n}(x_1, \cdots, x_n) = \prod_{i=1}^n F_X(x_i) \quad \forall n \in \mathbb{N}
$$

Sea $\underline X$ un muestra aleatoria de tamaño $n$, con $X_1, \cdots, X_n \overset{iid}{\sim} F_X(x)$

Llamamos $\underline x$ al conjunto de las $n$ observaciones obtenidas al realizar el expermiento $n$.
