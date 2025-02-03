Paxos es un protocolo/familia de protocolos que resuelven consenso en una red no confiable, o donde se pueden producir [[Generales Bizantinos|fallas bizantinas]].

El algoritmo progresó siempre que la mayoría estén funcionando correctamente, por lo que: $N >= 2f + 1$.

## Arquitectura

El **cliente** del sistema envía un request a la red (la cual funciona utilizando Paxos), este pedido:

- Puede ser rechazado.
- Se puede reintentar tantas veces como desea.

Los **proposers** reciben requests de clientes y comienzan el protocolo.

- Se debe elegir un líder para evitar *starvation*.

Los **acceptors** reciben propuestas de **proposers** y deben consensar los valores asociados a las propuestas.

- Mantienen el estado del protocolo en un almacenamiento estable.

El objetivo del sistema es que todos los **acceptors** consensuen un valor $v$ asociado a una propuesta realizada por un **proposer**:
