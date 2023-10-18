En las bases de datos reales, múltiples usuarios realizan operaciones de consulta y/o actualización simuñtáneamente. Nos guastaria aprovechar la capacidad de procesamiento lo mejor posible al atender a los usuarios.

En un sistema monoprocesador, se puede utiliza multitasking. Varios hilos o procesos pueden estar corriendo concurrentemente.

En un sistema multiprocesador, se disponen de varias unidades de procesamiento que funcionan de forma simultanea. La base de datos se puede replicar, disponiendo de varias copias de algunas tablas (o fragmentos de tablas) en distintas unidades de procesamiento.

La concurrencia es la posibilidad de ejecutar múltiples transacciones en forma simultánea.

## Modelo de Concurrencia

Utilizaremos el modelo de concurrencia solapada (interleaved concurreny), que considera las siguientes hiótesis:

1. Disponemos de un único procesador que puede ejecutar múltiples transacciones simultáneamente
2. Cada transacción esta formada por una secuencia de instrucciones atómicas, que el procesador ejecuta de a una a la vez.
3. En cualquier momento el *scheduler* puede suspender la ejecución de una transacción, e iniciar o retomar la ejecución de otra.

## Solapamiento

Un solapamiento entre dos [[Transacción|transacciones]] $T_1, T_2$ es una lista de $m(T_1) + m(T_2)$ instrucciones, en donde cada instrucción de $T_1$ y de $T_2$ aparece una única vez, y las instruccioens de cada transacción conservan el orden entre ellas dentro del solapamiento.

Podemos calcular la cantidad de solapamientos posibles como

$$
\frac{(m(T_1)+m(T_2))!}{m(T_1)!\cdot m(T_2)!}
$$

A partir de la [[Transacción#Notación|notación]] de las transacciones, podemos escribir por ejemplo:

$$
b_{T_1}b_{T_2}\dots R_{T_1}(X)\dots W_{T_2}(X)\dots c_{T_1}c_{T_2}
$$

## Ejecución Serial

Dado un conjunto de transacciones $T_1, T_2, \dots, T_n$, una ejecución serial es aquella en la que las transaccines se ejecutan por completo una detrás de otra, en base a algún orden dado.

Podemos calcular la cantidad de ejecuciones seriales distintas existen entre $n$ transacciones, tendremos $n!$

## Serializabilidad

Decimos que un solapamiento de un conjunto de transacciones $T_1, T_2, \dots, T_n$ es **serializable** cuando la ejecución de sus instrucciones en dicho orden deja la base de datos en un estado equivalente a aquel en que la hubiera dejado alguna ejecución serial.

Nos interesa q
