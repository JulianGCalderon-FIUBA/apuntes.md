Una red general de Petri es un grafo dirigido bipartito, que cumple con:

$$
PN = (T, P, A, W, M_0)
$$

Donde tenemos:

- Un conjunto de nodos $T = t_1, t_2,..., t_n$ llamados transiciones
- Un conjunto de nodos $P = p_1, p_2,..., p_n$ llamados lugares
- Un conjunto de arcos $A \subseteq (T\times P)\cup(P\times T)$
- Una función de peso $W: A \to \Bbb{N}$
- Una función de mara inicial $M_0: P \to N_0$

## Transiciones

El peso de un arco nos indica la cantidad de *tokens* que consume (entrada) o produce (salida) la utilización del arco (y de su transición).

La transición $t$ está habilitada si y solo si $M(p) \geq W(p,t) \forall p \in I(t)$. Cuando $t$ se dispara:

- $\forall p \in I(t): M(p) \leftarrow M(p) - W(p, t)$
- $\forall p \in O(t): M(p) \leftarrow M(p) + W(p, t)$
