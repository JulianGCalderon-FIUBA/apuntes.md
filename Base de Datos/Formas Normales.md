Las formas normales son una serie de estructuras con las que un esquema de base de datos puede cumplir o no.

Las formas normales clásicas son:

- Primera forma normal: **1FN**
- Segunda forma normal: **2FN**
- Tercera forma normal: **3FN**
- Forma normal Boyce-Codd: **FNBC**
- Cuarta forma normal: **4FN**
- Quinta forma normal: **5FN**

Cada forma normal es más fuerte que las anteriores. El cumplimiento de cualquier forma implica el cumplimiento de las anteriores.

En 1972, E. Codd propuso el concepto de normalización como el proceso a través del cual se convierte un esquema de base de datos en uno equivalente, y que cumple con una determinada forma normal.

Para normalizar una nueva relación, debemos partir de un conjunto de dependencias funcionales asociado que supondremos definido por el diseñador de la base de datos. Normalmente, este conjunto se denota con $F$.

## Primera Forma Normal

Un esquema de base de datos está en 1FN cuando los dominios de todos sus atributos solo permiten valores atómicos y monovaluados.

Actualmente, se considera que en el modelo relacional todos los atributos deben ser monovaludados y atómicos. Con este criterio, todo esquema relacional está ya en 1FN.

Si no es el caso, y el esquema tiene atributos multivaluados, entonces tendremos tres soluciones:

1. Colocar una tupla nueva por cada valor, repitiendo los otros atributos.
2. Suponer un máximo de valores, y colocar un atributo por cada uno.
3. Crear una nueva relación $1-n$, que relacione la tupla original con cada uno de los valores.

## Segunda Forma Normal

Una dependencia formal $X \to Y$ es **parcial** cuando existe un subconjunto propio $A \subset X, A \neq X$, para el cual $A \to Y$. Una dependencia funcional es **completa** si y solo si no es parcial.

Un atributo primo de una relación es aquel que es parte de alguna clave candidata de la relación. Decimos que una relación está en 2FN cuando todos sus atributos no primos tienen dependencia funcional completa de las claves candidatas.

Sea $R$ una relación que no está en 2FN. Luego, tendrá un conjunto de atributos $A$ no primos, tal que este tiene dependencia funcional completa de $B$, donde $B$ es un subconjunto de una clave candidata $C$. Esto nos obliga a incluir $A$ cada vez que está $B$, incluso si esto se repite en múltiples tuplas.

Para resolverlo, debemos generar una nueva relación $S$ con clave primaria $B$ y atributos $A \cup B$, y eliminar $A$ de la relación $R$.

Supongamos una tabla $\text{Docencia}(\text{Asignatura}, \text{Profesor}, \text{Departamento})$, donde la asignatura y el profesor son claves primarias, y el departamento depende de forma completa de la asignatura. Si yo quiero representar que un nuevo profesor da una asignatura, debo incluir el departamento (información redundante, ya que ya está en otras tuplas de la misma relación).

Para solucionarlo, debo generar una nueva tabla que permita abstraer esta información: $\text{Asignaturas}(Asignatura, Departamento)$. Luego, la tabla de docencia se vería como $\text{Docencia}(\text{Asignatura}, \text{Profesor})$. Para agregar un nuevo profesor a una materia, ahora no debo repetir el departamento.

## Tercera Forma Normal

Una dependencia formal $X \to Y$ es **transitiva** si existe un $Z$ tal que $X \to Z$ y $Z \to Y$. Siendo $Z \to Y$ no trivial, $X \to Y$ no trivial, y $ Z \not\to X$.
Todas las dependencias funcionales parciales no triviales son transitivas.

Decimos que una relación está en 3FN cuando todos sus atributos no primos tienen dependencia funcional transitiva de las claves candidatas.

Una definición equivalente es que para toda dependencia funcional no trivial $X \to Y$, o bien $X$ es superclave, o bien $Y - X$ solo contiene atributos primos.

Sea $R$ una relación que no está en 3FN. Luego, tendrá un conjunto de atributos $A$ no primos, tal que este tiene dependencia completa de $B$, donde $B$ es un conjunto de atributos no perteneciente a una clave candidata, pero que tiene dependencia funcional de una clave candidata $C$. Esto nos obliga a incluir $A$ cada vez que está $B$, incluso si se repite en múltiples tuplas.

Para resolverlo, debemos generar una nueva relación $S$ con clave primaria $B$ y atributos $A \cup B$, y eliminar $A$ de la relación $R$.