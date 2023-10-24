## Creación de Esquemas

El comando `CREATE SCHEMA` nos permite crear un nuevo esquema de base de datos dentro de nuestro gestor.

Cada esquema tiene un *dueño*, este será identificado con la opción `AUTHORIZATION`.

Los esquemas se agrupan en catálogos, y cada catálogo contiene un esquema llamado `INFORMATION_SCHEMA`, que describe a todos los esquemas contenidos en él.

Para eliminar un esquema, utilizamos `DROP SCHEMA`.

## Creación de Tablas

El comando `CREATE TABLE` nos permite definir la estructura de una tabla

```SQL
CREATE TABLE Alumno (
	padron INT PRIMARY KEY
	nombre VARCHAR(255)
	facultad INT FORIEGN KEY REFERENCES Facultad(id)
)
```

SQL no obliga a definir una clave primaria, pero siempre deberíamos hacerlo. Debido a esto, permite que una fila esté repetida muchas veces en una tabla, este concepto se conoce como *multiconjunto*.

Esto difiere del [[Álgebra Relacional]], ya que allí una relación es un conjunto de tuplas y, por lo tanto, no admitía repetidos.

Las claves primarias de una tabla nunca deberían ser `NULL`, aunque algunos motores lo permiten.

Para eliminar una tabla, utilizamos `DROP TABLE`.
