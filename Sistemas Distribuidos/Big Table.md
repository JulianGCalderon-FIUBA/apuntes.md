Es una plataforma de Google para almacenamiento distribuido, pero también un concepto el cual inspira otras bases de datos distribuidas.

Los datos se almacenan en tablas, que son mapas ordenados clave-valor. Cada clave representa una fila, y el valor representa los atributos de dicha fila (el valor para cada columna).

Las columnas son agrupadas en un "column family", y diferenciadas dentro de cada famlia por un "column qualifier".

Las tablas son *sparse*, es decir, si una columna no se utiliza en un rango de valores, no ocupa espacio.

Cada celda guarda múltiples valores, permitiendo versionado de los datos. Además, guarda un timestamp $t$.

![[Big Table 1739319381.png]]

Un tablet es un conjunto de filas consecutivas de una tabla, de acuerdo a la clave. Es la unidad de balanceo de Big Table, lo que permite escalar el sistema.

Este modelo tiene algunas ventajas:

- Las operaciones son atómicas por clave.
- Se aprovecha el principio de localidad de datos, para hacer lecturas por rangos de claves de forma rápida.

Por otro lado, tiene las siguientes restricciones:

- Es imposible crear índices, ya que está indexado en base a la clave.
- Es imposible crear contextos de transacciones *cross-keys*.

## Jerarquía

El almacenamiento es similar al de un árbol B+, la unidad de almacenamiento base es una tablet. En solo tres niveles, se puede tener una gran cantidad de información.

![[Big Table 1738715853.png]]

La velocidad es constante indiferente de la cantidad de datos, y está optimizada para bases de datos muy grandes.

## Arquitectura

![[Big Table 1738715974.png]]

Las operaciones de metadata se envían a un **Big Table Master**. Estas operaciones implican comunicarse con las tablets, y lockear tables o porciones de tablets, utilizando un servidor de llaves **chubby**.

A diferencia de Hadoop, y debido a la estructura de árbol, a veces es necesario rebalancear las tablets. Las tablets se dividen en dos, y pueden ser almacenados en servidores distintos, dividiendo el trabajo.

Es posible que la división de tablets no sea exitosa, y que todas las siguientes consultas vayan a una sola de las particiones. Este es el peor caso, y se busca evitar.
