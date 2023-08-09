La factorización LU consiste en en descomponer la matriz en dos matrices diagonales, por lo que su resolución sera simple.

$$
Ax = LUx = L(Ux) = b
$$

La complejidad de la solución sera de $O(n^2)$

## Paso 1

El primer paso consiste en encontrar la primer fila de $u$, a partir de la multiplicación de la primer fila de $L$ con las columnas de $U$

$$
u_{1j} = a_{1j}
$$

Luego, buscamos la primer columna de $l$, a partir de la multiplicacion de las filas de $L$ con la primer columna de $U$

$$
l_{j1}= \frac{a_{j1}}{u_{11}}
$$

## Paso 2

Aplicamos el paso 3 y 4 sucesivamente, para $i = 2, \cdots, n{-}1$

## Pase 3

Obtenemos $u_{ii}$ a partir de multiplicar la fila $i$ de $L$ con la columna $i$ de $U$

$$
u_{ii} = a_{ii} - \sum_{k=1}^{i-1} l_{ik}u_{kj}
$$

## Paso 4

Buscamos la $i$-esima fila de $U$, y la $i$-esima columna de $V$

$$
u_{ij} = a_{ij} - \sum_{k=1}^{i-1} l_{ik} u_{kj}
$$

$$
l_{ji} = \frac{1}{u_{ii}}\Big[a_{ji} - \sum_{k=1}^{i-1} l_{jk} u_{ki}\Big]
$$
