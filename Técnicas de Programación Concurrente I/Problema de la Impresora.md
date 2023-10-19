En una oficina hay una impresora compartida

Habitualmente, las personas que trabajan allí envían documentos para ser impresos. Sin embargo, muchas veces se generan inconvenientes, ya que varias personas envían documentos al mismo tiempo, y luego las impresiones se encuentran intercaladas en la bandeja de salida, entorpeciendo el trabajo.

## Solución con [[Exclusión Mutua Distribuida#Algoritmo Centralizado|Mutex Centralizado]]

El coordinador tendrá que levantar un servidor y un hilo por cada conexión entrante. Estos hilos manejan las conexiones con los clientes que quieren acceder a la sección crítica.

Además de los hilos, tendremos un *mutex* local, al cual accederán los hilos.

1. Cuando un hilo recibe una petición de *lock*, entonces trata de obtener el *lock* local:
2. En cuanto lo obtiene, le da el OK al cliente. Luego se queda esperando a que el cliente finalice.
3. Una vez el cliente indica que ya salió de la sección crítica, entonces realiza el *unlock*.

De esta forma, estamos manejando un *lock* de forma remota.

## Solución con [[Exclusión Mutua Distribuida#Algoritmo Distribuido|Mutex Distribuido]]

Como debemos tener una conexión con todos, entonces utilizaremos UDP. Cada cliente tendrá:

- Un socket UDP
- Una cola de clientes que hayan pedido el *socket* (y aún no les dio OK)
- Un *timestamp* de cuando pidió el *socket* (si es que lo pidió)
- Una lista de clientes que ya me dieron el OK.

Tendremos

### Entrada a la Sección Crítica

Cuando el cliente quiere entrar a la sección crítica, entonces guarda el *timestamp* y le envía un mensaje a cada uno de los clientes restantes.

Una vez recibió el OK de todos los clientes, entonces puede entrar en la sección crítica (para implementar esto, se puede utilizar una variable de condición).

### Salida de la Sección Crítica

Cuando el cliente quiere salir de la sección crítica, entonces debo drenar la cola de clientes que pidieron el *socket* y enviar un OK a cada uno.

### Recepción de Mensajes

Por cada mensaje de OK recibido, agrega al cliente a la lista de clientes que le enviaron el OK. (y hace un *notify* de la variable de condición)

Por cada mensaje de *timestamp* recibido, cuando el propio cliente no tiene un *timestamp* asociado, entonces sabremos que no está queriendo entrar a la sección crítica. Luego, puede enviar el OK.

Si tiene un *timestamp* asociado, y si el propio es mayor, envía un OK. En caso contrario, encola el cliente.
