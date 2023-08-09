En este capítulo, se introduce una nueva abstracción para un proceso, el ***thread*** o hilo. Un programa ***multi-threaded*** tiene más de un punto de ejecución. Se puede pensar a cada hilo como procesos separados que comparten el mismo espacio de direcciones, por lo tanto comparten información.

El estado de un ***thread*** entonces, es muy similar al de un proceso. Cada uno tiene su propio conjunto privado de registros que utiliza para computar, para pasar de un hilo a otro se debe ejecutar un ***context switch***. Este cambio de contexto será muy similar al utilizado para procesos.

En un programa ***multi-threaded*** tendremos un solo ***heap*** pero múltiples ***stacks***, uno para cada hilo. Estos romperá con nuestro esquema tradicional del espacio de direcciones, aunque no es un problema grave debido a que los stacks suelen tener tamaños pequeños.

## Ventajas

Hay dos razones principales por las cuales debemos usar concurrencia. La primera es el **paralelismo**, podemos dividir nuestro programa en distintas porciones que se ejecuten concurrentemente. Esto aporta velocidad en sistemas con múltiples procesadores, ya que cada hilo puede correr en un procesador distinto. Este proceso, de convertir un programa ***single-threaded*** a uno ***multi-threaded*** se conoce como ***paralelización***.

La segunda razón es un poco más sutil: para evitar que un programa se ralentiza debido a pedidos de **IO**. Utilizar hilos permite continuar la ejecución del programa en un hilo distinto, mientras otro hilo está suspendido.

## Intercambio de Información

Cuando utilizamos hilos, el resultado de la ejecución es **no determinística**, esto es debido a que el scheduler ***decide en que orden ejecutar los hilos, por lo que el resultado es **indeterminado**.

Como no sabemos el orden en que se ejecutarán los hilos, es muy difícil manejar de forma correcta las variables compartidas entre los distintos hilos. Cuando dos hilos quieren utilizar la misma variable al mismo tiempo, se producen algo conocido como ***condiciones de carrera*** o ***race conditions***, el resultado de la ejecución dependerá de que proceso se ejecuta antes, lo que puede ocasionar resultados inesperados.

Las porciones de código que pueden ocasionar una condición de carrera se conocen como ***secciones críticas***, una sección crítica es una porción del código que accede a una variable compartida (o cualquier recurso compartido).

## Atomicidad

Para solucionar este problema, necesitamos un mecanismo conocido como ***exclusión mutua**.* Esto garantiza que si un hilo está ejecutando una sección crítica, los otros hilos no podrán.

Para obtener esto, necesitamos una técnica conocida como ***atomic operation***. Una operación atómica es una operación que no puede ser interrumpida. Llamamos el agrupamiento de muchas acciones en una única operación atómica como una ***transacción***.

Si logramos que las secciones críticas sean *operaciones atómicas*, entonces no tendremos condiciones de carrera. La operación una vez empieza no puede ser interrumpida, por lo que ningún cambio de contexto puede alterar el resultado.

Normalmente no podremos encontrar una *operación atómica* para ***nuestra sección crítica, por lo que debemos recurrir a otra técnica: ***primitivas de sincronización***. Utilizando soporte del ***hardware***, podremos construir un programa ***multi-threaded*** que acceda a secciones criticas de forma sincronizada y controlada.
