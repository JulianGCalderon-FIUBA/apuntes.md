Paxos es un protocolo/familia de protocolos que resuelven consenso en una red no confiable, o donde se pueden producir [[Generales Bizantinos|fallas bizantinas]]. Hay muchas variantes del algoritmo.

El algoritmo progresó siempre que la mayoría estén funcionando correctamente, por lo que la fórmula de consenso es: $N >= 2f + 1$.

El consenso obtenido será eventualmente conocido por todos, y las en

## Arquitectura

El **cliente** del sistema envía un request al algoritmo:

- Puede ser rechazado. Este es el flujo esperado del algoritmo.
- Se puede reintentar tantas veces como desea.
- Los eventos se almacenan en un orden consistente.

Los **proposers** reciben requests de clientes y comienzan el protocolo.

- Se debe elegir un líder para evitar *starvation*.
- Mantienen un identificador incremental para cada propuesta.

Los **acceptors** reciben propuestas de proposers y deben consensar los valores asociados a las propuestas.

- Mantienen el estado del protocolo en un almacenamiento estable.
- Se llega al quorum si la mayoría están funcionando de forma correcta.

Los **learners** ejecutan las consultas cuando se llega a un consenso, y dan la respuesta al cliente.

![[Paxos 1738625508.png]]

## Funcionamiento

El protocolo está dividido en dos fases principales:

### Fase 0

El cliente envía una propuesta al proposer.

![[Paxos 1738626189.png]]

### Fase 1

Se divide en dos subfases:

- **Prepare**
- **Promise**

En la subfase de **prepare**, el proposer envía la propuesta a los acceptors, y espera a recibir el quorum. Este es el mensaje `prepare(N)`.

![[Paxos 1738626210.png]]

En la subfase de **promise**, si los acceptors no habían prometido nada previamente, prometen no aceptar ninguna otra request con un identificador menor al recibido

- Responden al proposer con un mensaje de `promise(N', v')` que contiene al `N'` y `v'` de una etapa previa.
- No responden si llega una propuesta con `N < N'`.

![[Paxos 1738626338.png]]

Si no se llega al consenso, el valor previo de la promesa se utiliza para volver a proponer un pedido. De esta forma, es tolerante a fallos ante la caída de un acceptor.

### Fase 2

Se divide en dos subfases:

- **Propose**
- **Accept**

En la subfase de **propose**, si el proposer recibe promesas de la mayoría, entonces:

- Envía las propuestas a los acceptors.
- Rechazá todas las consultas son un identificador menor a `N`.

![[Paxos 1738626350.png]]

En la subfase de **accept**, si la promesa es mantenida, se anuncia el nuevo valor `v`:

- Envian un mensaje de `accept(N, v)` a todos los learners y al proposer inicial.
- No envían `accept` si un mensaje con un identificador superior fue recibido.

![[Paxos 1738626363.png]]

El learner le responde al cliente y se toman acciones respecto al valor acordado:

![[Paxos 1738627421.png]]
