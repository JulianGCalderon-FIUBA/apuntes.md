El paralelismo es una forma de computación en la cual varios cálculos pueden realizarse simultáneamente, ​basado en el principio de dividir los problemas grandes para obtener varios problemas pequeños, que son posteriormente solucionados en paralelo.

Los objetivos de la paralelización son:

- Reducir el tiempo de cómputo de una tarea (latencia)
- Incrementar la cantidad de tareas que se pueden realizar en paralelo (*throughput*)
- Reducir la energía consumida al realizar todas las tareas

La posibilidad de paralelización es una de las ventajas importantes de un [[Sistema Distribuido]]

## Estrategias de Paralelización

Hay dos estrategias principales para paralelizar el trabajo:

- Descomposición funcional, en donde paralelizamos las tareas a realizar, y luego agregamos el resultado
- Particionamiento de datos, en donde cada conjunto independiente de datos se procesa en paralelo.

Estas dos estrategias se pueden combinar.

## Speedup

El **speedup** es el ratio de optimización de una operación.

El **camino crítico** es la máxima longitud de tareas secuenciales a computar. Define el mejor rendimiento que se puede obtener al realizar un conjunto de tareas.

Existen distintas formas de analizar el speedup:

- [[Ley de Amdahl]]
- [[Ley de Gustafson]]
- [[Modelo Work-Span]]

## Paralelismo vs. Concurrencia

En un sistema paralelo, la ejecución ocurre al mismo tiempo, con dos recursos distintos, de forma independiente

En un sistema concurrente, los procesos se deben sincronizar para acceder al mismo recurso.

![[Paralelización 1739229107.png]]

Cuanto más paralelizable es un sistema, más se podrá mejorar. Los casos de error tienden a estar en los puntos de sincronización.
