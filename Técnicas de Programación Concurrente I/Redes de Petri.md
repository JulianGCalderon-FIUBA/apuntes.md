Una red de Petri es un grafo dirigido bipartito, que cumple con:

$$
PN = (T,P,A)
$$

Donde tenemos:

- Un conjunto de nodos $T = t_1, t_2,..., t_n$ llamados transiciones
- Un conjunto de nodos $P = p_1, p_2,..., p_n$ llamados lugares
- Un conjunto de arcos $A \subseteq (T\times P)\cup(P\times T)$

Mostramos un ejemplo sencillo

![[Redes de Petri 1695766606.png|500]]

Donde $p_i$ son los estados de un sistema, y $t_i$ son los eventos que ocasionan los cambios de estado.

## Función de Marca

Se define la función de marca $M$ como la cantidad de *tokens* que hay en cada uno de los lugares de la red de Petri.

$$
M : P \to N_0
$$

Cuando hay un único *token* que está en el lugar $p_1$, entonces $M(p_1) = 1$, y $M(p_2) = 0$, por lo tanto, $M_0 = (1,0)$ (para el caso del ejemplo anterior)

## Funciones de Entrada y Salida

Sea $t$ una transición perteneciente a la red de Petri.

- Se define la función $I(t) = \{p \in P | (p,t) \in A\}$ como la entrada de la transición $t$. El conjunto de lugares que pueden derivar en esa transición. Es necesario que haya un *token* en todas las entradas de una transición para poder activarla.
- Se define la función $O(t) = \{p \in P | (p,t) \in A\}$ como la salida de la transición $t$. El conjunto de lugares al que se deriva un *token* a través de la transición $t$. Se genera un *token* para cada salida de una transición.

## Grafo de Alcance

Un grafo de alcance determina la función de marca para cada estado de la ejecución.

A partir de una red de Petri cualquiera:

![[Redes de Petri 1695767416.png|450]]

Podemos diagramar su grafo de alcance:

![[Redes de Petri 1695767438.png|450]]

Si encontramos que un estado del grafo de alcance no tiene ninguna arista saliente, diremos que estamos en un *deadlock*.

## Utilidades

Las redes de Petri nos permiten realizar un análisis estático del sistema, para detectar la existencia de *deadlocks*.
