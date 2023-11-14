En 1998, el científico E. Brewer postuló la imposibilidad de que un sistema de bases de datos distribuido garantice simultáneamente el máximo nivel de:

- **(C)** Consistencia *(consistency)*
- **(A)** Disponibilidad *(availability)*
- **(P)** Tolerancia a particiones *(partition tolerance)*

La [[Consistencia]] es la propiedad de que en un instante determinado, el sistema muestre un único valor de cada ítem de datos a los usuarios. Su nivel máximo es la consistencia secuencial.

La **disponibilidad** consiste en que toda consulta que llega a un nodo del sistema distribuido que no está caído reciba una respuesta efectiva.

La **tolerancia a particiones** consiste en que el sistema pueda responder una consulta aún cuando algunas conexiones entre algunos pares de nodos estén caídas.

Solo podemos elegir tres de estas propiedades.
