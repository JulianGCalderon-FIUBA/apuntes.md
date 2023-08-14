Los Archivos y bases de datos nos permiten que la información del sistema persista, cuando hablamos de modelado de datos, hablamos de tres niveles:

- **Conceptual:** Como un MDD, nos muestra las entidades y sus relaciones con otras entidades. No tiene nada que ver con la implementación, sino con el concepto
- **Lógico:** Diseño lógico de la base de datos/archivos. Debemos definir las tablas, las columnas, las claves primarias y foráneas.
- **Físico**: Implementación de la base de datos: índices, espacios de almacenamiento, seguridad, etc.

## Bases de Datos

Una base de datos es una colección ordenada de datos administrada por un sistema de gestión (DBMS, Database Management System)

### Modelos de Base de Datos

Existen distintos modelos conocidos de base de datos:

- **Jerárquico:** Una fila de cabecera (master), y el detalle de los elementos de la base de datos (detail)
- **De Red:** Similar, pero sin necesidad de navegar la jerarquía, se puede navegar de un registro a otro
- **Relacional:** Tablas relacionadas entre sí, por otras tablas:
	- Las claves primarias identifican las distintas filas (instancias) en una tabla
	- Las claves foráneas referencian a claves primarias de otras tablas y son empleadas para implementar las relaciones

	![[Diseno de Datos 1.png|525]]

- **Orientadas a** **Objetos:**
- **Orientadas a Documento:** no estructuradas

## De Modelo de Dominio a Base de Datos

- Una tabla por cada objeto de dominio
- Una tabla para cada superclase y subclase o una tabla para cada una
	- Tendremos una única tabla, con un identificador de tipo para determinar a qué subclase pertenece la entrada
	- Una tabla por cada variante, utilizando la misma clave foránea en la subclase que refieren a la clave primaria de las primarias.
- Implementar las asociaciones:
	- One-Many
	- One-One
	- Many-Many
	- Recursivas
	- Asociativas

### One-Many

El lado de **Many** mantiene referencia al **One** a partir de una clave foránea

![[Diseno de Datos 2.png|525]]

### One-One

Decidimos una tabla como más relevante, e incluimos la **foránea** en la otra

### Many-Many

Crear una tabla de correlación cuyas columnas serán las claves primarias de las tablas relacionadas. Los identificadores serán tanto claves, primarias como foráneas

![[Diseno de Datos 3.png|550]]

### Recursivas

Para cualquier tipo de cardinalidad, tendremos una tabla de correlación que una dos claves de la misma tabla.

### Asociativas

Necesitaremos una tabla asociación con atributos propios de la asociación

## Normalización

Buscamos evitar la redundancia de datos, la normalización es una herramienta para eliminar la redundancia. Debemos verificar tres reglas:

1. No hay atributos repetitivos
2. En registros con claves compuestas, todos los atributos no clave son funcionalmente dependientes de toda la clave
3. Todos los atributos son funcionalmente dependientes de la clave, no hay dependencias transitivas
