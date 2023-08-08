A medida que avanza el tiempo, los sistemas con múltiples procesador se vuelven cada vez más comunes. La aparición de procesadores ***multicore*** son el núcleo de estos sistemas.

Hay muchas problemáticas que surgen cuando tratamos de correr una aplicación en múltiples procesadores. Para poder hacer esto, debemos reescribir nuestro programa para permitir que se ejecute en ***paralelo***, quizás a partir de la utilización de hilos o ***threads***.

# Arquitecturas Multiprocesador

Las arquitecturas multiprocesador tienen ciertas diferencias respecto a las arquitecturas con un solo procesador, respecto al ***hardware***. La diferencia se centra en el uso de la memoria ***cache,*** y como se comparte información entre los procesadores.

En un sistema con un solo procesador, existe una jerarquía de ***caches*** que se utilizan para que el procesador corra programas de forma rápida. Por otro lado, en la memoria general toda la información, pero con tiempo de acceso mayores. La memoria ***cache*** se basa en los principios de localidad, tanto temporal como espacial.

Cuando tenemos múltiples procesador, utilizar ***cache*** puede ser más complicado. Cuando un programa modifica un valor, normalmente este se actualiza en el disco un tiempo después, por razones de optimización. Con múltiples procesadores, esto puede ser un problema. Se conoce como ***cache coherence***. 

Una solución para este problema es utilizar una técnica conocida como ***bus snooping***. Las ***caches*** prestan atención a las actualizaciones observando un ***bus*** que los conecta con la memoria principal. Cuando se detecta un cambio, se actualiza la información o se invalida la copia.

# Afinidad del Caché

Un problema final que surge con los multiprocesadores, es que si se cambia el procesador en el cual se está corriendo un proceso, se pierde la afinidad del *caché*. Cuando un programa vuelve a correr, suele ser buena idea que corra en el mismo procesador que antes.

# Planificador de Única Cola

EL enfoque más simple es el de reutilizar el planificador de un solo procesador, colocando todos los procesos a ejecutar en una cola de ejecución. Este enfoque se conoce como ***SQMS*** o ***single-queue multiprocessor scheduling***. Este enfoque es simple, aunque tiene ciertas desventajas.

Este enfoque no escala bien, para asegurarnos que funcione bien, debemos utilizar ***lockeo*** para evitar condiciones de carrera. Estos ***locks*** pueden tener un gran impacto negativo grande en el rendimiento.

Para solucionar la afinidad del caché, muchos procesadores introducen un mecanismo que permite que los procesos se ejecuten en el mismo procesador que antes. Específicamente, se podría proporcionar afinidad para algunos procesos, moviendo los otros para balancear la carga.

# Planificador de Múltiples Colas

Debido a los problemas que surgen con el enfoque anterior, muchos sistemas optaron por la utilización de múltiples colas. Se conoce como ***MQMS*** o ***multi-queue multiprocessor scheduling***.

Cada cola seguirá un esquema de planificación particular. Cuando un proceso entra a un sistema, se coloca en una de las colas. Cada planificador es independiente de los otros, lo que nos ahorra problemas de planificación e información. Este enfoque tiene numerosas ventajas. Es más escalable, además de proteger nativamente la afinidad de caché.

Con este enfoque, surge un nuevo problema: ***load imbalance***. La solución obvia para este problemática a la cual nos referimos como ***migración***. Moviendo procesos de un procesador a otro. Muchas veces, una única migración no solucionará el problema, sino que debemos recurrir a una migración continua. Existen muchos patrones de migración.

Para decidir cuando debemos realizar una migración, se puede utilizar la técnica conocida como ***work stealing***. Las colas con pocos trabajos pueden ocasionalmente ojear otras colas, si tiene muchos más procesos que la propia cola, entonces se opta por “robar” un proceso.