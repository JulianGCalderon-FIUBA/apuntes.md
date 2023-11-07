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

Si un evento $b$ fue influenciado por un evento $a$, la causalidad requiere que todos vean al evento $a$ antes que al evento $b$. Dos eventos que no están causalmente correlacionados se dicen concurrentes, y no es necesario que sean vistos por todos en el mismo orden.

En este modelo, "dos escrituras que están potencialmente causalmente relacionadas deben ser vistas por todos en el mismo orden".

## Consistencia Eventual

El modelo de consistencia eventual está basado en la siguiente observación: "En la mayoría de los sistemas reales, son pocos los procesos que realizan modificaciones o escrituras, mientras que la mayor parte solo lee, ¿Qué tan rápido necesitamos que las actualizaciones de un proceso que escribe sean vistos por los procesos que leen?"

Estas situaciones pueden tolerar un grado bastante más alto de inconsistencia.

Decimos entonces que una ejecución tiene consistencia eventual cuando "si en el sistema no se producen modificaciones (escrituras) por un tiempo suficientemente grande, entonces eventualmente todos los procesos verán los mismos valores".

En otras palabras, esto implica que eventualmente todas las réplicas llegaran a ser consistentes.
