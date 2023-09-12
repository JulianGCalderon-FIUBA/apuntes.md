## Definición de Datos

El comando `CREATE SCHEMA` nos permite crear un nuevo esquema de base de datos dentro de nuestro gestor.

Cada esquema tiene un *dueño*, este será identificado con la opción `AUTHORIZATION`.

Los esquemas se agrupan en catálogos, y cada catálogo contiene un esquema llamado `INFORMATION_SCHEMA`, que describe a todos los esquemas contenidos en él.

### Tipos de Datos

Para las variables numericas, tenemos:

- `INTEGER`: Entero, abreviado `INT`
- `SMALLINT`: Entero pequeño
- `FLOAT(n)`: Punto flotante (con aproximaciones).
- `DOUBLE PRECISION`: Punto flotante de alta precisión
- `NUMERIC(i,j)`: Tipo numérico exacto, sin aproximaciones

Para las cadenas de caracteres, tendremos:

- `CHARACTER(n)`: De longitud fija, abreviado `CHAR(n)`
- `CHARACTER VARYING(n)`: De longitud variable, abreviado `VARCHAR(n)`

Para las fechas y horas, tendremos:

- `DATE`: Precisión en dias.
- `TIME(i)`: Precisión de hasta microsegundos.
- `TIMESTAMP(i)`: Combina un `DATE` y un `TIME(i)`

Para booleanos, tendremos:
- `BOOLEAN`: Acepta `TRUE`, `FALSE`, `UNKNOWN`. Se emplea lógica de tres valores

Otros tipos variados