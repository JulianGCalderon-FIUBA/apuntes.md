Debemos tener tablas de hash distribuidas (DHT's) que permiten definir en que nodo se encontrará cierta información particular.

Este método no requiere de muchos cambios a medida que yo agrego información.

Para las consultas comunes, utilizamos las **tablas de hash distribuidas**. Para otras consultas más analíticas que requieren analizar mucha información, podremos no utilizarla y consultarle a todos los nodos.

Una forma de implementar una tabla de hash distribuida es a partir del modelo de [[Hashing Consistente]].
