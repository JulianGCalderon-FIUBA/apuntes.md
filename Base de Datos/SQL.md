#todo

## Definición de Datos

El comando `CREATE SCHEMA` nos permite crear un nuevo esquema de base de datos dentro de nuestro gestor.

Cada esquema tiene un *dueño*, este será identificado con la opción `AUTHORIZATION`.

Los esquemas se agrupan en catálogos, y cada catálogo contiene un esquema llamado `INFORMATION_SCHEMA`, que describe a todos los esquemas contenidos en él.

### Tipos de Datos

Para las variables numericas, tenemos:

- `INTEGER`: Entero, abreviado `INT`.
- `SMALLINT`: Entero pequeño.
- `FLOAT(n)`: Punto flotante (con aproximaciones).
- `DOUBLE PRECISION`: Punto flotante de alta precisión.
- `NUMERIC(i,j)`: Tipo numérico exacto, sin aproximaciones.

Para las cadenas de caracteres, tendremos:

- `CHARACTER(n)`: De longitud fija, abreviado `CHAR(n)`.
- `CHARACTER VARYING(n)`: De longitud variable, abreviado `VARCHAR(n)`

Para las fechas y horas, tendremos:

- `DATE`: Precisión en días.
- `TIME(i)`: Precisión de hasta microsegundos.
- `TIMESTAMP(i)`: Combina un `DATE` y un `TIME(i)`.

Para booleanos, tendremos:

- `BOOLEAN`: Acepta `TRUE`, `FALSE`, `UNKNOWN`. Se emplea lógica de tres valores.

Otros tipos de dato:

- `GLOB`: Del inglés "Character Large Object". Para documentos de texto de gran extensión.
- `BLOB`: Del inglés "Binary Large Object". paraarchivos binarios de gran extensión.

El usuario a su vez puede definir tipos de datos personalizados, a través del comando `CREATE DOMAIN`. Esto facilita la realización de futuros cambios

### Creación de Tablas

El comando `CREATE TABLE` nos permite definir la estructura de una tabla.

Las columnas pueden ser configuradas con valores por defecto (`DEFAULT`), o autoincrementales (`AUTO_INCREMENT`).

Podemos restringir la posibilidad de que tome un valor nulo (`NOT NULL`), o restringir aún más el conjunto de valores posibles a través de una verificación dinámica (`CHECK`).

La clave primaria se indica con `PRIMARY KEY`. Si está compuesta de una única columna, puede indicarse a continuación del tipo. Con la palabra clave `UNIQUE` se indica que una columna o conjunto de columnas no puede estar repetido (es una manera de identificar claves candidatas).

Las claves foráneas se especifican con `FOREIGN KEY...REFERENCES`. Con las opciones `ON DELETE` y `ON UPDATE` podemos indicar el comportamiento que tiene una clave foránea cuando la tupla a la que refiere es eliminada (o actualizada).

SQL permite que una fila esté repetida muchas veces en una tabla, este concepto se conoce como *multiconjunto*.

## Manipulación de Datos

### Clausula SELECT

El esquema básico de una consulta en SQL es

```SQL
SELECT A1, A2, ..., An
FROM T1, T2, ..., Tm
[WHERE condition];
```

En donde `A1, A2,..., An` es una lista de nombres de columnas, y `T1, T2,..., Tm` es una lista de nombres de tablas, y `condition` es una condición.

Se puede pensar como una proyección de las columnas `Ai` del filtrado oir `condition` del producto cartesiano de las tablas `Ti`.

Las condiciones atómicas admitidas son:

- aa #todo
- bb
- cc

En donde ⊙ debe ser un operador de comparación:

- `=`, `<>`.
- `>`, `>=`, `<`. `<=`.

Varias condiciones atómicas pueden unirse a través de operadores lógicos para formar una condición más compleja. Los operadores permitidos son: `AND`, `OR`, `NOT`.

La proyección no elimina filas repetidas, a menos que agreguemos la opción `DISTINCT`.

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

Y realizar operaciones entre las columnas en el resultado

```SQL
SELECT Producto.precio * 0.90 AS precioDescontado...
```

Las operaciones permitidas son:

- `+`, `-`, `*`, `/`: Operadores matemáticos, solo para columnas numéricas.
- `||`: Para concatenar cadenas
- `+`, `-`: Para sumar o restar tipos de datos temporales.
- `LN`, `EXP`, `POWER`, `LOG`, `SQRT`, `FLOOR`, `CEIL`, `ABS`, etc.

Por último, podemos aplicar una función de agregación a cada una de las columnas del resultado. Las más habituales son:

- `SUM(A)`: Suma los valores de la columna `A` de todas las filas.
- `COUNT([DISTINCT] A|*)`.
	- `COUNT(A)`: Cuenta la cantidad de filas con valor no nulo de la columna `A`.
	- `COUNT(DISTINCT A)`: Cuenta la cantidad de valores distintos (sin tener en cuenta los nulos) de la columna `A`.
	- `COUNT(*)`: Cuenta la cantidad de filas.
- `AVG(A)`: Calcula el promedio de los valores de `A`, descartando los valores nulos.
- `MAX(A)`: Devuelve el máximo de la columna `A`.
- `MIN(A)`: Devuelve el máximo de la columna `A`.
