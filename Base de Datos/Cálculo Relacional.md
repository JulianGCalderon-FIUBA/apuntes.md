Es un [[Lenguajes#Data-Manipulation Language|lenguaje de manipulación de datos]] declarativo, de más alto nivel que el álgebra relacional. Al no ser procedural, no especifica el orden de las operaciones. El [[Lenguaje SQL]] está inspirado en el cálculo relacional.

El cálculo relacional está basado en la **lógica de predicados**.

Existen dos variaciones: **cálculo relacional de tuplas**, y cálculo relacional de dominios. Solo vamos a estudiar la primera.

## Lógica de Predicados

La lógica de [[Modelo Relacional#Predicados|predicados]] de primer orden se basa en tres componentes:

- **Predicados:** Son funciones de una o más variables cuyo resultado es un valor de verdad (verdadero o falso).
- **Operaciones** entre predicados: $\land$, $\lor$, $\neg$, $\to$.
- **Cuantificadores** de variables: Existen dos cuantificadores:
	- Cuantificador universal: $(\forall m)q(m)$. Es verdadero si para cualquier valor de $m$, el predicado $q(m)$ es verdadero.
	- Cuantificador existencial: $(\exists m)q(m)$. Es verdadero si existe al menos un valor de $m$ para el cual el predicado $q(m)$ es verdadero.

Para restringir el dominio de la variable en un cuantificador universal, tenemos que usar la negación. En caso contrario, el resultado siempre será falso.

$$
(\forall m)(m \notin \text{Dominio} \lor \Phi(m))
$$

La expresión será verdadera para todas las variables del dominio que cumplen con el predicado $\Phi$.

De forma equivalente, podemos usar el cuantificador existencial negado

$$
(\nexists m)(m \in \text{Dominio} \land \neg\Phi(m))
$$

### Conjuntos Definidos por Predicado

La notación de construcción de conjuntos puede ser utilizada para definir un conjunto de valores a partir de un predicado.

$$
\{x|\Phi(x)\}
$$

La formula $\Phi(x)$ es denominada el **predicado**, y es una función cuyo resultado es un valor de verdad.

El conjunto estará definido por todos los $x$ *tal que* el predicado tome un valor verdadero.

Las variables definidas del lado izquierdo de la expresión se conocen como variables **libres**.

Las variables que no pertenecen al lado izquierdo y son utilizadas dentro del predicado se denominan variables **ligadas**. Es necesario que estén acompañadas de un cuantificador.

## Cálculo Relacional de Tuplas

En el cálculo relacional de tuplas, las variables representan **tuplas**.

Un **predicado simple** es una función de una tupla o de atributos de tuplas, cuyo resultado es un valor de verdad. Se admiten como predicados simples:

- $R(t)$, donde $R$ es una relación
- $t_1.A_i \odot t_2.A_j$
- $t.A_i \odot c$, con $c \in \text{dom}(A_i)$

En donde $\odot$ es un operador de **comparación**:

- $=$, $\neq$
- $>$, $\geq$, $<$, $\leq$ (solo para atributos cuyos dominios están ordenados)

Las **operaciones** entre predicados admitidas son: $\land$, $\lor$, $\neg$.

Una **expresión** del cálculo relacional de tuplas tiene la forma:

$$
\{t_1.A_{11}, t_1.A_{12}, \cdots, t_1.A_{1,{k_1}}, \cdots, t_n A_{n,{k_n}}|p(t_1, t_2, \cdots, t_n, t_{n+1}, \cdots, t_{n+m})\}
$$

Donde $p$ es un predicado válido, $t_1, t_2, \cdots, t_n$ son variables libres, y $t_{n+1}, \cdots, t_{n+m}$ son variables ligadas. Notemos que el predicado únicamente es función de las variables libres, pero son parte de la expresión.

> [!example] Ejemplo
> Liste el jugador más anciano del mundial
> 
> $$
> \{p.\text{name}|\text{Players}(p) \land (\nexists\theta)(\text{Players}(\theta) \land \theta.\text{birth\_date} < p.\text{birth\_date})\}
> $$
> 
> También podemos usar el cuantificador universal
> 
> $$
> \{p.\text{name}|\text{Players}(p) \land (\forall\theta)(\neg\text{Players}(\theta) \lor \theta.\text{birth\_date} \geq p.\text{birth\_date})\}
> $$

Una expresión **segura** es aquella que producirá una cantidad finita de resultados. No todas las expresiones válidas son seguras.

> [!example] Expresión no segura
> Hay una cantidad infinita de tuplas que no pertenecen a una relación.
> 
> $$
> \{p.\text{name}|\neg\text{Players(p)}\}
> $$

## Completitud Relacional

E. Codd demostró la equivalencia entre el álgebra relacional básica y el cálculo relacional. Esta equivalencia implica que ambos lenguajes tienen el mismo **poder expresivo**.

A su vez, se dice que un lenguaje es **relacionalmente completo** cuando tiene el mismo poder expresivo que el cálculo relacional.
