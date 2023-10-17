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
