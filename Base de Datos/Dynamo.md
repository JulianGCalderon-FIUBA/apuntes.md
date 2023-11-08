Dynamo es el *key-value store* de Amazon. Está diseñado siguiendo una arquitectura orientada a servicio *(SoA)*, la base de datos está distribuida en un *server cluster* que posee servidores web, routers de agregación, y nodos de procesamiento *(Dynamo instances)*.

Fue originalmente creado por Amazon como un SGDB distribuido para gestionar su sitio de comercio electrónico. Luego ha servido de base para la construcción de **Dynamo DB** disponible a través de AWS, la plataforma de *cloud computing* de Amazon.

En Dynamo, los datos deben estar estructurados de manera que las búsquedas sean siempre por clave.

Utiliza el método de *lookup* denominado [[Lookup#Hashing Consistente|Hashing Consistente]], que reduce la cantidad de movimientos de pares necesarios cuando cambia la cantidad de nodos $S$. Esto hace que sea más sencillo agregar nodos de forma dinámica, con impacto mínimo.

Es totalmente descentralizado, los nodos son pares entre sí. Esto implica que carece de un punto único de falla.

## Consistencia

Utiliza el modelo de consistencia denominado [[Consistencia#Consistencia Eventual|Consistencia Eventual]], que permite que las actualizaciones se propaguen a las réplicas de forma asincrónica.

Gracias a esto, las lecturas y escrituras pueden devolver el control rápidamente:

- Cuando un nodo recibe un *put* sobre una clave, no necesita propagarlo a las réplicas antes de confirmar la escritura.
- Dado que las operaciones de *get* pueden realizarse sobre cualquier réplica, es posible leer un valor no actualizado.

> [!note] Nota
> Cualquier nodo del listado de preferencias de una clave es elegible para una operación de *put* o *get*.

Se definen dos parámetros adicionales:

- $W \leq N$: Quorum de escritura. Un nodo puede devolver un resultado de escritura exitosa luego de recibir la confirmación de escritura de otros $W-1$ nodos del listado de preferencia. $W=2$ ofrece un nivel de replicación mínimo.
- $R \leq N$: Quorum de lectura. Un nodo puede devolver el valor de una clave leída luego de disponer de la lectura de $R$ nodos distintos (incluido el mismo). En muchas situaciones, $R=1$ es suficiente. Valores mayores de $R$ brindan tolerancia a fallas como corrupción de datos o ataque externos, pero hacen más lenta la lectura.

Para mantener sincronizadas las réplicas, Dynamo utiliza una estructura llamada **Merkle tree** que consiste en un árbol en que cada nodo no-hoja es un *hash criptografico* de los valores de sus hijos.
