## Transacción

Una transacción es una unidad logica de trabajo. También puede ser pensado como una secuencia ordenada de instrucciones atómicas.

Una misma transaccion puede realizar varias operaciones de consulta/AMB durante su ejecución.

Antes de existir multitasking, las transacciones se serializaban. Hasta tanto no se terminara una, no se iniciaba la siguiente. Esto no es una buena idea, nos gustaria poder ejecutar las transacciones simultaneamente. No es deseable que la ejecución de una transacción lenta demore a otras de ejecución rápida.

Si dos transaccioens utilizan conjuntos de datos distintos, debería poder ejecutarse concurrentemente en distintos procesadores.

Las transacciones comparten recursos (tablas) entre si. Esto es un problema importante para le ejecución concurrente.