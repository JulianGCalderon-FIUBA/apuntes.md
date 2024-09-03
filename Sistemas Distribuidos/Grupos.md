Es una construcción lógica que nos permite definir conjuntos de procesos que se comunicarán entre sí.

Los mensajes son enviados a todos o algunos de los miembros de un grupo.

Los grupos son dinámicos, pueden crearse y destruirse en cualquier momento.

Se debe definir un formato de entrada y de salida al grupo (suscripción y cancelación).

## Topologia

La **topología de red** se define como un mapa físico o lógico de una para intercambiar datos. En otras palabras, es la forma en que está diseñada la red, sea en el plano físico o lógico.

- Bus
- Star
- Tree
- Mesh
- Sequential
- Ring

La difusión puede ser centralizada (uno envía a todos) o descentralizada (uno envía a algunos y se continúa la cadena)

## Atomicidad

Los mensajes deben entregarse a todos o a ninguno. En estos casos es necesario realizar ACK de los mensajes, demorar el delivery de los paquetes recibidos.

Se puede reintentar el renvio de los mensjaes para asegurar la entrega, o tener un mensaje de "rollback" para notificar.
