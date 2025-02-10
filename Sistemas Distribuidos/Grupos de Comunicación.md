Es una construcción lógica que nos permite definir conjuntos de procesos que se comunicarán entre sí. Permiten ver una colección de procesos como una abstracción.

- Los mensajes son enviados a todos o algunos de los miembros de un grupo.
- Los grupos son dinámicos, pueden crearse y destruirse en cualquier momento.
- Se debe definir un formato de entrada y de salida al grupo (suscripción y cancelación).

## Difusión de Mensajes

Hay distintos modos de envío:

- Unicast: Comunicación punto a punto
- Anycast: Uno solo lo recibe, pero cualquiera. Por ejemplo, envía al nodo más cercano.
- Multicast: Lo reciben todos los que están en el grupo
- Broadcast: Lo reciben todos los procesos

## Topología de Difusión

Hay distintos tipos de [[Topología de Comunicación|topologías]] para la difusión:

- Centralizada: Un nodo le envía a todos.
- Descentralizada: Un nodo le envía a los vecinos, y estos propagan el mensaje.

![[Grupos de Comunicación 1739231329.png]]
