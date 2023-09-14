El lenguaje SQL (por sus siglas en inglés "Structured Query Language") es hoy en día el estándar para las operaciones de base de datos relacionales

Es tanto un [[Lenguajes|lenguaje]] de definición de datos como un lenguaje de manipulación de datos.

Es no procedural, y está basado en el cálculo relacional de tuplas.

SQL es una gramática libre de contexto (*context-free grammar*, CFG). Esto implica que su sintaxis puede ser descrita a través de reglas de producción.

Una de las notaciones más conocidas para CFG es la notación de Backus-Naur (*Backus-Naur form*, BNF). Esta es la notación adoptada en el estándar.

## Definición de Datos

El comando `CREATE SCHEMA` nos permite crear un nuevo esquema de base de datos dentro de nuestro gestor.

Cada esquema tiene un *dueño*, este será identificado con la opción `AUTHORIZATION`.

Los esquemas se agrupan en catálogos, y cada catálogo contiene un esquema llamado `INFORMATION_SCHEMA`, que describe a todos los esquemas contenidos en él.

SQL no obliga a definir una clave primaria, pero siempre deberíamos hacerlo. Debido a esto, permite que una fila esté repetida muchas veces en una tabla, este concepto se conoce como *multiconjunto*.

Esto difiere del [[Álgebra Relacional]], ya que allí una relación es un conjunto de tuplas y, por lo tanto, no admitía repetidos.

Las claves primarias de una tabla nunca deberían ser `NULL`, aunque algunos motores lo permiten.

## Manipulación de Datos

### Cláusula `SELECT...FROM...WHERE`

La consulta principal de SQL es

```SQL
Select A1, A2, ..., An
FROM T1, T2, ..., TN
[WHERE condition];
```

Es análogo a la siguiente expresión del álgebra relacional:

$$
\Huge\pi_{A_1, A_2, \cdots, A_n} \sigma_\text{condition} (T_1 \times T_2, \cdots, T_m)
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

### Cláusula `JOIN`

Al igual que el álgebra relacional, podemos realizar una junta a partir de la cláusula `JOIN`. Están implementados todos los tipos de junta.

```SQL
...FROM R INNER JOIN S ON condition...
...FROM R INNER JOIN S ON USING(attribute)...
...FROM R NATURAL JOIN S...
...FROM R LEFT OUTER JOIN S ON condition...
...FROM R RIGHT OUTER JOIN S ON condition...
...FROM R FULL OUTER JOIN S ON condition...
```

### Operaciones de Conjuntos

SQL incorpora las tres operaciones de conjuntos. Con la palabra clave `ALL`, el resultado será un multiconjunto.

```SQL
...R UNION [ALL] S...
...R INTERSECT [ALL] S...
...R EXCEPT [ALL] S...
```

Al igual que en el álgebra relacional, las tablas deben ser unión compatibles.

### Ordenamiento y Paginación

Podemos ordenar los resultados de una consulta con `ORDER BY`. Las columnas utilizadas para ordenar deben pertenecer a dominios ordenados, y deben estar incluidas dentro de las columnas de la proyección en la cláusula `SELECT`.

La paginación es la posibilidad de escoger un rango del listado de filas del resultado. Se puede resolver de forma estándar con `OFFSET` y `FETCH`, o en algunos gestores `LIMIT` y `OFFSET`.

```SQL
SELECT A, B
FROM T
ORDER BY A ASC, B DESC
OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;
-- LIMIT 10 OFFSET 10;
```

### Agregación

La agregación colapsa tuplas que coinciden en una serie de atributos, en una única tupla que las representa a todas.

Las columnas agrupadas pueden ser utilizadas en el `SELECT`, mientras que las columnas no agrupadas deben ser utilizadas con una función de agregación.

La cláusula `HAVING` es opcional y nos permite seleccionar solo algunos de los grupos del resultado, basándonos en resultados de funciones de agregación de las columnas no agregadas.

```SQL
SELECT nombre_tenista, COUNT(nombre_torneo), SUM(premio)
FROM Campeones
GROUP BY nombre_tenista
HAVING SUM(premio) >= 100000
```

### Subconsultas

El resultado de una subconsulta puede ser utilizado como argumento a otras cláusulas como `JOIN`.

```SQL
...Tabla JOIN (SELECT ... FROM ...) AS Alias...
```

Para usarse en condiciones, debe tener un solo elemento (única fila y única columna), estar acompañado de operadores como `ANY`, `ALL`, `IN`, `EXISTS`.

```SQL
...WHERE id = (SELECT MAX(id) FROM ...);
...WHERE columna = ANY (SELECT ... FROM ...);
...WHERE columna IN (SELECT ... FROM ...);
...WHERE columna EXISTS (SELECT ... FROM ...);
```
