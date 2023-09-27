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

## Formas Normales

Las formas normales son una serie de estructuras con las que un esquema de base de datos puede cumplir o no.

Las formas normales clásicas son:

- Primera forma normal: **1FN**
- Segunda forma normal: **2FN**
- Tercera forma normal: **3FN**
- Forma normal Boyce-Codd: **FNBC**
- Cuarta forma normal: **4FN**
- Quinta forma normal: **5FN**

Cada forma normal es más fuerte que las anteriores. El cumplimiento de cualquier forma implica el cumplimiento de las anteriores.
