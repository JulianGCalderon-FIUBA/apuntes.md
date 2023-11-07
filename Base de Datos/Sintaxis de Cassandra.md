## Definición de Datos

Creamos un nuevo **keyspace** con la siguiente instrucción en CQL.

```CQL
CREATE KEYSPACE empresa_db
WITH replication = {
	'class': 'SimpleStrategy',
	'replication_factor': 1
}
```

Asignamos este **keyspace** como aquel por defecto

```CQL
USE empresa_db
```

Luego, podemos crear una **column family**.

```CQL
CREATE COLUMNFAMILY clientes (
	cuit int,
	nombre text,
	domicilio text,
	primary key (cuit));
)
```

Es obligatoria definir una clave primaria.
