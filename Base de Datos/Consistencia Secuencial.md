En el estudio de la replicación en las bases de datos distribuidas, se utilizan distintos modelos de consistencia.

Uno de los modelos más fuertes, y que proviene de las bases de datos centralizadas, es el de consistencia secuencial.

Partimos de una serie de procesos que ejecutan instrucciones de lectura $R_{P_i}(X)$ y de escritura $W_{P_i}(X)$, sobre una base de datos distribuida.

Se dice que una base de datos distribuida tiene consistencia secuencial cuando "el resultado de cualquier ejecución concurrente de los procesos es equivalente al de alguna ejecución secuencial en que las instrucciones de los procesos se ejecutan una después de otra".
