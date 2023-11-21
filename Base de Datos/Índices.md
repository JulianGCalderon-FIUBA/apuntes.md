Los índices son estructuras de búsqueda almacenadas y actualizadas por el gestor, que agilizan la búsqueda de registros a partir del valor de una tributo o conjunto de atributos. Pueden implementarse con distintas estructuras de datos:

- Árboles: binarios, B, B+, B*, etc.
- Tablas de Hash.

En los gestores los índices se clasifican en distintos tipos:

- Cuando el índice se construye sobre el campo de ordenamiento clave de un archivo ordenado de registros, se denomina **índice primario**.
- Cuando se construye sobre el campo de ordenamiento del archivo físico, pero este no es clave, el índice se denomina **índice de clustering**.
- Los índices que se construyen sobre campos que no son los campos de ordenamiento del archivo se denominan **índices secundarios**.

> [!note] Observación
> Un archivo solo puede tener un único índice primario o de clustering

## [[Lenguaje SQL]]]

SQL no dispone de una sentencia estándar para la definición de índices, aunque la mayoría de los gestores tienen una sentencia tipo `CREATE INDEX` con la siguiente sintaxis:

```PostgreSQL
CREATE [UNIQUE] INDEX nombreIndice
ON tabla (A1, ..., An);
```

En PostgreSQL no se pueden crear índice de *clustering*, pero sí permite *clusterizar* la tabla manualmente, lo cual se puede ejecutar periódicamente.
