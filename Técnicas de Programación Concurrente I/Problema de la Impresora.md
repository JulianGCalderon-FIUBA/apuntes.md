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

Como debemos tener una conexión con todos, entonces utilizaremos UDP.
