Dynamo es el *key-value store* de Amazon. Está diseñado siguiendo una arquitectura orientada a servicio *(SoA)*, la base de datos está distribuida en un *server cluster* que posee servidores web, routers de agregación, y nodos de procesamiento *(Dynamo instances)*.

Dynamo fue originalmente creado por Amazon como un SGDB distribuido para gestionar su sitio de comercio electrónico. Luego ha servido de base para la construcción de **Dynamo DB** disponible a través de AWS, la plataforma de *cloud computing* de Amazon.

Utiliza el método de *lookup* denominado [[Lookup#Hashing Consistente|Hashing Consistente]], que reduce la cantidad de movimientos de pares necesarios cuando cambia la cantidad de nodos $S$. Esto hace que sea más sencillo agregar nodos de forma dinámica, con impacto mínimo.

Es totalmente descentralizado, los nodos son pares entre sí. Esto implica que carece de un punto único de falla.

## Consistencia

Utiliza el modelo de consistencia denominado [[Consistencia#Consistencia Eventual|Consistencia Eventual]], que tolera pequeñas inconsistencias en los valores almacenados en distintas réplicas.

Gracias a esto, las lecturas y escrituras pueden devolver el control rápidamente. Cuando un nodo recibe un *put* sobre una clave, no necesita propagarlo a las réplicas antes de confirmar la escritura. Dado que las operaciones de *get* pueden realizarse sobre cualquier réplica, es posible leer un valor no actualizado.

Se definen dos parámetros adicionales:

- $W \leq N$: Quorum de escritura. Un nodo puede devolver un resultado de escritura exitosa luego de recibir la confirmación de escritura de otros $W-1$ nodos del listado de preferencia.
- $R \leq N$: Quorum de lectura. Un nodo puede devolver el valor de una clave leída luego de disponer de la lectura de $R$ nodos distintos (incluido el mismo).
