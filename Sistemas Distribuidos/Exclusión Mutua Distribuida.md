El objetivo es crear un algoritmo que permita pedir y obtener acceso exclusivo a un recurso que se encuentra disponible en la red. Para lograr el objetivo, se utilizará **pasaje de mensajes**.

Recordemos que las propiedades que se buscan cumplir:

- **Safety**: Solo un proceso puede obtener el recurso en todo momento.
- **Liveness**: Si un proceso está listo para recibir un recurso, debe obtenerlo eventualmente.
- **Fairness**: El uso del recurso se distribuye de forma uniforme entre los procesos. Una vez obtenido, debe ser liberado luego de un tiempo límite.

## Servidor Central

Se designa alguno de los procesos del sistema como coordinación de la sección crítica.

Los procesos piden acceso a la sección crítica al servidor central, el cual se los otorga de a uno a la vez. Si un recurso se encuentra tomado, las consultas se encolan en modo FIFO.

Se sabe el identificador de cada recurso de antemano.

Algunas ventajas de este esquema son:

- Las consultas son procesadas en orden.
- Es fácil de entender y de implementar.
- Los procesos solo necesitan conocer al servidor.
- La cantidad de conexiones y mensajes es mínima.

Por otro lado, tiene las siguientes desventajas:

- El servidor central es un único punto de falla.
- Los procesos no pueden distinguir entre sí el servidor está caído o no responsivo.
- Se produce un cuello de botella.

## Token Ring

Se construye un anillo ordenando a todos los procesos por algún atributo. Luego se crea un token que circula alrededor del anillo.

Cuando un proceso recibe el token, accede a la sección crítica en caso de que sea necesario, y luego le pasa el *token* a su vecino. Puede haber múltiples *tokens*, uno por sección crítica.

Algunas ventajas:

- Fácil de implementar
- No es necesario elegir un coordinador
- Tolerante a caídas de nodos
- Requiere pocas conexiones (en el peor caso tiene que concoer a todos los nodos, pero se puede limitar a, por ejemplo, solo los 3 siguientes).

Es un algoritmo fácil de implementar y de entender, aunque tiene algunas desventajas:

- Se debe implementar algún mecanismo de recuperación de token, en caso de que se caiga el nodo que lo tenía.
- La creación de un anillo de forma dinámica requiere un protocolo en sí mismo.
- Se comunican siempre aunque nadie necesite el token.

## Ricart & Agrawala

Es un algoritmo distribuido que utiliza *reliable multicast* y relojes lógicos.

Cuando un proceso intenta acceder a una sección crítica, entonces:

- Crea un mensaje con un timestamp asociado al proceso, un identificador, y el nombre del recurso a acceder.
- Envía el mensaje a todos los procesos del grupo.
- Espera hasta que todos los procesos le den permiso de ingresar a la sección (`OK`)
- Entra la sección crítica.

Cuando un proceso recibe una consulta, entonces:

- Si no está interesado en entrar a la sección crítica, devuelve `OK`.
- Si posee la sección crítica, no responde y encola el mensaje. Una vez sale, devuelve `OK` a todos los mensajes encolados.
- Si envió previamente un mensaje para acceder a la sección crítica, entonces compara el timestamp del mensaje enviado y el mensaje recibido. Aquel que tenga un menor timestamp gana:
	- Si el receptor es el perdedor, entonces envía un `OK`.
	- Si el receptor es el ganador, entonces encola la consulta.

Algunas ventajas:

- No requiere de un coordinador
- Mientras nadie quiera acceder al recurso, no consume recursos en la red
- Tolerante a caídas de nodos

Tiene otras desventajas:

- Se requiere de un *mesh* de conexiones. Todos los procesos deben conocerse.
- La cantidad de mensajes enviados es muy alta.
- Es imposible detectar entre un proceso caído o un proceso en una sección crítica.
