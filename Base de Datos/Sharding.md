Es el modelo distribuido de procesamiento utilizado por [[MondoDB]].

Se basa en el particionamiento horizontal de las colecciones en **chunks**, que se distribuyen en nodos denominados **shards** o fragmentos. Cada uno de estos contendrá un subconjunto de los documentos en cada colección.

Un **sharding cluster** de MongoDB está formado por distintos tipos de nodos de ejecución:

- Los **shards** (fragmentos) son los nodos en los que se distribuyen los *chunks* de la colección. Cada *shard* corre un proceso denominado `mongod`.
- Los **routers** son los nodos servidores que reciben las consultas desde las aplicaciones clientes, y las resuelven comunicándose con los shards. Corren un proceso denominado `mongos`.
- Los **servidores de configuración** son los que almacenan la configuración de los routers y los shards.

![[Sharding 1698894023.png|475]]

El participando de las colecciones se realiza a partir de un *shard key*. La *shard key* es un atributo o conjunto de atributos de la colección que se escoge al momento de construir el *shared cluster*.

La asignación de documentos a shards se hace dividiendo en rangos los valores de la clave del *shard* conocido como *range-based sharding*, o bien a partir de una función de hash aplicada sobre su valor *(hashed sharding)*.

En un contexto de *sharding* es posible tener algunas colecciones *sharded* (fragmentadas) y otras *unshared* (no fragmentadas). Las colecciones no fragmentadas de una base de datos se almacenarán en un fragmento particular del cluster, que será el *shard primario* para esa base de datos.
