## Clique y Anticlique

Un **clique** es un subconjunto de vértices tal que cualquier par de ellos está unido por una arista, también llamado **clan**.

- El número de clique $\omega(G)$ es el cardinal del clique máximo.

Un **anticlique** es un subconjunto de vértices tal que cualquier par de vértices no está unido por una arista, también llamado conjunto independiente.

- El número de independencia $\alpha(G)$ es el cardinal del anticlique máximo.

Un clique/anticlique es maximal si no es un subconjunto de otro*.*

## Cubrimiento de vértices

Sea $G$ un grafo, $S \subset V(G)$ es un cubrimiento de vértices si y solo si cualquier arista $uv \in E(G)$ tiene uno de sus extremos en $S$.

- El invariante $\beta(G)$ define el cardinal del mínimo cubrimiento
- Un cubrimiento de vértices es minimal si este no incluye a otro cubrimiento de vértices.

$$
\alpha + \beta = n
$$

Si $T$ es un conjunto independiente de vértices, no hay ninguna arista entre cualquier par de vértices del conjunto, luego cualquier arista en $G$ tiene incide al menos una vez en $V(G) - T$, luego este será un cubrimiento de vértices.

## Dominación de vértices

Sea $G$ u grafo, $S \in V(G)$ es un conjunto de vértices dominantes si y solo si $\bigcup_{v \in S}$ $\Gamma(v) = V(G)$. Este es fuertemente dominante si se cumple la propiedad con el entorno cerrado $\Gamma[v)$

- Se define el número de dominancia $\gamma(G)$ como el cardinal del mínimo dominante
- Se define el número fuerte de dominancia $\gamma_s(G)$ como el cardinal del mínimo fuertemente dominante

## Apareamiento

Al igual que con los vértices, un apareamiento *(o matching)* es un conjunto independiente de aristas (dos aristas son independientes si no tienen un vértice común).

Un apareamiento será maximal si no es subconjunto propio de otro apareamiento y es máximo si no hay otro con mayor cardinal.

- El cardinal del máximo apareamiento se denomina $\alpha'(G)$, y se conoce como número de matching.
- Un matching es perfecto si es, a su vez, un cubrimiento de aristas.

## Cubrimiento de Aristas

Análogo al cubrimiento de vértices. $S$ es un cubrimiento de aristas si y solo cualquier vértice del grafo es alcanzado por una de las aristas del cubrimiento.

Un cubrimiento de aristas será minimal si no incluye a otro matching y es mínimo si no hay otro con menor cardinal.

El número del cardinal mínimo se denota $\beta'(G)$ se conoce como número de cubrimiento de aristas

De forma análoga, se demuestra que:

$$
\alpha' + \beta' = n
$$

Sea $S$ un apareamiento máximo, el conjunto de vértices que no pertenecen al apareamiento es un conjunto independiente, luego para cubrirlos se necesita al menos una arista para cada uno. Luego, la forma más óptima de seleccionar el resto de vértices es con una arista para cada par de vértices, lo cual se obtiene seleccionando $S$.
