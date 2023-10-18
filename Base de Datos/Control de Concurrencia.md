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
