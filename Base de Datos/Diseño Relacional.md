El diseño relacional consiste en construir un esquema de base de datos del [[Modelo Relacional]] que pueda correctamente representar la realidad. Algunos criterios comunes para un buen diseño relacional son:

- Preservación de información
- Redundancia mínima

Cuando se parte de un correcto diseño conceptual y se hace un correcto pasaje al modelo lógico, se obtiene un esquema sin redundancia y se preserva toda la información del mundo real que se quería modelar.

Para verificar y corregir un esquema relacional, la teoría de diseño relacional formaliza estos requisitos a través de las **formas normales**.

## Dependencias Funcionales

Dada una relación $R(\overline A)$, una dependencia funcional $X \to Y$, con $X, Y \subset \overline A$ es una restricción sobre las posibles tuplas de $R$ que implica que dos tuplas con igual valor del conjunto de atributos $X$ deben también tener igual valor del conjunto de atributos $Y$.

$$
\forall s,t \in R: s[X] = t[X] \implies s[Y] = t[Y]
$$

Cuando $Y \subset X$, entonces decimos que $X \to Y$ es una dependencia **trivial**. Las dependencias funcionales se definen a partir de la semántica de los datos. No es posible inferirlas viendo los datos.

### Dependencia Transitiva

Se puede aplicar la **transitividad**, de modo que dada una relación $R(\overline A)$, entonces si $A, B, C \in \overline A$, con las dependencias $A \to B$, y $B \to C$, entonces también se cumple que $A \to C$.

### Dependencia Multivaluada

Dada una relación $R(A)$, la **dependencia multivaluada** $X \to\to Y$ es una restricción sobre las posibles tuplas de $R$ que implica que para todo par de tuplas $t_1, t_2$ tales que $t_1[X] = t_2[X]$, deberían existir otras dos tuplas $t_3, t_4$ que resultan de intercambiar los valores de $Y$ entre $t1$ y $t2$.

## Descomposición

Partimos del concepto de la relación universal $R(\overline A)$. Esta engloba todos los atributos del mundo real que nuestro modelo representa.

Dada una relación universal $R$ y un conjunto de dependencias funcionales $F$ asociado, decimos que el conjunto de relaciones $\{ R_1(\overline B_1), \cdots, R_n(\overline B_n)\}$ es una descomposición de $R$ cuando todos los atributos de la relación $R$ se conservan.

$$
\bigcup_{i=1}^n A_i = \bigcup_{i=1}^m\bigcup_{j=1}^{n_i} B_{ij}
$$

Si una descomposición cumple que para toda instancia posible de $R$, la junta de las proyecciones sobre $R_i$ permite recuperar la misma instancia de relación, entonces decimos que la descomposición **preserva la información**.

Diremos que la descomposición **preserva las dependencias funcionales** cuando toda dependencia funcional puede inferirse a partir de las dependencias funcionales definidas en los $R_i$.
