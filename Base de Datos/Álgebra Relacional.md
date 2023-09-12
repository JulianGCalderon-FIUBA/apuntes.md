Tendremos dos componentes principales: el **álgebra relacional**, y el [[Cálculo Relacional]]. El cálculo nos dirá *qué* obtener, y el álgebra nos dirá *cómo* lo obtendremos.

El álgebra relacional es un [[Lenguajes#Data-Manipulation Language|lenguaje de manipulación de datos]] procedural, mientras que el cálculo relacional será un lenguaje declarativo.

## Definiciones

Este lenguaje especifica los procedimientos de consultas de datos a partir de un conjunto de operaciones.

Una **operación** es una función cuyos operandos son una o más relaciones, y cuyo resultado es también una relación.

$$
O: R_1 \times R_2 \times \cdots \times R_n \to S
$$

Las operaciones del álgebra relacional pueden combinarse entre ellos para formar una **expresión**.

La **aridad** es la cantidad de operandos que toma una operación.

## Operaciones Unarias

### Selección

El operador de **selección** $\sigma$ es un operador unario. Dada una relación $R$ y una condición que se aplica a cada tupla de $R$, selecciona aquellas tuplas de $R$ para las cuales la condición es verdadera.

$$
\sigma_{\text{cond}}: R \to S
$$

Como **condición**, utilizaremos condiciones de la forma:

- $A_i \odot A_j$
- $A_i \odot c$

Donde $\odot$ es un operador de comparación: $=$, $\neq$, $<$, $>$, $\leq$, $\geq$.

Estas condiciones se pueden combinar con operadores lógicos de conjunción $\land$, disyunción $\lor$, y negación $\neg$.

### Proyección

El operador de **proyección** $\pi$ es también un operador unario. Dada una relación $R$ y una lista de atributos $L$, devuelve una relación cuyas tuplas representan los posibles valores de los atributos de $L$ en $R$.

$$
\pi_L : R \to S
$$

El **orden** de los atributos dependerá es el mismo orden que figura en $L$.

Este operador elimina las tuplas **duplicadas**, ya que su resultado debe ser relación válida.

> [!example] SQL
> Se puede combinar la selección con la proyección con el comando `SELECT Rows FROM Table WHERE Condition`

### Asignación

Nos permite asignar el resultado de una operación a una *variable*. Podemos generar operaciones complejas al concatenar múltiples operaciones.

$$
Var \leftarrow R
$$

También se denota con el símbolo de igualdad $=$

### Redenominación

El operador de **redenominación** $\rho$ nos permite modificar los nombres de los atributos de una relación y/o de la relación misma. Nos permite preparar el resultado para una operación posterior.

$$
\rho_S : R \to S
$$

Dada una relación $R(A_1, A_2, \cdots, A_n)$, un nuevo nombre de relación $S$ y una lista de atributos $(B_1, B_2, \cdots, B_n)$. Entonces $\rho_S(B_1, B_2, \cdots, B_n) (R)$ produce una relación de nombre $S$ y atributos $(B_1, B_2, \cdots, B_n)$ cuyas tuplas coinciden con las tuplas de $R$.

Si se omiten los atributos, solo se cambia el nombre de la relación. Para cambiar el nombre de únicamente un atributo, podemos utilizar $\rho_{B_1 \leftarrow A_1}(R)$.

## Operaciones Binarias

### Unión

Dadas dos relaciones $R, S$, entonces la **unión** $R \cup S$ es una relación que contiene a todas las tuplas de $R$ y de $S$.

$$
\cup: R, S \to T
$$

Es necesario que $R$ y $S$ tengan el mismo **grado**.

Es necesario que haya **compatibilidad de tipo**. Deben coincidir en sus atributos en lo que respecta al dominio. Es decir, siendo $A$ los atributos de $R$ y $B$ los atributos de $S$, entonces $\text{dom}(A_i) = \text{Dom}(B_i)$.

Por convención, en la relación resultada el listado de atributos coincide con el de $R$

### Intersección

Dadas dos relaciones $R$ y $S$, la **intersección** $R\cap S$ conserva las tuplas que se encuentran en ambas relaciones.

$$
\cap: R, S \to T
$$

Es necesario que tengan el mismo grado y haya compatibilidad de tipo. Por convención, en la relación resultada el listado de atributos coincide con el de $R$.

### Diferencia

Dadas dos relaciones $R, S$, conserva las tuplas que se encuentran presentes en $R$ pero no en $S$.

$$
-: R, S \to T
$$

Es necesario que tengan el mismo grado y haya compatibilidad de tipo. Por convención, en la relación resultada el listado de atributos coincide con el de $R$.

### Producto Cartesiano

Dadas dos relaciones $R(A_1, A_2, \cdots, A_n), S(B_1, B_2, \cdots, B_n)$, el producto cartesiano produce una nueva relación $T(A_1, A_2, \cdots, A_n, B_1, B_2, \cdots, B_n)$, con una tupla por cada combinación posible de una tupla de $R$ con una tupla de $S$.

$$
\times: R, S \to T
$$

Si dos columnas tienen el mismo nombre $x$, entonces se diferencian en la tabla final como $R.x, S.x$. En el caso de estar calculando $R \times R$, llamaremos a sus atributos $R_1.A_i$ y $R_2.A_i$

En general, debe estar acompañado de una selección para reducir la cantidad de filas.

Esta operación no requiere que tengan el mismo grado, ni que haya compatibilidad de tipos.

> [!example] SQL
> Automáticamente realiza un producto cartesiano cuando se seleccionan dos tablas relacionadas en un `SELECT`.

### Junta

Dadas dos relaciones $R, S$ y una condición, la junta $R \bowtie_\text{cond} S$ selecciona del producto cartesiano $R \times S$ las tuplas que cumplen la condición.

$$
\bowtie_{\text{cond}}: R,S\to T
$$

No se admite cualquier condición, solo aquellas que incluyen un atributo de cada relación, es decir, de la forma $A_i \odot A_j$. Además, únicamente se puede utilizar el operador lógico de conjunción $\land$.

> [!example] SQL
> Para realizar una junta, podemos utilizar el comando `INNER JOIN` dentro de un `SELECT`.

La junta más general se conoce como **junta theta** *(theta join)*. Cuando solo utilizamos comparaciones de igualdad en sus condiciones atómicas, se denomina **junta por igual** *(equijoin)*. En estas juntas, el resultado dispondrá de pares de atributos distintos que poseerán información redundante. Para librarse de uno de ellos, se define la **junta natural**.

### Junta Natural

Dadas dos relaciones $R, S$ con un atributo en común tal que $A_i = B_i$, entonces la **junta natural** $R * S$ devolverá una junta entre ambos, conservando únicamente las tuplas $t$ tal que $t[A_i] = t[B_i]$, y descartando el atributo $B_i$.

$$
* : R, S \to T
$$

En la junta natural no se especifican las condiciones, por lo que se utilizaran automáticamente los atributos con igual nombre. Estos atributos se denominan **atributos de junta**.

### División

Es una operación inversa al producto cartesiano. Dadas dos relaciones $R, S$, la división $R \div S$ nos devuelve...

$$
\div : R, S \to T
$$

Partimos de una relación $R(A_1, A_2, \cdots, A_n)$ y una relación $S(B_1, B_2, \cdots, B_n)$ tal que $B \subset A$. Definimos $Y = A - B$.

Luego, se define la división $R \div S$ como la relación $T(Y)$, que contiene todas las tuplas $t \in \pi_Y(R)$ que cumplan que, para cada tupla $t_S \in S$, existe una tupla $t_R \in R$ tal que $t_R[Y] = t$ y $t_R[B] = t_s$.

En otras palabras, $R \div S$ nos devuelve una relación con todas las tuplas de $\pi_Y(R)$ tal que su combinación con cualquier tupla de $S$ pertenezca a $R$.

La relación $T$ es la de mayor cardinalidad posible contenida en $\pi_Y(R)$ y que cumple que $T \times S \subset R$.

### Junta Externa

La junta externa evita perder tuplas que no pueden ser combinadas con ningún elemento de la otra tabla. Existen tres tipos de tuplas externas:

- Junta externa **izquierda**: $⟕$
- Junta externa **derecha**: $⟖$
- Junta externa **completa**: $⟗$

Dadas dos relaciones $R, S$ y una condición, la junta externa entre $R \ [⟕,⟖,⟗]_\text{cond}\ S$ selecciona del producto cartesiano $R \times S$ las tupas que cumplen la condición, y añade:

- En la junta externa **izquierda**, todas las tuplas de $R$ que no aparecen en la proyección de los atributos de $R$ en el resultado final.
- En la junta externa **derecha**, todas las tuplas de $R$ que no aparecen en la proyección de los atributos de $R$ en el resultado final.
- En la junta externa **completa**, todas las tuplas de $R$ o de $S$ que no aparecen en la proyección de los atributos de $R$ o de $S$ respectivamente en el resultado final.

## Conjuntos Completos de Operadores

Hemos definido una serie de operaciones básicas del álgebra relacional, pero existen subconjuntos de ellos que tienen la misma capacidad de expresión que todo el conjunto. A dichos subconjuntos se los denomina **conjuntos completos de operadores**

Los siguientes operadores forman un conjunto completo:

$$
\sigma, \pi, \rho, \cup, -, \times
$$

Para demostrarlo, debemos mostrar que el resto de operadores se puede construir a partir de estos seis. Por ejemplo, la intersección:

$$
A \cap B = (B - A) \cup (A-B)
$$
