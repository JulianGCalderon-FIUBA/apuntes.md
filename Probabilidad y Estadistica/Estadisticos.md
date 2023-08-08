Un estadistico es cualquier función medible $T_m = T(\underline X)$ con valores en un espacio euclideo de dimensión finita.

Dado una muestra aleatoria $\underline X$, un estadistico es una función de la muestra aleatoria que, evaluada en los valores observados, debe poder resultar en un valor numérico.

Esta función no puede depender de parámetros deconocidos.

# Estadisticos Suficientes

Sea $\underline X$ un vector aleatorio de dimensión $n$ cuya distribución es $F_\theta(\underline x)$, $\theta \in M$, se dice que un estadistico $T$ es suficiente para $\theta$ si la distribucion de $\underline X$ condicionada a que $T = t$ es independiente de $\theta\ \forall t$

Esto significa que si ocnozco $T$ y la distribucion $\underline X | T = t$, entonces puedo reconstruir una muestra con la misma distribucion que la muestra original.

Un estadistico es una funcion de la muestra aleatoria, por lo que tambien es una variable aleatoria.

# Teorema de Factorizacion

Sea $\underline X$ un vector aleatorio con funcion de densidad (o probabilidad) conjunta $f_\theta(\underline x), \theta \in M$, entonces el estadistico $T = r(\underline X)$ es suficiente para $\theta$ si y solo si existen dos funciones $h, g$ tales que

$$
f_\theta(x) = g(r(\underline x), \theta) \cdot h(\underline x)
$$

Para el caso de familias exponenciales a $k$ parametros, entonces tendra como estadistico suficiente al vector:

 $T = (r_1(\underline x), \cdots, r_k(\underline x))$