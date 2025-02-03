Paxos es un protocolo/familia de protocolos que resuelven consenso en una red no confiable, o donde se pueden producir [[Generales Bizantinos|fallas bizantinas]].

El algoritmo progresó siempre que la mayoría estén funcionando correctamente, por lo que: $N >= 2f + 1$.

## Arquitectura

El **cliente** del sistema envía un request al algoritmo:

- Puede ser rechazado. Este es el flujo esperado del algoritmo.
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

### Fase 0

El cliente envía una propuesta al proposer.

![[Paxos 1738626189.png]]

### Fase 1a - Prepare

El proposer envía la propuesta a los acceptors, esperando una respuesta. Este pedido tiene un número identificador: `Prepare(N)`.

![[Paxos 1738626210.png]]

### Fase 1b - Promise

Los acceptors responden con una promesa de que no aceptaran ningún otro pedido con un identificador menor al recibido: `Promise(N, v)`.

### Fase 2a - Propose

Si recibe promesas de la mayoría, el proposer rechazará todos los requests con un identificador menor, y envía la propuesta `Propose(N, v)`.

### Fase 2b - Accept

Si la promesa es mantenida, se anuncia el nuevo valor `v`, y envia `Accept(N, v)` a todos los learners y al proposer inicial.
