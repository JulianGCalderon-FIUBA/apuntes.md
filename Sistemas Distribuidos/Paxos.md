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
- Mantienen un identificador incremental para las propuestas.

Los **acceptors** deben consensar los valores asociados a las propuestas.

- Se llega al quorum si la mayoría están funcionando de forma correcta.
- Se debe conocer la cantidad de acceptors que hay en el sistema

Los **learners** ejecutan las consultas cuando se llega a un consenso.

## Funcionamiento

El protocolo está dividido en dos fases principales:

- **Fase 1**
	- **Prepare**
	- **Promise**
- **Fase 2**
	- **Propose**
	- **Accept**

### Prepare

El proposer envía un mensaje de `PREPARE IDp` a todos los acceptors (o la mayoría).

El identificador del pedido debe ser único e incremental. Estos se pueden particionar, por ejemplo, un proposer utiliza identificadores pares, y el otro proposer identificadores impares.

![[Paxos 1738626210.png]]

### Promise

Los acceptors reciben el `PREPARE IDp`, y si no prometió ignorarlo, entonces promete ignorar todos los siguientes mensajes con un identificador menor al recibido. En este caso, responde con un mensaje de `PROMISE IDp`.

En caso de que ya haya prometido algo previamente, entonces en su lugar responde con un mensaje de `PROMISE IDp, IDa, Value`, donde `IDa` y `Value` corresponden a valores de un pedido previo.

![[Paxos 1738626338.png]]

### Propose

Si el proposer obtiene mayoría de promesas para un identificador determinado `IDp`, entonces envía `PROPOSE IDp, Value` a todos los acceptors (o la mayoría).

El valor a enviar es el asociado al mayor identificador de un pedido aceptado que tenga. En caso de que no tenga ninguno, puede utilizar el valor del pedido actual.

Esto permite que pedidos que fueron aceptados, pero que no llegaron a consenso por la caída de acceptors, se reintenten.

![[Paxos 1738626350.png]]

### Accept

Los acceptors reciben el mensaje `PROPOSE IDp, Value`, y si no prometió ignorarlo, entonces responde con `ACCEPT IDp, Value` al proposer, y a todos los learners.

![[Paxos 1738626363.png]]

Si la mayoría de los acceptors aceptan el valor `Value`, se llega a consenso sobre el valor. El consenso no necesariamente es sobre el identificador, ya que este es interno para el protocolo.

Si un proposer o learner recibe mayoría *accepts* sobre el valor `Value`, saben que se llegó al consenso sobre el valor.
