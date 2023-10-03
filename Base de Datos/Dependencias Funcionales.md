Dada una relación $R(\overline A)$, una dependencia funcional $X \to Y$, con $X, Y \subset \overline A$ es una restricción sobre las posibles tuplas de $R$ que implica que dos tuplas con igual valor del conjunto de atributos $X$ deben también tener igual valor del conjunto de atributos $Y$.

$$
\forall s,t \in R: s[X] = t[X] \implies s[Y] = t[Y]
$$

## Axiomas

Hay tres axiomas que sirven para inferir dependencias funcionales:

- Axioma de reflexividad: $Y \subset X \implies X \to Y$
- Axioma de aumento: $\forall W: X \to Y \implies XW \to YW$
- Axioma de transitividad: $X \to Y \land Y \to Z \implies X \to Z$

La notación $F \vDash X \to Y$ implica que $X \to Y$ puede ser deducido del conjunto de dependencias funcionales $F$.

Las siguientes tres reglas se deducen de los axiomas

- Regla de unión: $X \to Y \land X \to Z \implies X \to YZ$
- Regla de pseudo transitividad: $\forall W: X\to Y \land YW \to Z \implies XW \to Z$.
- Regla de descomposición: $X \to YZ \implies X \to Y \land X \to Z$

## Clausura

Sea $F$ un conjunto de dependencias funcionales, entonces $F^+$ se conoce como clausura de $F$ y contiene el conjunto de todas las dependencias funcionales que pueden inferirse de $F$. Esto es:

$$
F^+ = \{X \to Y|F \vDash X \to Y\}
$$

La clausura de un atributo son todos los atributos que puedo inferir de dicho atributo, a partir de un conjunto de dependencias funcinoales $F$.

$$
X_F^+ = \{A_i|F \vDash X \to A_i\}
$$

Las clausuras de todos los atributos de una relación son una forma ordenada de construir su $F^+$.

A partir de esto, podemos definir una clave candidata como cualquier conjunto de atributos tal que su clausura contiene todos los atributos de la relación.

## Cubrimiento y Equivalencia

Dados dos conjuntos de dependencias funcionales $F, G$, decimos que $F$ **cubre** a $G$ si $G^+ \subset F^+$. Esto implica que cualquier dependencia funcional de $G$ puede ser inferida por $F$.

$$
	
$$

Dados dos conjuntos de dependencias funcionales $F, G$, decimos que son **equivalentes** si $F^+ = G^+$. Lo simbolizaremos con $F \equiv G$. Esto implica que tanto $F$ cubre a $G$, y $G$ cubre a $F$.

## Cubrimiento Minimal

Dado un conjunto de dependencias funcionales $F$, trataremos de encontrar un conjunto equivalente $G$ que cumpla con ciertas reglas:

1. No haya atributos innecesarios del lado izquierdo de alguna dependencia, tal que al sacarlos el conjunto de dependencias sea equivalente.

	$$
	\forall (X \to Y) \in G: \nexists (Z \to Y) \in G, Z \subset X, Z \neq X
	$$

2. No haya dependencias redundantes, tal que al sacarlas el conjunto de dependencias sea equivalente.

	$$
	\nexists(X \to Y) \in G: G - \{X \to Y\} \equiv G
	$$

Este conjunto $G$ se llamará cubrimiento minimal de $F$.

### Algoritmo de Cubrimiento Minimal

Para hallar un cubrimiento minimal, tomaremos tres pasos:

1. Pasar las dependencias funcionales a forma canónica. Esto quiere decir que del lado derecho solo puede haber un atributo.
2. Eliminar los atributos innecesarios del lado izquierdo de cada dependencia funcional.
3. Eliminar las dependencias funcionales redundantes.

## Trivialidad

Cuando $Y \subset X$, entonces decimos que $X \to Y$ es una dependencia **trivial**. Las dependencias funcionales se definen a partir de la semántica de los datos. No es posible inferirlas viendo los datos.

## Dependencia Parcial

Una dependencia formal $X \to Y$ es **parcial** cuando existe un subconjunto propio $A \subset X, A \neq X$, para el cual $A \to Y$.

Una dependencia funcional es **completa** si y solo si no es parcial.

## Dependencia Transitiva

Se puede aplicar la **transitividad**, de modo que dada una relación $R(\overline A)$, entonces si $A, B, C \in \overline A$, con las dependencias $A \to B$, y $B \to C$, entonces también se cumple que $A \to C$.

Una dependencia formal $X \to Y$ es **transitiva** si existe un $Z$ tal que $X \to Z$ y $Z \to Y$. Siendo $Z \to Y$ no trivial, $X \to Y$ no trivial, y $Z \cancel\to X$. Todas las dependencias funcionales parciales no triviales son transitivas.

## Dependencia Multivaluada

Dada una relación $R(A)$, la **dependencia multivaluada** $X \to\to Y$ es una restricción sobre las posibles tuplas de $R$ que implica que para todo par de tuplas $t_1, t_2$ tales que $t_1[X] = t_2[X]$, deberían existir otras dos tuplas $t_3, t_4$ que resultan de intercambiar los valores de $Y$ entre $t1$ y $t2$. Es decir:

- $t_1[X] = t_2[X] = t_3[X] = t_4[X]$
- $t_1[Y] = t_4[Y]$ y $t_2[Y] = t_3[Y]$
- $t_1[A - X \cup Y] = t_3[A - X \cup Y]$
- $t_2[A - X \cup Y] = t_4[A - X \cup Y]$

Por una cuestión de simetría, si $X \to\to Y$, entonces también vale que $X \to\to A - X \cup Y$.

Las dependencias multivaluadas en las que $X \cup Y = A$, o $Y \subset X$ son triviales.

## Dependencia de Junta

Siempre que en una relación $R$ haya una dependencia multivaluada $X \to\to Y$, entonces $R$ puede ser descompuesta sin perdida en $R'(X, Y)$, eliminando $Y$ de $R$.

Sin embargo, existen relaciones que pueden ser descompuestas en más de dos relaciones, también sin perdida. Cuando esto ocurre, decimos que hay una dependencia de junta.

Dada una relación $R(A)$, y una serie de subconjuntos de atributos $X_1, X_2, \cdots, X_n$, decimos que $(X_1, X_2, \cdots, X_n)$ es una dependencia de junta cuando la descomposición de $R$ en $\pi_{X_1}(R) * \pi_{X_2}(R) * \cdots * \pi_{X_n}(R)$ es sin perdida de información.
