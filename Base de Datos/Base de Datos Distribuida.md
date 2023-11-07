Un sistema de gestión de bases de distribuido es aquel que corre como sistema distribuido en distintas computadoras (nodos) que se encuentran sobre una red, aprovechando las ventajas de la computación distribuida y brindando a las aplicaciones la abstracción de ser un único sistema coherente.

En un [[Modelo Relacional]], las operaciones de junta entre datos que se encuentran en nodos distintos puede ser un problema. Por otro lado, garantizar las [[Transacción#Propiedades ACID|propiedades ACID]] en un sistema distribuido es difícil, necesitamos que los nodos se sincronicen entre sí. Si bien es posible distribuir una base de datos relacional, tiene diversas dificultades.

Desde los últimos años, la velocidad de las redes y la capacidad de almacenamiento aumenta, mientras que el procesamiento se mantiene estancado. Debido a esto, las bases de datos *"noSQL"* utilizará un modelo de [[Base de Datos Distribuida]] donde no fragmentarán los datos, sino que los replicaran.

Hay distintos problemas que debo resolver cuando diseñamos una base de datos distribuida:

## Fragmentación

La fragmentación es la tarea de dividir un conjunto de agregados entre un conjunto de nodos. Se realiza con dos objetivos:

- Almacenar conjuntos muy grandes de datos que de lo contrario no podrían caber en un único nodo.
- Paralelizar el procesamiento, permitiendo que cada nodo ejecute una parte de las consultas para luego integrar los resultados.

Según la manera de fragmentar, podemos distinguir entre:

- **Fragmentación horizontal:** Los agregados se reparten entre los nodos, de manera que cada nodo almacena un subconjunto de agregados. Generalmente, se asigna el nodo a partir del valor de alguno de los atributos del agregado.
- **Fragmentación vertical:** Distintos nodos guardan un subconjunto de atributos para cada agregado. Todos suelen compartir los atributos que conforman la clave.

Muchas veces, se utiliza una combinación de ambas.

## Replicación

La replicaciones es el proceso por el cual se almacenan múltiples copias de un mismo dato en distintos nodos del sistema. Nos brinda varias ventajas:

- **Es un mecanismo de backup**, permite recuperar el sistema en caso de fallas de disco o catastróficas.
- **Permite repartir la carga** de procesamiento si permitimos que las réplicas respondan consultas o actualizaciones.
- **Garantiza cierta disponibilidad** del sistema aun si se caen algunos nodos.

Cuando las réplicas solo funcionan como mecanismo de *backup* se denominan réplicas secundarias. Cuando también pueden hacer procesamiento, se las conoce como réplicas primarias.

La replicación nos genera un nuevo problema a resolver: la consistencia de los datos. Puede darse la situación de que distintas réplicas almacenen (al menos, temporalmente) distintos valores para un mismo dato.

## Búsqueda

Debemos tener tablas de hash distribuidas (DHT's) que permiten definir en que nodo se encontrará cierta información particular.

Este método no requiere de muchos cambios a medida que yo agrego información.

Para las consultas comunes, utilizamos las **tablas de hash distribuidas**. Para otras consultas más analíticas que requieren analizar mucha información, podremos no utilizarla y consultarle a todos los nodos.

Una forma de implementar una tabla de hash distribuida es a partir del modelo de [[Hashing Consistente]].

## Consistencia

Es necesario que la información entre los distintos nodos de un sistema distribuido sean consistenes.

Hay distintas técnicas que solucionan el problema de la consistencia, como:

### Consistencia Secuencial

En el estudio de la replicación en las bases de datos distribuidas, se utilizan distintos modelos de consistencia.

Uno de los modelos más fuertes, y que proviene de las bases de datos centralizadas, es el de consistencia secuencial.

Partimos de una serie de procesos que ejecutan instrucciones de lectura $R_{P_i}(X)$ y de escritura $W_{P_i}(X)$, sobre una base de datos distribuida.

Se dice que una base de datos distribuida tiene consistencia secuencial cuando "el resultado de cualquier ejecución concurrente de los procesos es equivalente al de alguna ejecución secuencial en que las instrucciones de los procesos se ejecutan una después de otra". Esto no implica serializabilidad, pues las transacciones no deben ser solapadas.

Este tipo de consistencia va en contra de la disponibilidad, pues es un modelo muy restrictivo.

### Consistencia Causal

En el modelo de consistencia causal se busca capturar eventos que puedan estar causalmente relacionados.

Si un evento $b$ fue influenciado por un evento $a$, la causalidad requiere que todos vean al evento $a$ antes que al evento $b$. Dos eventos que no están causalmente correlacionados se dicen concurrentes, y no es necesario que sean vistos por todos en el mismo orden.

En este modelo, "dos escrituras que están potencialmente causalmente relacionadas deben ser vistas por todos en el mismo orden".

### Consistencia Eventual

El modelo de consistencia eventual está basado en la siguiente observación: "En la mayoría de los sistemas reales, son pocos los procesos que realizan modificaciones o escrituras, mientras que la mayor parte solo lee, ¿Qué tan rápido necesitamos que las actualizaciones de un proceso que escribe sean vistos por los procesos que leen?"

Estas situaciones pueden tolerar un grado bastante más alto de inconsistencia.

Decimos entonces que una ejecución tiene consistencia eventual cuando "si en el sistema no se producen modificaciones (escrituras) por un tiempo suficientemente grande, entonces eventualmente todos los procesos verán los mismos valores".

En otras palabras, esto implica que eventualmente todas las réplicas llegaran a ser consistentes.
