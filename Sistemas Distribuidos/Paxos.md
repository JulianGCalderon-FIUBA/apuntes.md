Paxos es un protocolo/familia de protocolos que resuelven consenso en una red no confiable, o donde se pueden producir [[Generales Bizantinos|fallas bizantinas]]. Hay muchas variantes del algoritmo.

El algoritmo progresó siempre que la mayoría estén funcionando correctamente, por lo que la fórmula de consenso es: $N >= 2f + 1$.

El consenso obtenido será eventualmente conocido por todos, y las entidades buscarán acordar cualquier valor, independiente de quien lo propuso. Una vez obtenido el consenso, no se puede cambiar.

El algoritmo funciona sobre la base de que los pedidos pueden ser rechazados, y es el flujo típico. Los clientes pueden reintentar consultas tantas veces como se desea.

## Arquitectura

El sistema consiste en los siguientes actores:

- **Proposer**: proponen valores al algoritmo.
- **Acceptor**: trabajan en obtener consenso.
- **Learner**: aprenden al valor consensuado.

Además, se requiere que los nodos deben ser persistentes.

![[Paxos 1738625508.png]]

Los **proposers** son los que comienzan el protocolo.

- Se debe elegir un líder para evitar *starvation*.
- Mantienen un identificador incremental para las propuestas. Estos deben ser únicos, por lo que una solución se particionarlos (por ejemplo, un proposer utiliza identificadores pares, y otro identificadores impares).

Los **acceptors** deben consensar los valores asociados a las propuestas.

- Se llega al quorum si la mayoría están funcionando de forma correcta.
- Se debe conocer la cantidad de acceptors que hay en el sistema

Los **learners** ejecutan las consultas cuando se llega a un consenso.

## Funcionamiento

El protocolo está dividido en dos fases principales:

### Prepare

En la fase de **prepare**, el proposer envía la propuesta a los acceptors, y espera a recibir el quorum. Este es el mensaje `prepare(N)`.

![[Paxos 1738626210.png]]

En la sub fase de **promise**, si los acceptors no habían prometido nada previamente, prometen no aceptar ninguna otra request con un identificador menor al recibido

- Responden al proposer con un mensaje de `promise(N', v')` que contiene al `N'` y `v'` de una etapa previa.
- No responden si llega una propuesta con `N < N'`.

![[Paxos 1738626338.png]]

Si no se llega al consenso, el valor previo de la promesa se utiliza para volver a proponer un pedido. De esta forma, es tolerante a fallos ante la caída de un acceptor.

### Fase 2

Se divide en dos sub fases:

- **Propose**
- **Accept**

En la sub fase de **propose**, si el proposer recibe promesas de la mayoría, entonces:

- Envía las propuestas a los acceptors.
- Rechaza todas las consultas son un identificador menor a `N`.

![[Paxos 1738626350.png]]

En la sub fase de **accept**, si la promesa es mantenida, se anuncia el nuevo valor `v`:

- Envían un mensaje de `accept(N, v)` a todos los learners y al proposer inicial.
- No envían `accept` si un mensaje con un identificador superior fue recibido.

![[Paxos 1738626363.png]]

El learner le responde al cliente y se toman acciones respecto al valor acordado:

![[Paxos 1738627421.png]]
