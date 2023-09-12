El lenguaje SQL (por sus siglas en inglés "Structured Query Language") es hoy en día el estándar para las operaciones de base de dstos relacionales

Es tanto un [[Lenguajes|lenguaje]] de definición de datos como un lenguaje de manipulación de datos.

Es no procedural, y está basado en el cálculo relacional de tuplas.

SQL es una gramática libre de contexto (context-free grammar, CFG). Esto implica que su sintaxis puede ser descrita a través de reglas de producción.

Una de las notaciones más conocidas para CFG's es la notación de Backus-Naur (Backus-Naur form, BNF). Esta es la notación adopata en el estandar.

## Definición de Datos

El comando `CREATE SCHEMA` nos permite crear un nuevo esquema de base de datos dentro de nuestro gestor.

Cada esquema tiene un *dueño*, este será identificado con la opción `AUTHORIZATION`.

Los esquemas se agrupan en catálogos, y cada catálogo contiene un esquema llamado `INFORMATION_SCHEMA`, que describe a todos los esquemas contenidos en él.

SQL no obliga a definir una clave primaria, pero siempre deberiamos hacerlo. Debido a esto, permite que una fila esté repetida muchas veces en una tabla, este concepto se conoce como *multiconjunto*. Esto difiere del [[Álgebra Relacional]], ya que allí una relación es un conjunto de tuplas y, por lo tanto, no admitia repetidos.

Las claves primarias de una tabla nunca deberían ser `NULL`, aunque algunos motores lo permiten.

## Manipulación de Datos

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

Las columnas y las tablas pueden ser renombradas

```SQL
Select Person
```
