Un sistema de gestión de bases de distribuido es aquel que corre como sistema distribuido en distintas computadoras (nodos) que se encuentran sobre una red, aprovechando las ventajas de la computación distribuida y brindando a las aplicaciones la abstracción de ser un único sistema coherente.

En un [[Modelo Relacional]], las operaciones de junta entre datos que se encuentran en nodos distintos puede ser un problema. Por otro lado, garantizar las [[Transacción#Propiedades ACID|propiedades ACID]] en un sistema distribuido es difícil, necesitamos que los nodos se sincronicen entre sí. Si bien es posible distribuir una base de datos relacional, tiene diversas dificultades.

Desde los últimos años, la velocidad de las redes y la capacidad de almacenamiento aumenta, mientras que el procesamiento se mantiene estancado. Debido a esto, las bases de datos *"noSQL"* utilizará un modelo de [[Bases de Datos Distribuida]] donde no fragmentarán los datos, sino que los replicaran.

Hay distintos problemas que debo resolver cuando diseñamos una base de datos distribuida:

- Fragmentación.
- Replicación.
- Búsqueda, o *lookup*.
- [[Consistencia]].
- Métodos de acceso.

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
