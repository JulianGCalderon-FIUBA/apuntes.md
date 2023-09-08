Queremos realizar un cómputo "simple" sobre un conjunto grande de datos. Cada dato es independiente, o un pequeño subconjunto lo es.

Algunos ejemplos de estas tareas son: procesar sonido, imágenes, video, entrenar redes neuronales.

Para resolver esto, podríamos utilizar Fork-Join.

Lanzar una tarea tiene un costo de cómputo, por lo que no siempre utilizar concurrencia es más rápido (en particular cunado el cómputo es muy simple). Además, la cantidad de CPU es limitada

En estos casos, es mejor lanzar menos tareas, pero con más trabajo cada una. Cuando las tareas acceden a memoria cercana, esto tiene la ventaja de que aprovecha mejor el principio de localidad de memoria.

Si aun así, el rendimiento no es tan bueno como necesitamos. Podemos recurrir a las operaciones vectoriales.

## Operaciones Vectoriales

Al detenerse la ley de Moore, el aumento de transistores no se tradujo en un aumento de velocidad. Esto se debio a que el calor generador por los transistores era mayor al que fisicamente se podia disipar.

En su lugar, se agregaron múltiples ALU para operar sobre los mismos registros de forma concurrente. Esto dio lugar a la introducción de juegos de instrucciones SIMD (Single Instruction Multiple Data).

Los registros del procesador se pueden dividir en carriles (la cantidad de carriles depende del tamaño de los registros), y operar sobre cada uno de ellos de forma concurrente con una ALU distinta.

Tendremos dos tipos de operaciones:

- Operaciones **verticales** entre los mismos carriles de los distintos registros.
- Operaciones **horizontales** reducen un vector en un escalar, pero son más lentas.

## CUDA

En CUDA, los hilos se modelan como bloques que trabajan sobre una pequeña porción de memoria independiente, y se puede direccionar en una, dos, o tres dimensiones.

Permite hasta 2048 hilos por IS
