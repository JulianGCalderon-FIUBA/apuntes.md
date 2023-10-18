El problema de control de concurrencia en vistas de garantizar el aislamiento tiene dos enfoques:

- Enfoque **pesimista**: Busca garantizar que no se produzcan conflictos
	- Control de concurrencia basado en *locks*
- Enfoque **optimista**: Consiste en "dejar hacer" a las transacciones y deshacer (*rollback*) una de ellas si en fase de validación se descubre un conflicto. Es conveniente cuando la probabilidad de error es baja.
	- Control de concurrencia basado en *timestamps*.
	- *Snapshot Isolation*: Cada transacción tiene un *snapshot* o copia local, funciona mucho mejor en contextos optimistas.
	- Control de concurrencia multiversión.

## Basado en Locks

El gestor utiliza locks para bloquear a los recursos y no permitir que más de una transacción los use en forma simultánea. Los locks son insertados por el gestor como instrucciones especiales en medio de la transacción.

Es posible garantizar el aislamiento a partir de la utilización de locks (no es trivial, requiere más que simplemente bloquear antes de acceder a una variable).

El protocolo más común es el conocido protocolo de lock de dos fases (2PL; two-phase lock): Una transacción no puede adquirir un lock luego de liberar un lock que había adquirido.

La regla naturalmente divide la ejecución en dos fases:

1. Fase de adquisición de locks, en la que la cantidad de locks adquiridos crece
2. Fase de liberación de locks, en la que la cantidad de locks decrece.

El cumplimiento de este protocolo es condición suficiente para garantizar que cualquier orden de ejecución de un conjunto de transacciones sea serializable. Por otro lado, nos prohíbe muchos solapamientos que hubiesen sido válidos, por lo que el código es menos eficiente.

### Deadlocks

La utilización de locks nos trae problemas que antes no teníamos, como la aparición de *deadlocks*. Para prevenirlos tendremos distintos mecanismos.

- Cada transacción adquiera todos los locks que necesita antes de comenzar su primera instrucción, de forma simultánea,
- Definir un ordenamiento de los recursos, y obligar a que luego todas las transacciones respeten dicho ordenamiento en la adquisición de locks.

Estos métodos no son óptimos, ya que requieren de saber los recursos que necesitaremos de antemano.

Otra forma de resolver esto es a partir de mecanismos de detección de *deadlocks*:

- Con la utilización del **grafo de alocación de recursos**.
- Definir un *timeout* para la adquisición del lock, despues del cual se aborta la transacción.

### Grafo de Alocación de Recursos

Es un grafo dirigido que posee a las transacciones y los recursos como nodos, y en el cual se coloca un arco de una transacción a un recurso cada vez que una transacción espera por un recurso, y un arco de un recurso a una transacción cada vez que la transacción posee el *lock* de dicho recurso.

Cuando se detecta un ciclo en este grafo, se aborta una de las transacciones involucradas.

### Inanición

La inanición o *livelock* es una condición vinculada con el *deadlock*, y ocurre cuando una transacción no logra ejecutarse por un periodo de tiempo indefinido. Puede ocurrir, por ejemplo, cuando ante un deadlock se elige siempre a la misma transacción para ser abortada.

La solución más común consiste en encolar los pedidos de *locks* de manera que las transacciones que esperan d
