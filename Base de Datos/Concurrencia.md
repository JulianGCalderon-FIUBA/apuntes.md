En las bases de datos reales, múltiples usuarios realizan operaciones de consulta y/o actualización simuñtáneamente. Nos guastaria aprovechar la capacidad de procesamiento lo mejor posible al atender a los usuarios.

En un sistema monoprocesador, se puede utiliza multitasking. Varios hilos o procesos pueden estar corriendo concurrentemente.

En un sistema multiprocesador, se disponen de varias unidades de procesamiento que funcionan de forma simultanea. La base de datos se puede replicar, disponiendo de varias copias de algunas tablas (o fragmentos de tablas) en distintas unidades de procesamiento.

La concurrencia es la posibilidad de ejecutar múltiples transacciones en forma simultánea.

## Modelo de Concurrencia

Utilizaremos el modelo de concurrencia solapada (interleaved concurreny), que considera las siguientes hiótesis:

1. Disponemos de un único procesador que puede ejecutar múltiples transacciones simultáneamente
2. Cada transacción esta formada por una secuencia de instrucciones atómicas, que el procesador ejecuta de a una a la vez.
3. En cualquier momento el *scheduler* puede suspender la ejecución de una transacción, e iniciar o retomar la ejecución de otra.

## Anomalias de Ejecución Concurrente

Cuando se ejecutan transacciones en forma concurrente se da lugar a distintas situaciones anómalas que pueden violar las propiedades ACID.

### Lectura Sucia

La anomalía de la **lectura sucia** ocurre cuando una transacción $T_2$ lee lo que ha sido modificado por otra transacción $T_1$.

Si luego $T_1$ debe ser deshecha, entonces la lectura de $T_2$ no fue valida, esto implica que $T_2$ también debe ser deshecha. Si cuando se debe deshacer $T_2$, encontramos que ya se habia realizado *commit*, entonces estaremos ante un error.

Esta anomalía también se la conoce con el nombre de *temporary update* o *read uncommited data*.

Esta anomalía es un conflicto del tipo:

$$
WR: W_{T_1}(X)\dots R_{T_2}(X)\dots (a_{T_1} \lor c_{T_1})
$$

### Actualización perdida

La anomalia de la **actualización perdida** ocurre cuando una transacción $T_2$ modifica un item que fue leído anteriormente por una primera transacción $T_1$ que aún no terminó. Si la primera transacción luego modifica, lo hará en base al valor leido inicialmente, y la modificación de $T_2$ se perderá.

Si en cambio la primera transacción volvería a leer el item luego de que la segunda la escribiera, se encontraría un valor distinto. Este caso se conoce como **lectura no repetible**.

La anomalía de **escritura sucia** ocurre cuando una transacción $T_2$ escribe un item que ya habia sido escrito por otra transacción $T_1$. Si $T_1$ luego aborta, se deshacera el cambio de $T_2$ también.

La anomalía del **fantasma**, se produce cuando una transacción $T_1$ observa un conjunto de items que cumplen determinada condición, y luego dicho conjunto cambia porque algunos de sus items son modificados/creados/eliminados por otra transacción $T_2$.

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
