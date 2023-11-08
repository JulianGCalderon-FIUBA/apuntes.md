Son una evolución de los [[Gestores de Clave Valor]], ya que agrupan los pares vinculados a una misma entidad como columnas asociadas a una misma clave primaria.

Un valor particular de la clave primaria junto con todas sus columnas asociadas forma un agregado análogo a la fila de una tabla.

Además, estas bases permiten agregar conjuntos de columnas en forma dinámica a una fila, convirtiéndola en un agregado llamado **wide row**, aunque por motivos históricos, quedó *wide column*.

Los gestores de este estilo más conocidos son:

- [[Apache Cassandra]]
- Google BigTable
- Apache HBase
