Paxos es un protocolo/familia de protocolos que resuelven consenso en una red no confiable, o donde se pueden producir [[Generales Bizantinos|fallas bizantinas]].

El algoritmo progresó siempre que la mayoría estén funcionando correctamente, por lo que: $N >= 2f + 1$.

## Arquitectura

El **cliente** del sistema envía un request a la red (la cual funciona utilizando Paxos), este pedido:

- Puede ser rechazado.
- Se puede reintentar tantas veces como desea.

Los **proposers** reciben requests de clientes y comienzan el protocolo.

- Se debe elegir un líder para evitar *starvation*.
- Mantienen un identificador incremental para cada propuesta.

Los **acceptors** reciben propuestas de proposers y deben consensar los valores asociados a las propuestas.

- Mantienen el estado del protocolo en un almacenamiento estable.
- Se llega al quorum si la mayoría están funcionando de forma correcta.

Los **learners** ejecutan las consultas cuando se llega a un consenso, y dan la respuesta al cliente.

![[Paxos 1738625508.png]]

## Funcionamiento

El protocolo está dividido en fases.

- Fase 0: El cliente envia una propuesta a un proposer.
- Fase 1a: El proposer envía la propuesta a los acceptors, esperando una respuesta.
- Fase 1b: Los acceptors responden con una promesa de que no aceptaran ningun
