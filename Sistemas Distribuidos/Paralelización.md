El paralelismo es una forma de computación en la cual varios cálculos pueden realizarse simultáneamente, ​basado en el principio de dividir los problemas grandes para obtener varios problemas pequeños, que son posteriormente solucionados en paralelo.

Los objetivos de la paralelización son:

- Reducir el tiempo de cómputo de una tarea (latencia)
- Incrementar la cantidad de tareas que se pueden realizar en paralelo (*throughput*)
- Reducir la energía consumida al realizar todas las tareas

No es lo mismo un sistema paralelo, que un sistema concurrente. En un sistema paralelo, los procesos son independientes, y cada uno tiene sus propios recursos. En un sistema concurrente, los recursos son compartidos.

La posibilidad de paralelización es una de las ventajas importantes de un [[Sistema Distribuido]]

## Estrategias de Paralelización

Hay dos estrategias principales para paralelizar el trabajo:

- Descomposición funcional, en donde paralelizamos las tareas a realizar, y luego agregamos el resultado
- Particionamiento de datos, en donde cada conjunto independiente de datos se procesa en paralelo.

Estas dos estrategias se pueden combinar.
