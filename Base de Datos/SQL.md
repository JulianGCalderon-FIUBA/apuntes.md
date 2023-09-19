El lenguaje SQL (por sus siglas en inglés "Structured Query Language") es hoy en día el estándar para las operaciones de base de datos relacionales

Es tanto un [[Lenguajes]] de definición de datos como un lenguaje de manipulación de datos.

Es un lenguaje no procedural, y está basado en el [[Cálculo Relacional]] de tuplas.

SQL es una gramática libre de contexto (*context-free grammar*, CFG). Esto implica que su sintaxis puede ser descrita a través de reglas de producción.

Una de las notaciones más conocidas para CFG es la notación de Backus-Naur (*Backus-Naur form*, BNF). Esta es la notación adoptada en el estándar.

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

## Cláusula `SELECT...FROM...WHERE`

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

Dado una relación `Vuelos(codVuelo, ciudadDesde, ciudadHasta)` que indica todos los vuelos que ofrece una aerolínea, encuentre todas las ciudades que son alcanzables desde París, independientemente de la cantidad de escalas.

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

## Estructura `CASE`

Nos permite agregar cierta lógica de la programación estructurada a una sentencia de SQL.

Permite seleccionar distintos valores posibles de salida en función de distintas condiciones.

```SQL
SELECT CASE WHEN ... THEN ... ELSE ... END
FROM ...
```

## Funciones de Ventana

Permiten aplicar un procesamiento final a los resultados de una consulta, siguiendo una serie de pasos:

1. Se dividen en grupos, llamados particiones
2. Cada partición se ordena internamente
3. Se cruza información entre las filas de cada partición

A cada atributo del `SELECT` de una consulta se le puede aplicar una función de ventana distinta, o no aplicarle función a alguna.

Esto permite agregar información según el ordenamiento de las filas de la tabla.

### Única Partición

El esquema básico es el siguiente, donde se puede utilizar una función de agregación `f(A)` o una función de ventana `w(A_i,...)`.

```SQL
SELECT atleta, RANK() OVER(ORDER BY tiempo DESC)
FROM ...
```

Esto agrega a cada fila del resultado, una columna dependiente de dicha fila y su orden respecto al resto de filas. Si no se utiliza `ORDER BY` dentro de `OVER`, se tendrá un orden indefinido y probablemente, un comportamiento indeseado.

Existen múltiples funciones de ventana, como `RANK`, `ROW_NUMBER`, `LAG`, etc.

A diferencia del `GROUP BY`, no agrupa. No cambiará la cantidad de filas en el resultado.

La función de ventana se aplica antes del ordenamiento que pueda hacerse en la cláusula `ORDER BY`.

Para el caso de las funciones de agregación, se aplica únicamente para las filas anteriores a la fila actual, según el orden propuesto.

Si vamos a utilizar una misma ventana múltiples veces, podemos definirla con `WINDOW`.

```SQL
SELECT atelta, RANK() OVER ventana_tiempo
FROM ...
WINDOW ventana_tiempo AS (ORDER BY tiempo DESC)
```

### Múltiples Particiones

En un esquema con múltiples particiones, antes de aplicar cada ventana, se puede agrupar el resultado por el valor de un conjunto de atributos. A cada uno de estos grupos, se lo denomina partición.

```SQL
SELECT pais, producto, RANK() OVER(ORDER BY ...)
FROM ...
```

Para cada producto, se calcula su posición respecto al resto de países, ordenando por cantidad de exportaciones. Se puede pensar como una agrupación dentro de una ventana.

## Inserciones

Las inserciones se realizan con el comando `INSERT INTO`. Si no especificamos las columnas, debemos colocar todas y en el orden definido. Se deben respetar las restricciones definidas.

```SQL
INSERT INTO Tabla VALUES
	(a1, a2, ..., an),
	(b1, b2, ..., bn),
	...

INSERT INTO Tabla(Col1, Col2, ..., Col3) VALUES
	(a1, a2, ..., an),
	(b1, b2, ..., bn),
	...
```

También, podemos insertar el resultado de una subconsulta, con

```SQL
INSERT INTO T(Col1, Col2, ..., Col3)
SELECT ...
```

Si se alcanza a un error, se deshace la operación completa.

## Eliminaciones

El borrado se realiza con el comando `DELETE FROM`. Se deben respetar las restricciones definidas.

```SQL
DELETE FROM Tabla
WHERE ...
```

Si se alcanza a un error, se deshace la operación completa.

## Modificaciones

La actualización se realiza con el comando `UPDATE`. Se deben respetar las restricciones definidas.

```SQL
UPDATE Tabla
SET A1=c1, A2=c2, Ak=ck
WHERE ...
```

Se pueden modificar muchas filas con un solo `UPDATE`.

Si se alcanza a un error, se deshace la operación completa.
