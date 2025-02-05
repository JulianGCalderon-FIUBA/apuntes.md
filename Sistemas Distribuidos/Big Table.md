Es una plataforma de Google para almacenamiento distribuido, pero también un concepto el cual inspira otras bases de datos distribuidas.

La unidad de almacenamiento básica son pares clave-datos. Los datos son en realidad, un conjunto de valores (columnas).

Los datos pueden ser de tipo *sparse*, donde hay muchos datos nulos, por lo que se optimiza el almacenamiento para este caso. Estos datos no tienen un orden definido, sino que conocen su "column family".

Un tablet es un conjunto de filas consecutivas, de acuerdo a la clave. Es la unidad de balanceo de Big Table, lo que permite escalar el sistema.

## Jerarquía

El almacenamiento es similar al de un árbol B+, la unidad de almacenamiento base es una tablet. En solo tres niveles, se puede tener una gran cantidad de información.

![[Big Table 1738715853.png]]

La velocidad es constante, y esta optimizada para bases de datos muy grandes.

## Arquitectura


