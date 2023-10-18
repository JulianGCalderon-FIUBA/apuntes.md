En las bases de datos reales, múltiples usuarios realizan operaciones de consulta y/o actualización simuñtáneamente. Nos guastaria aprovechar la capacidad de procesamiento lo mejor posible al atender a los usuarios.

En un sistema monoprocesador, se puede utiliza multitasking. Varios hilos o procesos pueden estar corriendo concurrentemente.

En un sistema multiprocesador, se disponen de varias unidades de procesamiento que funcionan de forma simultanea. La base de datos se puede replicar, disponiendo de varias copias de algunas tablas (o fragmentos de tablas) en distintas unidades de procesamiento.

La concurrencia es la posibilidad de ejecutar múltiples transacciones en forma simultánea.

## Modelo de Concurrencia

Utilizaremos el modelo de concurrencia solapada (interleaved concurreny), que considera las siguientes hiótesis:

1. Disponemos de un único procesador que puede ejecutar múltiples transacciones simultáneamente
2. Cada transacción esta formada por una secuencia de instrucciones atómicas, que el procesador ejecuta de a una a la vez.
3. En cualquier momento el *scheduler* puede suspender la ejecución de una transacción, e iniciar o retomar la ejecución de otra.

## Control de Concurrencia

El problema de control de concurrencia en vistas de garantizar el aislamiento tiene dos enfoques:

- Enfoque pesimista: Busca garantizar que no se produzcan conflictos
	- Control de concurrencia basado en *locks*
- Enfoque optimista: Consiste en "dejar hacer" a las transacciones y deshacer (rollback) una de ellas si en fasede validación se descubre un conflicto. Es conveniente cuando la probabilidad de error es baja.
	- Control de concurrencia basado en *timestamps*.
	- *Snapshot Isolation*: Cada transacción tiene un *snapshot* o copia local, funciona mucho mejor en contextos optimistas.
	- Control de concurrencia multiversión.

### Basado en Locks

El gestor utiliza locks para bloquear a los recursos y no permitir que mas de una transacción los use en forma simultánea. Los locks son insertados por el gestor como instrucciones espceiales en medio de la transacción.

Es posible garantizar el aislamiento a partir de la utilización de locks (no es trivial, requiere mas que simplemente bloquear antes de acceder a una variable).

El protocolo mas común es el conocido protocolo de lock de dos fases (2PL; two-phase lock): Una transacción no puede adquirir un lock luego de liberar un lock que habia adquirido.

La regla naturalmente divide la ejecución en dos fases:

1. Fase de adquisisión de locks, en la que la cantidad de locks adquiridos crece
2. Fase de liberación de locks, en la que la cantidad de locks decrece.

El cumplimiento de este protocolo es condición suficiente para garantizar que cualquier orden de ejecución de un conjunto de transaciónes sea serializable. Por otro lado, nos prohibe muchos solapamientos que hubiesen sido validos, por lo que el código es menos eficiente.

La utilización de locks nos trae problemas que antes no teniamos, como la aparición de *deadlocks* y *livelocks*. Para detectar un *deadlock*, podemos utilizar un mecanismo de detección de basado en un grafo de alocación de recursos.
