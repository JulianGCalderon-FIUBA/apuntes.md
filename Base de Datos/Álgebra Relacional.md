Tendremos dos componentes principales: el **álgebra relacional**, y el **cálculo relacional**. El cálculo nos dirá *qué* obtener, y el álgebra nos dirá *cómo* lo obtendremos.

El álgebra relacional es un [[Lenguajes|lenguaje]] procedural, mientras que el cálculo relacional será un lenguaje declarativo.

## Definiciones

Este lenguaje especifica los procedimientos de consultas de datos a partir de un conjunto de operaciones. Una **operación** es una función cuyos operandos son una o más relaciones, y cuyo resultado es también una relación.

Las operaciones del álgebra relacional pueden combinarse entre ellos para formar una **expresión**.

La **aridad** es la cantidad de operandos que toma una operación.

## Operaciones Básicas

### Selección

El operador de selección $\sigma$ es un operador unario.

$$
\sigma_{\text{cond}}: R \to S
$$

Se queda con las tuplas que cumplan una determinada condición. Matemáticamente, se puede definir como:

$$ 
\sigma_\text{cond} (R) = \{t\in R: \text{cond}(T)\}
$$

Como condición, utilizaremos condiciones de la forma: $A_i \odot A_j$ o $A_i \odot c$. Donde $\odot$ es un operador de comparación: $=, \neq, <, >, \leq, \geq$.

Estas condiciones se pueden combinar con operadores lógicos *and* $\land$ y *or* $\lor$

### Proyección

El operador de proyección $\pi$ es también un operador unario.

$$
\pi_L : R \to S
$$

Dada una relación $R$ y una lista de atributos $L$, devuelve una relación cuyas tuplas representan los posibles valores de los atributos de $L$ en $R$.

El orden de los atributos en las tuplas resultantes es el orden de expresado en $L$.

Este operador elimina las tuplas duplicadas, ya que su resultado debe ser relación válida.

> [!example] SQL
> Se puede combinar la selección con la proyección con el comando `SELECT (Row1, Row2, Row3) FROM Table WHERE Condition`

### Asignación

Nos permite asignar el resultado de una operación a una *variable*. Podemos generar operaciones complejas al concatenar múltiples operaciones.

$$
Var \leftarrow R
$$

### Redenominación

Con la redenominación, le cambiamos el nombre a una relación, lo que nos permite diferenciarlas cuando se utilizan dos veces en la misma expresión. De la misma forma, se puede redenominar un atributo.

$$
\rho_S : R \to R
$$

Cambia el nombre de la relación $R$ por $S$.

## Operaciones de Conjuntos

### Unión

Dadas dos relaciones, obtendremos una nueva relación con las tuplas de ambas

$$
\cup: R, S \to T
$$

Ambas relaciones deben tener el mismo grado, y compatibilidad de tipo. La compatibilidad de tipo especifica que los atributos en la misma posición (en orden) deben tener el mismo tipo de dato.

El listado de atributos será el de la primera relación.

### Intersección

Dadas dos relaciones, conserva las tuplas que se encuentran en ambas

$$
\cap: R, S \to T
$$

Deben cumplirse las mismas restricciones que para la unión.

El listado de atributos será el de la primera relación.

### Diferencia

Dadas dos relaciones $R, S$, conserva las tuplas que se encuentran presentes en $R$ pero no en $S$.

$$
-: R, S \to T
$$

Deben cumplirse las mismas restricciones que para la unión.

El listado de atributos será el de la primera relación.

### Producto Cartesiano

Dadas dos relaciones $R(R_1, R_2, \cdots, R_n), S(S_1, S_2, \cdots, S_n)$, el producto cartesiano produce una nueva relación $T(R_1, R_2, \cdots, R_n, S_1, S_2, \cdots, S_n)$. Combina cada tupla de $R$ con cada tupla de $S$.

$$
\times: R, S \to T
$$

A diferencia de la unión, la relación crece en cantidad de columnas. No requiere compatibilidad de tipos ni de grado.

Si dos columnas tienen el mismo nombre $x$, entonces se diferencian como $R.x, S.x$. Si la tabla tiene el mismo nombre, se diferencian como $R1.x, R2.x$.

En general, debe estar acompañado de una selección para reducir la cantidad de filas.

### Junta

La junta es una operación compuesta, que consiste de un producto cartesiano, seguido de una selección.

$$
\bowtie_{\text{cond}}: R,S\to T
$$

No se admite cualquier condición, solo las del tipo $A_i \odot A_j$.

> [!example] SQL
> El gestor automáticamente realiza un producto cartesiano cuando se seleccionan dos tablas relacionadas en un `SELECT`, agregando en `WHERE` la condición para la junta. Otra forma es utilizar directamente `INNER JOIN`.

#### Junta Natural

Existen tres juntas principales. La junta más general se conoce como *theta join*.

Cuando solo utilizamos comparaciones de igualdad en sus condiciones atómicas, se denomina junta por igual *(equijoin)*

En estas juntas, el resultado dispondrá de pares de atributos distintos que poseerán información redundante. Para librarse de uno de ellos, se define la **junta natural**. Esta junta se simboliza con $R * S$.

Para que sea posible, las relaciones deben estar preparadas (con el mismo nombre de atributo de ambos lados). En la junta natural no se especifican las condiciones, por lo que se utilizaran automáticamente los atributos con igual nombre.

Los atributos comparados en una junta se denominan **atributos de junta**.

### División

Es una operación inversa al producto cartesiano. Partimos de una relación $R$ y una relación $S$ cuyos atributos están incluidos en $R$. Si llamamos $A$ a los atributos de $R$ y $B$ a los atributos de $S$, entonces $B \subset A$, y definimos $Y = A - B$.

Luego, se define la división $R \div S$ como la relación $T(Y)$, que contiene todas las tuplas $t$ que cumplan que:

1. La tupla $t$ pertenece a $\pi_Y(R)$
2. Para cada tupla $t_S \in S$, existe una tupla $t_R \in R$ tal que $t_R[Y] = t$ y $t_R[B] = t_s$.

La relación $T$ es la de mayor cardinalidad posible contenida en $\pi_Y(R)$ y que cumple que $T * S \subset R$
