Un estadístico es cualquier función medible $T_m = T(\underline X)$ con valores en un espacio euclídeo de dimensión finita.

Dado una muestra aleatoria $\underline X$, un estadístico es una función de la muestra aleatoria que, evaluada en los valores observados, debe poder resultar en un valor numérico.

Esta función no puede depender de parámetros desconocidos.

## Estadísticos Suficientes

Sea $\underline X$ un vector aleatorio de dimensión $n$ cuya distribución es $F_\theta(\underline x)$, $\theta \in M$, se dice que un estadístico $T$ es suficiente para $\theta$ si la distribución de $\underline X$ condicionada a que $T = t$ es independiente de $\theta\ \forall t$

Esto significa que si conozco $T$ y la distribución $\underline X | T = t$, entonces puedo reconstruir una muestra con la misma distribución que la muestra original.

Un estadístico es una función de la muestra aleatoria, por lo que también es una variable aleatoria.

## Teorema de Factorización

Sea $\underline X$ un vector aleatorio con función de densidad (o probabilidad) conjunta $f_\theta(\underline x), \theta \in M$, entonces el estadístico $T = r(\underline X)$ es suficiente para $\theta$ si y solo si existen dos funciones $h, g$ tales que

$$
f_\theta(x) = g(r(\underline x), \theta) \cdot h(\underline x)
$$

Para el caso de familias exponenciales a $k$ parámetros, entonces tendrá como estadístico suficiente al vector:

 $T = (r_1(\underline x), \cdots, r_k(\underline x))$
