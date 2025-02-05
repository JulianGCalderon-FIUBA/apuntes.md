Es una plataforma de Google para almacenamiento distribuido, pero también un concepto el cual inspira otras bases de datos distribuidas.

La unidad de almacenamiento básica son pares clave-datos. Los datos son en realidad, un conjunto de valores (columnas).

Los datos pueden ser de tipo *sparse*, donde hay muchos datos nulos, por lo que se optimiza el almacenamiento para este caso. Estos datos no tienen un orden definido, sino que conocen su "column family".

Un tablet es un conjunto de filas consecutivas, de acuerdo a la clave. Es la unidad de balanceo de Big Table, lo que permite escalar el sistema.

Este modelo tiene algunas ventajas:

- Las operaciones son atómicas por clave.
- Se aprovecha el principio de lcoalidad de datos, para ahcer lecturas por rangos de claves de forma rápida.

## Jerarquía

El almacenamiento es similar al de un árbol B+, la unidad de almacenamiento base es una tablet. En solo tres niveles, se puede tener una gran cantidad de información.

![[Big Table 1738715853.png]]

La velocidad es constante, y está optimizada para bases de datos muy grandes.

## Arquitectura

![[Big Table 1738715974.png]]

Las operaciones de metadata se envían a un **Big Table Master**. Estas operaciones implican comunicarse con las tablets, y lockear tables o porciones de tablets, utilizando un servidor de llaves **chubby**.

A diferencia de Hadoop, y debido a la estructura de árbol, a veces es necesario rebalancear las tablets. Las tablets se dividen en dos, y pueden ser almacenados en servidores distintos.
