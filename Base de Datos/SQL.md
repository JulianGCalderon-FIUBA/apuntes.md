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

