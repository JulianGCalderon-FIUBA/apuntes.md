Es necesario que la información entre los distintos nodos de un sistema distribuido sean consistenes.

Hay distintas técnicas que solucionan el problema de la consistencia, como:

## Consistencia Secuencial

En el estudio de la replicación en las bases de datos distribuidas, se utilizan distintos modelos de consistencia.

Uno de los modelos más fuertes, y que proviene de las bases de datos centralizadas, es el de consistencia secuencial.

Partimos de una serie de procesos que ejecutan instrucciones de lectura $R_{P_i}(X)$ y de escritura $W_{P_i}(X)$, sobre una base de datos distribuida.

Se dice que una base de datos distribuida tiene consistencia secuencial cuando "el resultado de cualquier ejecución concurrente de los procesos es equivalente al de alguna ejecución secuencial en que las instrucciones de los procesos se ejecutan una después de otra". Esto no implica serializabilidad, pues las transacciones no deben ser solapadas.

Este tipo de consistencia va en contra de la disponibilidad, pues es un modelo muy restrictivo.

## Consistencia Causal

En el modelo de consistencia causal se busca capturar eventos que puedan estar causalmente relacionados.

Si un evento $b$ fue influenciado por un evento $a$, la causalidad requiere que todos vean al evento $a$ antes que al evento $b$.
