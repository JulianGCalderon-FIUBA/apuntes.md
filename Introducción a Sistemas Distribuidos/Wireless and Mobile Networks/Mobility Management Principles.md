Primero, consideraremos las distintas dimensiones de la movilidad, con cierto grado de detalle:

- ***From the network layer's standpoint, how mobile is a user?*** Un usuario móvil presenta distintos desafíos para la capa de red. Si un usuario se mueve a lo largo del edificio, entonces no es móvil para la capa de red. Incluso, si se asocia con el mismo ***access point*** independiente de su ubicación, entonces ni siquiera es móvil para la perspectiva de la capa de enlace. Por otro lado, si el usuario esta viajando a altas velocidades, atravesando multiples redes de acceso inalámbrico, entonces este es un usuario medianamente móvil. Si ademas quiere mantener conexiones ***TCP*** estables, es altamente móvil.
- ***How important is it for the mobile node's address to always remain the same?*** Si el usuario esta moviéndose a altas velocidades mientras mantiene una conexiones *TCP*, entonces es necesario que mantenga la misma dirección IP***.*** Si esto ocurre, la movilidad es invisible para la capa de aplicación.
- ***What supporting wired infrastructure is available?*** En todos los escenarios mencionados, asumimos que había una infraestructura fija a la cual los usuarios pueden conectarse. Sin embargo, en situaciones donde no ocurre esto, surgen las redes ***ad hoc***. Estas estarán fuera del alcance del libro

La residencia permanente de un móvil es su red local, y la entidad dentro de la red local que se encarga de manejar las funciones de movilidad se conoce como ***home agent***. La red en la cual un dispositivo reside actualmente se conoce como red extranjera, o visitada. La entidad que se encarga de manejar las funciones de movilidad se conoce como ***foreign agent***. Un ***correspondent*** es una entidad que quiere comunicarse con un nodo móvil.

## 1. Addressing

Cuando un usuario móvil esta en una red extranjera, todo el trafico dirigido a la dirección permanente del nodo, debe ser redirigida a la dirección actual. Una forma de realizar esto, es que la red extranjera publicite la nueva dirección utilizando protocolos de *intradomain* e *interdomain* *routing*. Esta solución resuelve el problema, pero no es escalable.

Una solución alternativa, implica mover la funcionalidad de movilidad del centro de la red a los bordes de la misma. El agente local se podría encargar de esta funcionalidad. Un rol del agente extranjero es el de crear un llamado ***care-of-address (COA)*** para el nodo móvil. Esta sera la ***foreign address***. Una segunda responsabilidad es la de informarle al agente local del ***COA***. Un nodo móvil también puede asumir las responsabilidades de un agente externo.

## 2. Routing to a Mobile Node

Existen dos enfoques para resolver el envío de paquetes a un nodo móvil:

### Indirect Routing to a Mobile Node

En este enfoque, se envían los paquetes directamente a la dirección permanente, sin enterarse de que el usuario es un usuario móvil. El agente local tiene la importante función de recibir estos paquetes y reenviarlos a la red extranjera. Desde allí, el ***foreign agent*** le reenviara los paquetes al usuario.

Para realizar esto, el agente local encapsula el datagrama en otro datagrama, completo. Este tiene como dirección el ***COA*** del nodo móvil. Cuando el agente extranjero lo recibe, lo des-encapsula y se lo envía al nodo original.

Cuando el nodo responde, este enviará un paquete con su dirección permanente como remitente, y con la dirección permanente del correspondiente. Debido a que conoce su dirección, no se deberá enviara el paquete al agente local.

En general, la funcionalidad requerida para este enfoque es:

- ***A mobile-node-to-foreign-agent protocol:*** El nodo móvil debe registrarse con el agente extranjero cuando se conecta a una red extranjera. Ademas, debe des-registrarse cuando sale de la red
- ***A foreign-agent-to-home-agent registration protocol:*** El agente extranjero debe registrar el ***COA*** con el agente local. Pero no debe explícitamente des-registrarlo. Esto se hara automáticamente con la registración del nuevo ***COA***, por parte de otro agente extranjero.
- ***A home-agent datagram encapsulation protocol:*** Permitiendo enviar el paquete original del correspondiente dentro de un datagrama direccionado al ***COA***.
- ***A foreign-agent decapsulation protocol:*** Permitiendo la des-encapsulación del paquete original, y el envío al nodo móvil.

Aun siguiendo este enfoque, puede haber perdida de paquetes cuando un nodo se cambia de red extranjera. En estos casos, se debe usar mecanismos de recuperaciones de perdida de paquetes, en capas superiores (capa de transporte, o aplicación).

### Direct Routing to a Mobile Node

El enfoque mostrado previamente sufre una ineficiencia conocida como ***triangle routing problem***. Los paquetes se envían primero a la red local, luego a la red extranjera, y finalmente al nodo móvil.

Este enfoque soluciona el problema, ya que el ***correspondent*** ***agent*** primero aprende la dirección ***COA*** del nodo móvil, y le envía paquetes directamente. Para aprender esta dirección, puede inicialmente realizar una consulta al agente local para aprender la dirección. Al igual que con el agente extranjero, el correspondiente puede manualmente realizar estas consultas, sin necesidad de que lo haga el ***correspondent agent***.

Esto, trae dos dificultades importantes:

- Se necesita un ***mobile-user location protocol***, para que el correspondiente consulte a la red local la dirección temporal del nodo.
- Cuando un nodo móvil se mueve de una red extranjera a otra, como se envían los paquetes a la nueva red. Una solución, es la de adoptar un protocol para notificarle al correspondiente el cambio de ***COA***. Sin embargo, otra solución alternativa la utilizada en la realidad.

Denominaremos ***anchor foreign agent*** al agente la red en la que el nodo móvil se encontraba originalmente. Cuando el nodo móvil cambia de red, este registra con el nuevo agente, y el nuevo agente le provee al ***anchor foreign agent*** de la dirección ***COA*** del nodo móvil.

Cuando el ***anchor*** ***foreign agent*** recibe un datagrama para el nodo móvil, entonces puede reencapsularlo y enviarselo al nodo móvil utilizando su nuevo ***COA***.
