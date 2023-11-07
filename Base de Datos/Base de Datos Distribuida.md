Un sistema de gestión de bases de distribuido es aquel que corre como sistema distribuido en distintas computadoras (nodos) que se encuentran sobre una red, aprovechando las ventajas de la computación distribuida y brindando a las aplicaciones la abstracción de ser un único sistema coherente.

En un [[Modelo Relacional]], las operaciones de junta entre datos que se encuentran en nodos distintos puede ser un problema. Por otro lado, garantizar las [[Transacción#Propiedades ACID|propiedades ACID]] en un sistema distribuido es difícil, necesitamos que los nodos se sincronicen entre sí. Si bien es posible distribuir una base de datos relacional, tiene diversas dificultades.

Desde los últimos años, la velocidad de las redes y la capacidad de almacenamiento aumenta, mientras que el procesamiento se mantiene estancado. Debido a esto, las bases de datos *"noSQL"* utilizará un modelo de [[Base de Datos Distribuida]] donde no fragmentarán los datos, sino que los replicaran.

Hay distintos problemas que debo resolver cuando diseñamos una base de datos distribuida:

- [[Replicación]]
- [[Base de Datos/Fragmentación|Fragmentación]]
- [[Búsqueda]]
- [[Consistencia]]
