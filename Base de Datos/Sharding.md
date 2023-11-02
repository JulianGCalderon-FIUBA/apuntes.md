Es el modelo distribuido de procesamiento utilizado por [[MondoDB]].

Se basa en el particionamiento horizontal de las colecciones en **chunks**, que se distribuyen en nodos denominados **shards** o fragmentos. Cada uno de estos contendrá un subconjunto de los documentos en cada colección.

Un **sharding cluster** de MongoDB está formado por distintos tipos de nodos de ejecución:

- Los *shards (fragmentos)* son los nodos en los que se distribuyen los *chunks* de las colección. Cada *shard* corre un proceso denominado `mongod`.
- Los *routers* son los nodos servidores que reciben las consultas desde las aplicaciones clientes, y las resuelven comunicandose con los *shards*. Corren un proceso denominado `mongos`.
- Los *servidores de configuración* son los que almacenan la configuración de los routers y lo