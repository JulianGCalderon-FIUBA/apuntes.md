Sea $S$ un conjunto de elementos a cubrir, y $L$  un conjunto de subconjuntos de $S$, entonces debemos elegir elementos de $L$ tal que:

- ***Cobertura:*** Se cubran todos los elementos de $S$ con solapamiento
- ***Partición:*** Se cubran todos los elementos de $S$ sin solapamiento
- ***Packing:*** Se cubra la mayor cantidad de elementos de $S$ que se pueda sin solapamiento.

Nótese que usualmente los problemas de *cobertura* y *packing* tienen solución óptima, mientras que los de ***partición*** pueden llegar a ser incompatibles

## Cobertura

Debemos plantear ecuaciones por cada elemento $s$ de $S$, utilizando aquellos elementos de $L$ que contienen al elemento $s$.

$$
\sum_{i:S_j\in L_i} Y_{L_i} \geq 1
$$

Al menos uno de los elementos de sumatorio debe tener como valor uno. Debemos elegir elementos de $L$ tal que la unión de todos los elementos de como resultado $S$

## Partición

Debido a que no permitimos solapamiento, entonces utilizaremos una igualdad para restringir el modelo

$$
\sum_{i:S_j \in L_i} Y_{L_i} = 1
$$

En otras palabras, además de las restricción de unión mencionada anteriormente, la intersección de todos los subconjuntos de $L$ elegidos debe ser el conjunto vacío

## Packing

Ahora, en lugar de usar constantes para las restricciones, plantearemos variables bivalentes que indican la selección de cada elemento de $S$.

$$
\sum_{i:S_j \in L_i} Y_{L_i} = Y_{S_j}
$$

Luego, vamos a maximizar la suma de estas variables bivalentes.

$$
Z_{\max} = \sum_{i}Y_{S_i}
$$

Si queremos, además, favorecer la solución que minimice la cantidad de elementos de $L$ tomados, entonces

$$
Z_{\max} = \sum_{i}Y_{S_i} - m\Big(\sum_jY_{L_j}\Big)
$$

con $m$ suficientemente chico como para que el modelo favorezca un elemento de $S$ por cualquier cantidad de elementos de $L$