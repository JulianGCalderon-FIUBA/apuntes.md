Queremos realizar un cómputo "simple" sobre un conjunto grande de datos. Cada dato es independiente, o un pequeño subconjunto lo es. Para resolver esto, podriamos utilizar Fork-Join.

Lanzar una tarea tiene un costo de cómputo, por lo que no siempre utilizar concurrencia es más rápido (en particular cunado el cómputo es muy simple). Además, la cantidad de CPU es limitada

En estos casos, es mejor lanzar menos tareas, pero con más trabajo cada una. Cuando las tareas acceden a memoria cercana, esto tiene la ventaja de que aprovecha mejor el principio de localidad de memoria.

## Operaciones Vectoriales

Al detenerse la ley de Moore, el aumento de transistores no se tradujo en un aumento de velocidad. En su lugar, se agregaron múltiples ALU para operar sobre los mismos registros de forma concurrente. Esto dio lugar a la introducción de juegos de instrucciones SIMD (Single Instruction Multiple Data).

Los registros del procesador se pueden dividir en $N$ carriles (según el tamaño de los datos), y operar sobre cada uno de ellos de forma concurrente con una ALU distinta.

Debido a que en las operaciones participan múltiples registros, se utilizan operaciones verticales. El primer carril del primer registro opera junto al primer carril del segundo registro.
