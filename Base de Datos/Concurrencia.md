En las bases de datos reales, múltiples usuarios realizan operaciones de consulta y/o actualización simuñtáneamente. Nos guastaria aprovechar la capacidad de procesamiento lo mejor posible al atender a los usuarios.

En un sistema monoprocesador, se puede utiliza multitasking. Varios hilos o procesos pueden estar corriendo concurrentemente.

En un sistema multiprocesador, se disponen de varias unidades de procesamiento que funcionan de forma simultanea. La base de datos se puede replicar, disponiendo de varias copias de algunas tablas (o fragmentos de tablas) en distintas unidades de procesamiento.

La concurrencia es la posibilidad de ejecutar múltiples transacciones en forma simultánea.

## Transacción

Una transacción es una unidad logica de trabajo. También puede ser pensado como una secuencia ordenada de instrucciones atómicas.

Una misma transaccion puede realizar varias operaciones de consulta/AMB durante su ejecución.

Antes de existir multitasking, las transacciones se serializaban. Hasta tanto no se terminara una, no se iniciaba la siguiente. Esto no es una buena idea, nos gustaria poder ejecutar las transacciones simultaneamente. No es deseable que la ejecución de una transacción lenta demore a otras de ejecución rápida.

Si dos transaccioens utilizan conjuntos de datos distintos, debería poder ejecutarse concurrentemente en distintos procesadores.

Las transacciones comparten recursos (tablas) entre si. Esto es un problema importante para le ejecución concurrente.

## Modelo de Concurrencia

Utilizaremos el modelo de concurrencia solapada (interleaved concurreny), que considera las siguientes hiótesis:

1. Disponemos de un único procesador que puede ejecutar múltiples transacciones simultáneamente
2. Cada transacción esta formada por una secuencia de instrucciones atómicas, que el procesador ejecuta de a una a la vez.
3. En cualquier momento el *scheduler* puede suspender la ejecución de una transacción, e iniciar o retomar la ejecución de otra.

## Instrucciones Atómicas

Las instruccines atómicas básicas de una transacción son:

- `leer_item(X)`: Lee el valor del item X, cargandolo en una variable en memoria
- `escribir_item(X)`: Ordena escribir el valor que está en memoria del item X en la base de datos.

Un item puede representar:

- El valor de un atributo en una fila determinada
- Una fila de una tabla
- Un bloque del disco
- Una tabla

En el único momento en el que la CPU interactura con la base de datos, es cuando ejecuta alguna de las dos operaciones vistas. Cualquier otra operación (manipulación de datos en memoria) es independiente del resto de transacciones.

> [!note] Nota
> Ordenar escribir no es lo mismo que efectivamente escribir. El nuevo valor podría quedar temporalmente en un *buffer* en memoría.

## Propiedades ACID

La ejecución de transacciones por un SGBD deben cumplir cuatro propiedades deseables:

- **Atomicidad:** Desde el punto de vista del usuario, las transacciones deben ser ejecutadas de forma atómica. Esto quiere decir que, o se ejecutan de forma completa, o no se ejecutan.
- **Consistencia:** Cada ejecución, por si misma, debe preservar la consistencia de la base de datos. La consistencia se define a partir de las reglas de integridad.
- **Aislamiento:** El resultado de la ejecución concurrente de las transacciones debe ser el mismo que si las transacciones se ejecutaran de forma aislada. Debe ser equivalente a alguna ejecución serial.
- **Durabilidad:** Una vez que el gestor informa que la transacción fue completada, debe asegurar la persistencia de la misma, independiente de toda falla que pueda ocurrir.

Para garantizar estas propiedades, los gestores disponen de mecanismos de recuperación para deshacer las opeaciones realizadas. En algun lado, el gestor debe tener un *log* de todas las operaciones que ejecuta. El gestor a veces utiliza el *log* no solo para deshacer transacciones, sino para rehacerlas. Esto nos permite satisfacer la propiedad de *durabilidad*.

Este *log* debe estar en disco para asegurar que vamos a poder recuperarnos de cualquier falla. En el disco del *log* se puede aprovechar la estructura secuencial, que es mucho mas rapida que una escritura de acceso aleatorio (como ocurriria con un disco normal).

Para ello, es necesario agregar a la secuencia de instrucciones de cada transaccion, algunas instrucciones especiales.

- `begin`: Indica el comienzo de una transacción.
- `commit`: Indica que la transacción ha terminado exitosamente, y se espera que su resultado haya sido efectivamente almacenado de forma persistente.
- `abort`: Indica que se produjo un error o falla, y que por lo tanto todos los efectos de la transacción deben ser deshechos (rolled back).

## Anomalias de Ejecución Concurrente

La anomalía de la **lectura sucia** ocurre cuando una transacción $T_2$ lee lo que ha sido modificado por otra transacción $T_1$. Si luego $T_1$ debe ser deshecha, entonces la lectura de $T_2$ no fue valida, esto implica que $T_2$ también debe ser deshecha. Si cuando se debe deshacer $T_2$, encontramos que ya se habia realizado *commit*, entonces estaremos ante un error.

Esta anomalía es un conflicto del tipo:

$$
WR: W_{T_1}(X)\dots R_{T_2}(X)\dots (a_{T_1} \lor c_{T_1})
$$

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

El cumplimiento de este protocolo es condición suficiente para garantizar que cualquier orden de ejecución de un conjunto de transaciónes sea serializable.
