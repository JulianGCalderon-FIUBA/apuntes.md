El objetivo de la elección de líder es elegir a un proceso en un grupo para que desempeñe. Se deben permitir reelecciones en caso de que el proceso líder decida darse de baja, o se encuentre caído.

Cualquier proceso puede comenzar una nueva elección de líder, solo puede haber más de un líder a la vez, y el resultado de la elección de un nuevo líder debe ser única y repetible.

## Propiedades

Los siguientes algoritmos de elección de líder comparten las siguientes propiedades:

- Cada proceso tiene un identificador único.
- Todos los procesos poseen un arreglo que indica el estado del algoritmo de líder
- Los estados posibles son "definidos" (`elected == P`), o "indefinido" (`elected == @)`.
- El estado inicial de un proceso es indefinido.

Se deben garantizar:

- **Safety**: Un proceso participante posee uno de ambos estados posibles.
- **Liveness**: Todos los procesos participan de la elección de líder y bien terminan con estado "definido", o comienzan una nueva elección de líder.

### Algoritmo de Anillo

Al inicio de una elección, el proceso $p$ se marca como participando, y envía un mensaje en sentido del anillo, indicando que es el líder.

Cuando un proceso recibe un mensaje de elección de líder:

- Si se encuentra en estado "no participando"
	- Cambia su estado a participando.
	- Compara el identificador del líder del mensaje con el suyo, lo reemplaza en caso de ser mayor, y reenvía el mensaje al nodo siguiente.
- Si se encuentra en estado "participando", analiza el identificador del mensaje:
	- Si es menor al suyo, no reenvía el mensaje.
	- Si es mayor al suyo, reenvía el mensaje.
	- Si es igual al suyo, entonces es el líder.

Cuando un proceso reconoce que es el líder, entonces cambia su estado a "no participando", y envía un mensaje de "líder elegido".

Cuando un proceso recibe un mensaje de "líder elegido", cambia su estado a "no participando", y registra el nuevo líder. Si el identificador es distinto al suyo, retransmite el mensaje.

### Algoritmo Bully

Este algoritmo asume que cualquier proceso puede morir de forma inesperada, por lo que utiliza *timeouts* para detectar que un proceso no está respondiendo.

Asume que todos los procesos pueden comunicarse entre sí, y conocen los identificadores de todo el resto de procesos.

Se definen las siguientes variables:

- `t_max`: Tiempo máximo de transmisión.
- `t_proceso`: Tiempo máximo de cualquier proceso para resolver un mensaje.
- `T`: Tiempo para detectar procesos caídos, calculado como `2 * t_max + t_proceso`.

El proceso con mayor identificador puede identificarse como líder, y envía un mensaje de "coordinador" a todos los procesos del sistema, indicando que él es el líder:

- Los procesos al recibir este mensaje, eligen al proceso que envío el mensaje como líder.

Si un proceso detecta el líder está caído, envía un mensaje de "elección" a todos los procesos con un identificador mayor al suyo:

- Los procesos al recibir este mensaje, responden con un mensaje "ack", y comienzan una nueva elección.
- Si un proceso que comenzó una elección no recibe respuesta luego de un tiempo transcurrido $T$, este se autoproclama líder.

Eventualmente, el proceso vivo con mayor identificador recibira un mensaje "elección", y al obtener respuesta del resto se autoproclamará como líder.

Si un proceso caído vuelve a la vida, comienza una nueva elección de lider. Si este es el que posee el mayor identificador, será elegido como nuevo líder.
