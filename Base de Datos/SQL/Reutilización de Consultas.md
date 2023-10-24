## Cláusula `WITH`

Es opcional según el estándar, pero permite construir una tabla auxiliar temporal previo a una consulta.

```SQL
WITH Tabla(Col1, Col2, ..., Coln)
AS (SELECT ...)
SELECT ...
```

## Vistas

Si queremos guardar la estructura junto a las tablas, para utilizarse para múltiples consultas, entonces utilizamos `CREATE VIEW` para crear una nueva vista. Se puede hacer referencia a estas vistas como si fuesen una tabla.

```SQL
CREATE VIEW Tabla(Col1, Col2, ..., Coln)
AS (SELECT ...)
```

Las vistas materializadas se guardan en la base de datos ya calculada, lo cual nos ahorra de calcularlo cada vez. El gestor debe actualizar la vista materializada cuando se actualiza la lista, o cada cierto tiempo.

```SQL
CREATE MATERIALIZED VIEW Tabla(Col1, Col2, ..., Coln)
AS (SELECT ...)
```

## Cláusula `WITH RECURSIVE`

Amplía el poder expresivo de SQL, permitiendo encontrar la clausura transitiva de una consulta. Dada una tabla `T` que es entrada de una consulta, permite que el resultado de la misma sea utilizado en lugar de `T` para volver a ejecutar la misma consulta.

Se repite la consulta hasta hallar un punto fijo de nuestra consulta. Esto es, la tabla `T` tal que al aplicarle la consulta, devuelva el mismo `T`.

```SQL
WITH RECURSIVE Tabla(Col1, Col2, ..., Coln)
AS (<valor inicial>) UNION (<subconsulta>)
SELECT ...
```

Dada una relación `Vuelos(codVuelo, ciudadDesde, ciudadHasta)` que indica todos los vuelos que ofrece una aerolínea, podemos encontrar todas las ciudades que son alcanzables desde París, independientemente de la cantidad de escalas.

```SQL
WITH RECURSIVE CiudadesAlcanzables(nombre)
	AS ('Paris')
	UNION (
		SELECT ciudadHasta
		FROM Vuelos JOIN CiudadesAlcanzables
			ON Vuelos.ciudadDesde = CiudadesAlcanzables.ciudad
		)
SELECT ciudad FROM Alcanzables;
```
