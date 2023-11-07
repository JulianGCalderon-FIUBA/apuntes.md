Son una evolución de los [[Gestores de Clave Valor]], ya que agrupan los pares vinculados a una misma entidad como columnas asociadas a una misma clave primaria.

Un valor particular de la clave primaria junto con todas sus columnas asociadas forma un agregado análogo a la fila de una tabla. Pero además, estas bases permiten agregar conjuntos de columnas en forma dinámica a una fila, convirtiéndola en un agregado llamado **wide row**.

Esta dinámica podría representar las interrelaciones de la entidad con otra entidad.

Los gestores de este estilo mas conocidos son:

- Google BigTable
- Apache HBase
- Apache Cassandra

## Cassandra

Surgio en Facebook en 2008, y en 2009 fue adquirida por Apache. Actualmente, es utilizada po Facebook, Twitter, Netflix.

A diferencia de gestores como [[Gestores Orientados a Documentos#MongoDB|MongoDB]], el esquema de las tablas está definido, por lo que no se puede agregar datos de cualquier forma.

No es estrictamente orientada a columnas. La organización de los datos es por fila o *wide row*.

Utiliza una arquitectura llamada **share-nothing**. No existe un estado compartido centralizado, ni un controlador, ni una arquitectura maestro-esclavo. Todos los nodos son pares. Esto nos permite ofrecer mucha escalabilidad.

### Esquema

Cada **keyspace** puede estar distribuido en varios nodos de nuestro *cluster*.

El concepto análogo al de la tabla es el de **column family**.

Una fila está formada por una clave compuesta, y un conjunto de pares clave valor (o columnas).

### Wide Columns

La idea es que las columnas de una fila puedan variar dinámicamente en función de las necesidades. Es necesario indicar cuáles son las columnas que se pueden repetir.

Cuando en una fila las columnas se repiten identificadas por el valor que toman las columnas clave, se dice que la fila se convirtió en una **wide row**. Dentro de una misma **wide row**, se pueden pensar a las columnas dinámicas como sus filas.

![[Gestores Wide Column 1699391317.png|525]]
