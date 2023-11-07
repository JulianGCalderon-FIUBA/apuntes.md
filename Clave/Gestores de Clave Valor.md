Almacenan vectores asociativos o diccionarios, es decir, conjuntos formados por pares de elementos de la forma `(clave, valor)`.

Las claves son únicas, y el único requisito sobre su dominio es que sea comparable por igual. Algunos ejemplos son:

- **Berkeley DB**
- **Dynamo**
- **Redis**

Este tipo de bases de datos tiene cuatro operaciones elementales:

- Insertar un nuevo par: `put`
- Eliminar un par existente: `delete`
- Actualizar el valor de un par: `update`
- Encontrar un par asociado a una clave particular: `get`

Sus ventajas son:

- **Simplicidad**
	- No se define un esquema, [[Lenguajes#Data-Definition Language|DDL]], restricciones de integridad, ni dominios.
	- El agregado es mínimo, y está limitado al par.
	- El objetivo es guardar y consultar grandes cantidades de datos, pero no de interrelaciones entre los datos.
- **Velocidad:** Ya que prioriza la eficiencia de acceso, por sobre la integridad de los datos.
- **Escalabilidad:** Generalmente, proveen replicación (ya sea maestro-esclavo o distribuida), y permiten repartir las consultas entre los nodos.

## Dynamo

Dynamo es el *key-value store* de Amazon. Está diseñado siguiendo una arquitectura orientada a servicio, la base de datos está distribuida en un *server cluster* que posee servidores web, routers de agregación, y nodos de procesamiento.

Utiliza un método de [[Búsqueda]] denominado [[Hashing Consistente]] que reduce la cantidad de movimientos de pares necesarios cuando cambia la cantidad de nodos $S$.

Es totalmente descentralizado, los nodos son pares entre sí. Esto implica que carece de un punto único de falla.

Utiliza un modelo de [[Consistencia]] denominado [[Consistencia#Consistencia Eventual|Consistencia Eventual]], que tolera pequeñas inconsistencias en los valores almacenados en distintas réplicas.

Gracias a esto, las lecturas y escrituras pueden devolver el control rápidamente. Cuando un nodo recibe un *put* sobre una clave, no necesita propagarlo a las réplicas antes de confirmar la escritura. Dado que las operaciones de *get* pueden realizarse sobre cualquier réplica, es posible leer un valor no actualizado.

Se definen dos parámetros adicionales:

- $W \leq N$: Quorum de escritura. Un nodo puede devolver un resultado de escritura exitosa luego de recibir la confirmación de escritura de otros $W-1$ nodos del listado de preferencia.
- $R \leq N$: Quorum de lectura. Un nodo puede devolver el valor de una clave leída luego de disponer de la lectura de $R$ nodos distintos (incluido el mismo).

Para mantener sincronizadas las réplicas, *Dynamo* utiliza una estructura llamada **Merkle Tree** que consiste en un árbol en que cada nodo no-hoja es un hash criptográfico de los valores de sus hijos.

Dynamo fue originalmente creado por Amazon como un SGDB distriuido para gestionar su sitio de comercio electronico. Luego ha servido de base para la construcción de **Dynamo DB** dispoinible a través de AWS, la plataforma de *cloud computing* de Amazon.

En Dynamo, los datos deben estar estructurados de manera que las búsquedas sean siempre por clave.

Una forma de simular la estructura de tabla de los gestores relacionaales es utilizando pares (clave, valor) con la siguiente estructura
