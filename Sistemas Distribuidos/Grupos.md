Es una construcción lógica que nos permite definir conjuntos de procesos que se comunicarán entre sí. Permiten ver una coleccion de procesos como una abstraccion.

- Los mensajes son enviados a todos o algunos de los miembros de un grupo.
- Los grupos son dinámicos, pueden crearse y destruirse en cualquier momento.
- Se debe definir un formato de entrada y de salida al grupo (suscripción y cancelación).

## Difusion de Mensajes

Hay distintos modos de envio:

- Unicast: Comunicacion punto a punto
- Anycast: Uno solo lo recibe, pero cualquiera
- Multicast: Lo reciben todos los que estan en el grupo
- Broadcast: Lo reciben todos los procesos

## Topologia

Hay distintos tipos de topologias para la difusion:

- Centralziada: Un nodo le envia a todos.
- Descentralizada: Un nodo le envia a los vecinos, y estos propagan el mensaje.

## Atomicidad

Hay situaciones donde queremos que o todos reciban el mensaje, o ninguno. Para esto necesitaremos utilizar ACKs y reintentos.
