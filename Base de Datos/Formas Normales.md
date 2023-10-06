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

Para normalizar una nueva relación, debemos partir de un conjunto de [[Dependencias Funcionales]] asociado que supondremos definido por el diseñador de la base de datos. Normalmente, este conjunto se denota con $F$.

## Descomposición

Partimos del concepto de la relación universal $R(\overline A)$. Esta engloba todos los atributos del mundo real que nuestro modelo representa.

Dada una relación universal $R$ y un conjunto de dependencias funcionales $F$ asociado, decimos que el conjunto de relaciones $\{ R_1(\overline B_1), \cdots, R_n(\overline B_n)\}$ es una descomposición de $R$ cuando todos los atributos de la relación $R$ se conservan.

$$
\bigcup_{i=1}^n A_i = \bigcup_{i=1}^m\bigcup_{j=1}^{n_i} B_{ij}
$$

Si una descomposición cumple que para toda instancia posible de $R$, la junta de las proyecciones sobre $R_i$ permite recuperar la misma instancia de relación, entonces decimos que la descomposición **preserva la información**. Cuando una descomposición no preserva la información, siempre su reconstrucción genera tuplas de más (nunca de menos, pues siempre podemos realizar un producto cartesiano).

Diremos que la descomposición **preserva las dependencias funcionales** cuando toda dependencia funcional puede inferirse a partir de las dependencias funcionales definidas en los $R_i$.

### Proyección de Dependencias Funcionales

Al descomponer una relación $R$ con un conjunto de dependencias funcionales $F$ en $D = (R_1(Z_1), R_2(Z_2), \cdots, R_n(Z_n))$, es necesario saber qué dependencias funcionales se preservan.

Las dependencias funcionales que se preservan son las que surgen de la proyección de $F$ sobre los atributos $Z_i$ de cada relación $R_1$. Donde el conjunto de dependencias funcionales de $D$ será la unión de cada proyección.

$$
F_D = F_{Z_1} \cup F_{Z_2} \cup \cdots \cup F_{Z_n}
$$

Diremos que se preservan las dependencias funcionales cuando ambos conjuntos son equivalentes: $F^+ \equiv F_D^+$

## Primera Forma Normal

Un esquema de base de datos está en 1FN cuando los dominios de todos sus atributos solo permiten valores atómicos y monovaluados.

Actualmente, se considera que en el modelo relacional todos los atributos deben ser monovaludados y atómicos. Con este criterio, todo esquema relacional está ya en 1FN.

Si no es el caso, y el esquema tiene atributos multivaluados, entonces tendremos tres soluciones:

1. Colocar una tupla nueva por cada valor, repitiendo los otros atributos.
2. Suponer un máximo de valores, y colocar un atributo por cada uno.
3. Crear una nueva relación $1-n$, que relacione la tupla original con cada uno de los valores.

## Segunda Forma Normal

Un atributo primo de una relación es aquel que es parte de alguna clave candidata de la relación. Decimos que una relación está en 2FN cuando todos sus atributos no primos tienen dependencia funcional [[Dependencias Funcionales#Dependencia Parcial|completa]] de las claves candidatas.

Las claves candidatas son aquellos conjuntos de atributos que implican a todo el resto de atributos. De esta forma, la repetición de dos elementos con los mismos atributos en una clave candidata implicaría que el resto de atributos también serían iguales, por lo que no afectaría la relación.

Sea $R$ una relación que no está en 2FN. Luego, tendrá un conjunto de atributos $A$ no primos, tal que este tiene dependencia funcional completa de $B$, donde $B$ es un subconjunto de una clave candidata $C$. Esto nos obliga a incluir $A$ cada vez que está $B$, incluso si esto se repite en múltiples tuplas.

Para resolverlo, debemos generar una nueva relación $S$ con clave primaria $B$ y atributos $A \cup B$, y eliminar $A$ de la relación $R$.

Supongamos una tabla $\text{Docencia}(\text{Asignatura}, \text{Profesor}, \text{Departamento})$, donde la asignatura y el profesor son claves primarias, y el departamento depende de forma completa de la asignatura. Si yo quiero representar que un nuevo profesor da una asignatura, debo incluir el departamento (información redundante, ya que ya está en otras tuplas de la misma relación).

Para solucionarlo, debo generar una nueva tabla que permita abstraer esta información: $\text{Asignaturas}(Asignatura, Departamento)$. Luego, la tabla de docencia se vería como $\text{Docencia}(\text{Asignatura}, \text{Profesor})$. Para agregar un nuevo profesor a una materia, ahora no debo repetir el departamento.

## Tercera Forma Normal

Decimos que una relación está en 3FN cuando todos sus atributos no primos tienen [[Dependencias Funcionales#Dependencia Transitiva|dependencia funcional transitiva]] de las claves candidatas. Es decir, no existen atributos no primos que dependen de un conjunto de atributos que no son clave candidata.

Una definición equivalente es que para toda [[Dependencias Funcionales#Dependencia Trivial|dependencia funcional no trivial]] $X \to Y$, o bien $X$ es superclave, o bien $Y - X$ solo contiene atributos primos.

Sea $R$ una relación que no está en 3FN. Luego, tendrá un conjunto de atributos $A$ no primos, tal que $C \to A$ es transitiva a través de $B$. Esto nos obliga a incluir $A$ cada vez que está $B$, incluso si se repite en múltiples tuplas.

Para resolverlo, debemos generar una nueva relación $S$ con clave primaria $B$ y atributos $A \cup B$, y eliminar $A$ de la relación $R$.

### Algoritmo de 3FN

1. Definimos el conjunto de esquemas $D$ inicialmente vacío
2. Primero, debemos encontrar un cubrimiento minimal de $F_\min$ para $F$.
3. Por cada dependencia funcional con conjunto $X$ del lado izquierdo:
	1. Creamos un esquema de relación $R_X(X, A_1, A_2, \cdots, A_k)$ donde $X \to A_i$ son las únicas dependencias funcionales en $F_\min$ con el conjunto $X$ del lado izquierdo.
	2. Ampliamos el conjunto de esquemas $D = D \cup R_X$

#todo

## Forma Normal Boyce-Codd

Decimos que una relación está en FNBC si no existen relaciones transitivas. Sin importar si incluye atributos primos o no. Esta forma nos permite resolver situaciones donde tendremos múltiples claves candidatas que se solapan.

Dicho de otra forma, para todas las dependencias funcionales $X \to Y$, entonces $Y$ es clave (o superclave).

Sea $R$ una relación que no está en FNBC. Luego, tendrá un conjunto de atributos $A$, tal que $C \to A$ es transitiva a través de $B$. Esto nos obliga a incluir $A$ cada vez que está $B$, incluso si se repite en múltiples tuplas.

Para resolverlo, debemos generar una nueva relación $S$ con clave primaria $B$ y atributos $A \cup B$, y eliminar $A$ de la relación $R$.

Este tipo de descomposiciones no nos asegura conservar la dependencia funcional.

### Algoritmo de FNBC

#todo

## Cuarta Forma Normal

Una relación $R$ está en 4FN cuando para toda [[Dependencias Funcionales#Dependencia Multivaluada|dependencia multivaluada]] no trivial $X \to\to Y$, $X$ es clave (o superclave).

Para resolverlo, debemos generar una nueva relación $S$ con clave primaria $X$ tal que esté relacionada con cada elemento distinto de $Y$ con el cual se relaciona en alguna tupla.

Es común que las dependencias multivaluadas provengan de la existencia de atributos multivaluados en el modelo conceptual, o de interrelaciones $N-N$ no capturadas

Las relaciones en 4FN están automáticamente en FMBC, pues todas las dependencias multivaluadas son, a su vez, dependencias funcionales. Esto se debe a que las dependencias multivaluadas son un caso genérico de las dependencias funcionales.

$$
X \to Y \implies X \to\to Y
$$

## Quinta Forma Normal

Una relación $R(A)$ está en 5FN si y solo si para toda [[Dependencias Funcionales#Dependencia de Junta|dependencia de junta]] $(X_1, X_2, \cdots, X_n)$ no trivial (tal que ningún $X_i = A$) todos los $X_i$ son superclaves.

Observemos que una dependencia de junta implica una dependencia multivaluada, que implica una dependencia funcional.
