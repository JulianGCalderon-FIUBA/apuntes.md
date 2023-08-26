Una inferencia consiste en construir un modelo sobre la base de datos experimentales y extraer conclusiones

Definimos **población** como la totalidad de los resultados experimentales

Al realizar el experimento una cierta cantidad de veces obtenemos un conjunto de datos, esto se denomina **muestra**.

A partir de la muestra, podemos analizar el comportamiento de la población

## Muestra

Definimos muestra como una variable aleatoria $X$, definida sobre $(\Omega, \mathcal A, P)$ con distribución desconocida (al menos parcialmente) $F_X(x) = P(X \leq x)$

Esta variable aleatoria representa lo que llamamos un **observable** del experimento aleatorio

Si poseemos una muestra infinita, esto se puede representar como una sucesión infinita de variables aleatorias $X_1, X_2, X_3, \cdots$, todas idénticamente distribuidas a $X$

Por lo que la función de conjunto se define de la siguiente forma

$$
F_{X_1, \cdots, X_n}(x_1, \cdots, x_n) = \prod_{i=1}^n F_X(x_i) \quad \forall n \in \mathbb{N}
$$

Sea $\underline X$ una muestra aleatoria de tamaño $n$, con $X_1, \cdots, X_n \overset{iid}{\sim} F_X(x)$

Llamamos $\underline x$ al conjunto de las $n$ observaciones obtenidas al realizar el experimento $n$.
