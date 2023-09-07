Es un [[Lenguajes|lenguaje]] declarativo, de más alto nivel que el álgebra relacional. Al no ser procedural, no especifica el orden de las operaciones.

Es un lenguaje basado en la lógica de [[Predicados|predicados]]

Presenta dos variantes:

- El cálculo relacional de tuplas
- El cálculo relacional de dominios

El lenguaje SQL está inspirado en el cálculo relacional

## Cálculo Relacional de Tuplas

En el cálculo relacional de tuplas, las variables representan tuplas.

Un predicado simple es una función de una tupla o de atributos de tuplas, cuyo resultado es un valor de verdad. Se admiten como predicados simples:

- $R(t)$, donde $R$ es una relación
- $t_1.A_i \odot t_2.A_j$
- $t.A_i \odot c$, con $c \in \text{dom}(A_i)$

Las operaciones entre predicados admitidas son: $\land$, $\lor$, $\neg$.

Una expresión del cálculo relacional de tuplas tiene la forma:

$$
\{t_1.A_{11}, t_1.A_{12}, \cdots, t_1.A_{1,{k_1}}, \cdots, t_n A_{n,{k_n}}|p(t_1, t_2, \cdots, t_n, t_{n+1}, \cdots, t_{n+m})\}
$$

Donde $p$ es un predicado válido, $t_1, t_2, \cdots, t_n$ son variables libres, y $t_{n+1}, \cdots, t_{n+m}$ son variables ligadas.

Las variables ligadas deben ser cuantificadas, y no pueden aparecer del lado izquierdo.

> [!example] Ejemplo
> Liste el jugador mas anciano del mundial
> 
> $$
> \{p.\text{name}|\text{Players}(p) \land (\nexists\theta)(\text{Players}(\theta) \land \theta.\text{birth\_date} > p.\text{birth\_date})\}
> $$

Una expresión **segura** es aquella que producirá una cantidad finita de resultados. No todas las expresiones válidas son seguras.

> [!example] Expresión no segura
> Hay una cantidad infinita de tuplas que no pertenecen a una relación.
> 
> $$
> \{p.\text{name}|\neg\text{Players(p)}\}
> $$

## Cálculo Relacional de Dominios

En el cálculo relacional de dominios, las variables representan dominios.

Un predicado simple es una función de un conjunto de dominios, cuyo resultado es un valor de verdad. Se admiten como predicados simples:

- $R(x_1, x_2, \cdots, x_n)$, donde $R(A_1, A_2, \cdots, A_n)$ es una relación
- $x_i \odot x_j$
- $x_i \odot c$, con $c \in \text{dom}(A-i)$

Las operaciones entre predicados admitidas son: $\land$, $\lor$, $\neg$.

Una expresión del cálculo relacional de tuplas tiene la forma:

$$
\{x_1, x_2, \cdots, x_n|p(x_1, x_2, \cdots, x_n, x_{n+1}, \cdots, x_{n+m})\}
$$

Donde $p$ es un predicado válido, $x_1, x_2, \cdots, x_n$ son variables libres, y $x_{n+1}, \cdots, x_{n+m}$ son variables ligadas.

> [!example] Ejemplo
> Liste los nombres de los jugadores nacidos antes de 1980
> 
> $$
> \{\text{name}|(\exists \text{birth\_date})(\text{Player}(\text{name}, \text{birth\_date})\land \text{birth\_date} \leq 1980)\}
> $$

## Completitud Relacional

E. Codd demostró la equivalencia entre el álgebra relacional básica y el cálculo relacional. Esta equivalencia implica que ambos lenguajes tienen el mismo **poder expresivo**.

A su vez, se dice que un lenguaje es **relacionalmente completo** cuando tiene el mismo poder expresivo que el cálculo relacional.
