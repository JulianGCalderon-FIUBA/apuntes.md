La consulta principal de SQL es

```SQL
Select A1, A2, ..., An
FROM T1, T2, ..., TN
[WHERE condition];
```

Es análogo a la siguiente expresión del álgebra relacional:

$$
\large\pi_{A_1, A_2, \cdots, A_n} \sigma_\text{condition} (T_1 \times T_2, \cdots, T_m)
$$

La única diferencia es que SQL no elimina tuplas repetidas, para hacerlo, se debe utilizar `SELECT DISTINCT`.

Si se combinan dos tablas con el mismo nombre, se deben renombrar (además, podemos opcionalmente renombrar las columnas)

```SQL
...FROM Personas AS P1(dni1), Personas AS P2(dni2)...
```

Las columnas pueden ser renombradas y modificadas a partir de una operación elemento a elemento. También se pueden aplicar funciones de agregación a cada columna.

```SQL
Select price * 0.9 as discounted_price, SUM(price) as total...
```

La cláusula `WHERE` permite condiciones de reconocimiento de patrones para cadenas a partir de `LIKE`.

```SQL
...WHERE nombre LIKE 'Ana%'; -- El nombre debe comenzar con Ana.
```

## Cláusula `JOIN`

Al igual que el álgebra relacional, podemos realizar una junta a partir de la cláusula `JOIN`. Están implementados todos los tipos de junta.

```SQL
...FROM R INNER JOIN S ON condition...
...FROM R INNER JOIN S ON USING(attribute)...
...FROM R NATURAL JOIN S...
...FROM R LEFT OUTER JOIN S ON condition...
...FROM R RIGHT OUTER JOIN S ON condition...
...FROM R FULL OUTER JOIN S ON condition...
```

## Operaciones de Conjuntos

SQL incorpora las tres operaciones de conjuntos. Con la palabra clave `ALL`, el resultado será un multiconjunto.

```SQL
...R UNION [ALL] S...
...R INTERSECT [ALL] S...
...R EXCEPT [ALL] S...
```

Al igual que en el álgebra relacional, las tablas deben ser unión compatibles.

## Ordenamiento y Paginación

Podemos ordenar los resultados de una consulta con `ORDER BY`. Las columnas utilizadas para ordenar deben pertenecer a dominios ordenados, y deben estar incluidas dentro de las columnas de la proyección en la cláusula `SELECT`.

La paginación es la posibilidad de escoger un rango del listado de filas del resultado. Se puede resolver de forma estándar con `OFFSET` y `FETCH`, o en algunos gestores `LIMIT` y `OFFSET`.

```SQL
SELECT A, B
FROM T
ORDER BY A ASC, B DESC
OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;
-- LIMIT 10 OFFSET 10;
```

## Agregación

La agregación colapsa tuplas que coinciden en una serie de atributos, en una única tupla que las representa a todas.

Las columnas agrupadas pueden ser utilizadas en el `SELECT`, mientras que las columnas no agrupadas deben ser utilizadas con una función de agregación.

La cláusula `HAVING` es opcional y nos permite seleccionar solo algunos de los grupos del resultado, basándonos en resultados de funciones de agregación de las columnas no agregadas.

```SQL
SELECT nombre_tenista, COUNT(nombre_torneo), SUM(premio)
FROM Campeones
GROUP BY nombre_tenista
HAVING SUM(premio) >= 100000
```

## Subconsultas

El resultado de una subconsulta puede ser utilizado como argumento a otras cláusulas como `JOIN`.

```SQL
...Tabla JOIN (SELECT ... FROM ...) AS Alias...
```

Para usarse en condiciones, debe tener un solo elemento (única fila y única columna), o estar acompañado de operadores como `ANY`, `ALL`, `IN`, `EXISTS`. En estos casos, debe tener misma cantidad de columnas.

```SQL
...WHERE id = (SELECT MAX(id) FROM ...);
...WHERE columna = ANY (SELECT ... FROM ...);
...WHERE columna IN (SELECT ... FROM ...);
...WHERE columna EXISTS (SELECT ... FROM ...);
```

Las subconsultas, de hecho, pueden estar en cualquier lugar. Podríamos, por ejemplo, usar una subconsulta como expresión del `SELECT`. Es importante notar que cuando se usa como un valor, debe tener un solo elemento.

```SQL
SELECT id, (SELECT nombre FROM ...) FROM ...
```

Cuando una subconsulta hace referencia a un valor externo, se dice que están **correlacionadas**. El costo de este tipo de consultas es mucho más elevado, ya que debe repetir la consulta por cada tupla de la consulta padre.

## Estructura `CASE`

Nos permite agregar cierta lógica de la programación estructurada a una sentencia de SQL.

Permite seleccionar distintos valores posibles de salida en función de distintas condiciones.

```SQL
SELECT CASE WHEN ... THEN ... ELSE ... END
FROM ...
```
