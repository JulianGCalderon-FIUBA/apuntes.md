En 1998, el científico E. Brewer postuló la imposibilidad de que un sistema de bases de datos distribuido garantice simultáneamente el máximo nivel de:

- **(C)** Consistencia *(consistency)*
- **(A)** Disponibilidad *(availability)*
- **(P)** Tolerancia a particiones *(partition tolerance)*

La [[Consistencia]] es la propiedad de que, en un instante determinado, el sistema muestre un único valor de cada ítem de datos a los usuarios. Su nivel máximo es la consistencia secuencial.

La **disponibilidad** consiste en que toda consulta que llega a un nodo del sistema distribuido que no está caído reciba una respuesta efectiva.

La **tolerancia a particiones** consiste en que el sistema pueda responder una consulta aun cuando algunas conexiones entre algunos pares de nodos estén caídas.

El teorema CAP dice entonces que a lo sumo podemos ofrecer dos de las tres garantías:

- **AP:** Si la red está particionada, podemos optar por seguir respondiendo consulta aun cuando algunos nodos no responden. La consistencia no es máxima.
- **CP:** Con la red particionada, si queremos garantizar consistencia máxima, no podremos garantizar disponibilidad. Es posible que no podamos responder una consulta, ya que esperamos un mensaje de confirmación desde nodos que no pueden comunicarse.
- **CA:** Si queremos consistencia y disponibilidad, entonces no podremos tolerar que una cantidad indeterminada de enlaces se caiga.

Debido a que no podremos garantizar que una red no se particióne, el sistema deberá necesariamente ser tolerante a particiones. En el campo específico de la ejecución de transacciones, estas limitaciones llevaron a la definición de garantías más débiles que las [[Transacción#Propiedades ACID|propiedades ACID]].

## Propiedades BASE

Las propiedades BASE representan un sistema distribuido con:

- **(BA)** Disponibilidad básica *(basic availability)*: El gestor distribuido está siempre en funcionamiento, aunque eventualmente puede devolvernos un error, o un valor desactualizado.
- **(S)** Estado débil *(soft state)*: No es necesario que todos los nodos réplica guarden el mismo valor de un ítem en un determinado instante. No existe entonces un "estado actual de la base de datos".
- **(E)** Consistencia eventual *(eventual consistency)*: Si dejaran de producirse actualizaciones, eventualmente todos los nodos réplica alcanzarían el mismo estado.
