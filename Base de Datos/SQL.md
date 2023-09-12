El lenguaje SQL (por sus siglas en ingles "Structured Query Language") es hoy en dia el estándar para las operaciones de base de dstos relacionales

Es tanto un [[Lenguajes|lenguaje]] de definición de datos como un lenguaje de manipulación de datos.

Es no procedural, y esta basado en el cálculo relacional de tuplas.

SQL es una gramática libre de contexto (context-free grammar, CFG). Esto implica que su sintaxis puede ser descrita a través de reglas de producción.

Una de las notaciones más conocidas para CFG's es la notación de Backus-Naur (Backus-Naur form, BNF). Esta es la notación adopata en el estandar.

## Definición de Datos

El comando `CREATE SCHEMA` nos permite crear un nuevo esquema de base de datos dentro de nuestro gestor.

Cada esquema tiene un *dueño*, este será identificado con la opción `AUTHORIZATION`.

Los esquemas se agrupan en catálogos, y cada catálogo contiene un esquema llamado `INFORMATION_SCHEMA`, que describe a todos los esquemas contenidos en él.

SQL no obliga a definir una clave primaria, pero siempre deberiamos hacerlo. Debido a esto, permite que una fila esté repetida muchas veces en una tabla, este concepto se conoce como *multiconjunto*. Esto difiere del [[Álgebra Relacional]], ya que allí una relación es un conjunto de tuplas y, por lo tanto, no admitia repetidos.

Las claves primarias de una tabla nunca deberían ser `NULL`, aunque algunos motores lo permiten.

## Manipulación de Datos

### Cláusula `SELECT`

El esquema básico de una consulta en SQL es

```SQL
SELECT A1, A2, ..., An
FROM T1, T2, ..., Tm
[WHERE condition];
```

En donde `A1, A2,..., An` es una lista de nombres de columnas, y `T1, T2,..., Tm` es una lista de nombres de tablas, y `condition` es una condición.

Se puede pensar como una proyección de las columnas `Ai` del filtrado por `condition` del producto cartesiano de las tablas `Ti`.

Las condiciones atómicas admitidas son:

- `A1 ⊙ A2`.
- `A ⊙ c`, con `c` una constante perteneciente al dominio de `A`.
- `A [NOT] LIKE p`, donde `A1` es una cadena, y `p` un patrón.
- `(A1, A2,..., An) [NOT] IN m`, donde `m` es un conjunto o multiconjunto.
- `A [NOT] BETWEEN a AND b`, con `a` y `b` en el dominio de `A`.
- `A IS [NOT] NULL`.
- `EXISTS T`.
- `A ⊙ [ANY|ALL] T`.

En donde ⊙ debe ser un operador de comparación:

- `=`, `<>`.
- `>`, `>=`, `<`. `<=`.

Varias condiciones atómicas pueden unirse a través de operadores lógicos para formar una condición más compleja. Los operadores permitidos son: `AND`, `OR`, `NOT`.

### Eliminación de Repetidos

La proyección no elimina filas repetidas, a menos que agreguemos la opción `DISTINCT`.

### Alias de Tablas o Columnas

En la cláusula `FROM` es posible indicar un alias para las tablas

```SQL
...FROM Persona p...
...FROM Persona AS p...
```

Cuando se selecciona una columna, si la misma es ambigua, se deberá indicar el nombre de la tabla o su alias.

Es posible cambiar el nombre de las columnas en el resultado

```SQL
SELECT p1.nombre AS NPadre, p2.nombre AS NHijo
```

### Operaciones por Columna

Se pueden realizar operaciones entre las columnas en el resultado

```SQL
SELECT Producto.precio * 0.90 AS precioDescontado...
```

Las operaciones permitidas son:

- `+`, `-`, `*`, `/`: Operadores matemáticos, solo para columnas numéricas.
- `||`: Para concatenar cadenas
- `+`, `-`: Para sumar o restar tipos de datos temporales.
- `LN`, `EXP`, `POWER`, `LOG`, `SQRT`, `FLOOR`, `CEIL`, `ABS`, etc.

### Agregación por Columnas

Por último, podemos aplicar una función de agregación a cada una de las columnas del resultado. Las más habituales son:

- `SUM(A)`: Suma los valores de la columna `A` de todas las filas.
- `COUNT([DISTINCT] A|*)`.
	- `COUNT(A)`: Cuenta la cantidad de filas con valor no nulo de la columna `A`.
	- `COUNT(DISTINCT A)`: Cuenta la cantidad de valores distintos (sin tener en cuenta los nulos) de la columna `A`.
	- `COUNT(*)`: Cuenta la cantidad de filas.
- `AVG(A)`: Calcula el promedio de los valores de `A`, descartando los valores nulos.
- `MAX(A)`: Devuelve el máximo de la columna `A`.
- `MIN(A)`: Devuelve el máximo de la columna `A`.

### Reconocimiento de Patrones

La cláusula `WHERE` también permite condiciones de reconocimiento de patrones para columnas que son *strings* a través de `LIKE`. Si queremos ignorar las mayúsculas, utilizamos `ILIKE`.

```SQL
...WHERE attrib LIKE pattern;
```

Se acepta como patrón una secuencia de caracteres delimitada por comillas, combinada con los siguientes caracteres especiales:

- `_`: Representa un carácter arbitrario.
- `%`: Representa cero o más caracteres arbitrarios.

### Cláusula `JOIN`

SQL también implementa las operaciones de junta a través del operador `JOIN`.

```SQL
...FROM R INNER JOIN S ON condition... 
...FROM R INNER JOIN S USING(attribute)...
```

Si no especifico una condición o atributo, se utiliza una junta natural

```SQL
...FROM R NATURAL JOIN S...
```

Para utilizar una junta externa, utilizamos respectivamente:

```SQL
...FROM R LEFT OUTER JOIN S...
...FROM R RIGHT OUTER JOIN S...
...FROM R FULL OUTER JOIN S...
```

### Operaciones de Conjuntos

SQL incorpora las tres operaciones de conjuntos:

```SQL
...R UNION [ALL] S...
...R INTERSECT [ALL] S...
...R EXCEPT [ALL] S...
```

Pero debemos tener en cuenta que:

- Las tablas pueden provenir a su vez de una subconsulta
- las tablas deben ser **union compatibles**.
- Si no se agrega la palabra clave `ALL`, el resultado será un conjunto en lugar de un multiconjunto.
