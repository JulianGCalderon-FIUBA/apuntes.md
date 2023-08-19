---
title: Principles of Reliable Data Transfer
---

La abstracción del servicio provista por las capas superiores es la de un canal viable de comunicación por la cual se puede transferir datos. Con este canal, ningún bit puede ser corrompido o perdido. Es la responsabilidad de un ***reliable data transfer protocol*** de implementar este servicio.

Asumiremos a lo largo de esta discusión que los paquetes serán recibidos en el orden que fueron enviados, con algunos posiblemente siendo perdidos. Por otro lado, únicamente consideraremos el caso de ***unidirectional data transfer***, si bien el caso ***bidireccional*** no es conceptualmente más difícil, es más tedioso de explicar.

## 1. Building a Reliable Data Transfer Protocol

### Reliable Data Transfer over a Perfectly Reliable Channel

El remitente simplemente acepta datos de la capa superior, crea un paquete conteniendo los datos y los envía a través del canal. Desde el lado del receptor, este recibe el paquete desde el canal subyacente, extrae los datos y se los envía a la capa superior.

Al ser un canal confiable, no hay necesidad de enviar al remitente del mensaje algún tipo feedback de que los datos llegaron correctamente.

### Reliable Data Transfer over a Channel with Bit Errors

Un modelo más realista es aquel que tienen en cuenta la corrupción de los bits en el envío del paquete. Un protocolo ***ARQ (Automatic Repeat reQuest)*** es aquel que utiliza tanto ***positive acknowledgments*** como ***negative acknowledgements.*** Tendremos tres características en estos tipos de protocolos.

- ***Error Detection:*** Principalmente, necesitaremos un mecanismo para que el receptor de un paquete pueda determinar si este fue recibido correctamente. Una posible implementación de esto sería la utilización de un nuevo campo en el paquete: ***checksum field***.
- ***Receiver Feedback***: El receptor deberá enviar ***positive (ACK)*** y ***negative (NAK) acknowledgements*** en respuesta a los paquetes recibidos para indicar que fueron recibidos correctamente.
- ***Retransmission:*** Un paquete que fue recibido de forma errónea tendrá que ser retransmitido.

El remitente sabrá cuál fue el último paquete transmitido y puede reenviarlo en caso de recibir un mensaje de NAK. Si recibe un ACK, este enviará el próximo paquete. En estos protocolos, denominados ***stop-and-wait***, no se envía mas información a través de la red hasta asegurarse que el último paquete haya sido enviado correctamente.

Aún no hemos tenido en cuenta la posibilidad de que los paquetes ACK o NAK estén corruptos. Por lo menos, necesitaremos agregar ***checksum bits*** a estos paquetes para detectar los errores.

- Una posible solución es la de tener un tercer mensaje de utilizado por el remitente para indicar que último mensaje que recibió fallo, pero esto puede entrar en un ciclo de mensajes fallidos. Este es un camino difícil.
- Otra alternativa podría ser la de agregar suficientes ***checksum*** bits como para permitir al remitente no solo detectar sino también recuperarse de los errores.
- Un último enfoque puede ser el de simplemente reenviar el último paquete si se recibió un mensaje de ***acknowledge*** corrupto. Este enfoque introduce un problema nuevo, el de los paquetes duplicados

Una simple solución a este último problema mencionado es el de agregar números de secuencia a los paquetes enviados. En el caso más simple de un protocolo ***stop-and-wait***, un campo de ***1 bit*** para el número de secuencia será suficiente (estos protocolos son conocidos como ***alternating-bit-protocol)***. Únicamente necesitamos saber si el paquete recibido es el mismo que el anterior, o único distinto.

Podríamos obtener el mismo efecto si en lugar de enviar NAK, enviamos un ACK por el último paquete recibido correctamente. (agregándole también un número de secuencia). Si el remitente recibe dos ACK por el mismo paquete, sabrá que tiene que reenviar el paquete fallido.

### Reliable Data Transfer over a Lossy Channel with Bit Errors

Supongamos que ahora, además de corrupción de bits, el canal subyacente puede perder paquetes (este no es un evento poco común en las redes de hoy en dia). Hay múltiples enfoques para lidiar con la pérdida de paquetes, nos centraremos en el que se enfoca en recuperar los paquetes perdidos desde el remitente.

Supongamos que el ***paquete*** de enviado o si ACK correspondiente se pierde. En cualquier caso, no habrá ninguna respuesta de confirmación arribando al remitente. Si el remitente está dispuesto a esperar lo suficiente como para asegurarse que el paquete se perdió, entonces puede reenviarlo.

El remitente debe reenviar el paquete lo más pronto posible, para asegurarse que el ***delay*** por la pérdida de paquetes sea lo menor posible. Usualmente, se toma un tiempo de espera tal que el paquete es probable que se haya perdido, aunque sin garantías. Esta técnica introduce la posibilidad de paquetes duplicados, pero podemos solucionarlas utilizando lo visto en anteriormente.

Implementar un mecanismo de retransmisión requiere de un ***countdown timer***. El remitente deberá poder iniciar un ***timer*** con cada paquete enviado, responder a un ***timer interrupt***, y frenar un el ***timer***.

## 2. Pipelined Reliable Data Transfer Protocols

La solución presentada anteriormente tiene un problema fundamental, su desempeño es muy bajo debido al protocolo ***stop-and-wait***. Si definimos ***utilization*** del remitente como la fracción de tiempo en la que está ocupado enviando bits a través del canal.

La solución a este problema es simple, en lugar de operar en un protocolo ***stop-and-wait***, debemos permitir que el remitente envíe múltiples paquetes sin esperar a sus ***acknowledgements***. Esta técnica se conoce como ***pipelining,*** tiene las siguientes consecuencias:

- El rango de números de secuencia debe incrementarse, ya que puede haber múltiples paquetes en tránsito sin haber recibido su ***acknowledgment***.
- Tanto el emisor deberá ***bufferear*** los paquetes que aun no fueron confirmados. Esto también es necesario del lado del receptor.
- El rango de números de secuencia y los requerimientos del buffer dependerán de la forma en la que el protocolo responden a los paquetes perdidos. Existen dos enfoques principales: ***Go-Back-N*** y ***Selective Repeat***.

## 3. Go-Back-N (GBN)

Este protocolo consiste en permitir que el remitente tenga un número máximo de $n$ de paquetes sin confirmación en el ***pipeline***. Este número suele ser denominado ***window size***, y el protocolo como ***sliding-window protocol***. Este número es limitado debido a que el campo del ***header*** tiene un tamaño fijo. TCP tiene un campo para el número de secuencia de 32 bits, pero cuenta los ***bytes*** en el ***byte stream*** en lugar de los paquetes.

Un ***GBN sender*** debe responder a tres tipos de eventos:

- ***Invocation from above:*** Cuando se trata de enviar un paquete, el remitente debe primero verificar que la ventana no está completa, si no lo está entonces se actualizan los valores y se envía el paquete a través del canal subyacente. Si la ventana está completa, usualmente se ***bufferea*** el paquete para enviarlo posteriormente. Si aún no hay paquetes enviándose, entonces se inicia el ***timer***.
- ***Receipt of an ACK:*** Cuando llega un ACK del paquete con número de secuencia $n$, entonces se toma como un ***cumulative acknowledgment***, indicando que todo los paquetes hasta ese número de secuencia (incluido) fueron entregados correctamente. En esta punto se mueve la base de la ventana. Si no quedan paquetes por recibir, entonces se frena el ***timer***.
- ***A timeout Event:*** Cuando ocurre un ***timeout***, entonces todos los paquetes que aún no fueron confirmados serán reenviados.

Desde el lado del receptor, es simple. Si un paquete con número de secuencia $n$ es recibido correctamente y en orden, entonces este envía un ACK para el paquete $n$, y le entrega la porción de datos a la entrada superior. En otro caso, se envía un ACK con el último paquete recibido y se descarta la información.

Como todos los datos deben ser entregados en orden, un receptor podría guardar los paquetes correctos que están fuera de orden,pero esto es innecesario ya que en la implementación actual el remitente reenvía todos los mensajes a partir del que se perdió. Este enfoque tiene la ventaja de ser simple ya que el receptor no debe guardar los paquetes recibidos, únicamente el del último paquete recibido en orden.

La implementación de este protocolo usualmente utiliza ***event-based programming***, ya que los distintos procedimientos son invocados según el resultado de distintos eventos asincrónicos.

## 4. Selective Repeat (SR)

El protocolo GBN tiene la desventaja de que en redes con ***mucho delay***, pueden llegar a retransmitirse un gran número de paquetes de forma innecesaria. Como su nombre sugiere, estos protocolos consisten en selectivamente repetir únicamente aquellos paquetes que se perdieron. Se utiliza una ventana de tamaño $n$ tanto para el receptor como para el remitente.

Un receptor debe confirmar todos los paquetes que recibe ya sea en orden o no, aquellos paquetes fuera de orden deberán ser guardados para ser entregados a la capa superior en cuanto reciba los paquetes faltantes.

Un ***SR sender*** debe responder a tres tipos de eventos:

- **Invocation from above:** Cuando se trata de enviar un paquete, el remitente debe primero verificar que la ventana no está completa, si no lo está entonces se actualizan los valores y se envía el paquete a través del canal subyacente. Si la ventana está completa, usualmente se ***bufferea*** el paquete para enviarlo posteriormente.
- ***Receipt of an ACK:*** Cuando llega un ACK del paquete con número de secuencia $n$, entonces se marca es paquete como confirmado. Si el número de paquete coincide con la base, entonces esta se avanza hasta el siguiente paquete sin confirmación. Al moverse la ventana, se envían los paquetes que habían sido previamente guardados.
- ***A timeout event:*** Cada paquete deberá tener su propio ***timer,*** por lo que el paquete correspondiente al evento será reenviado.

Si un RC receiver recibe un ***paquete*** que se encuentra dentro de su ventana, entonces se envía un ACK y se almacena (en caso de no haberlo recibido previamente). Si el número de paquete coincide con la base, entonces este paquete y los consecuentes (si ya fueron recibidos) se envían a la capa superior. La ventana se avanza hasta el primer número de secuencia que aún no fue recibido.

Si el paquete recibido no pertenece a la ventana, entonces se genera un ACK aunque este paquete ya haya sido confirmado (y entregado a la capa superior). En cualquier otro caso, se ignora el paquete.

Es importante notar que el remitente y el receptor no tendrán una vista idéntica de lo que fue recibido y lo que no. Las ventanas de cada uno no siempre coincidirán. Esta falta se sincronización tendrá importantes consecuencias cuando nos enfrentamos con el rango finito de números de secuencia. Para el receptor no hay forma de distinguir entre la retransmisión de un paquete y la original transmisión de un paquete (si sus números de secuencia coinciden). Para solucionar esto, se necesitara un tamaño de ventana de a lo sumo la mitad del espacio de los números de secuencia.

Para este análisis, asumimos que los paquetes llegan (o se pierden) en el orden que fueron enviados. Esto es razonable si los hosts están conectados a través de un único cable fisico. Cuando el canal que los une es una red, puede ocurrir ***packet reordering***. Este implica que ACK con un número de secuencia puede llegar cuando este ya no se encuentra en la ventana del receptor ni del emisor. El enfoque tomado en la práctica es asegurarse de no reutilizar un número de secuencia hasta que el remitente se asegure que cualquier otro paquete con ese mismo número de secuencia ya no esté en la red. Un tiempo de vida máximo de tres minutos se asume para las extensiones TCP en redes de alta velocidad.
