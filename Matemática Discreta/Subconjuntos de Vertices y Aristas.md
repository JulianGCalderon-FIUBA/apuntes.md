## Clique y Anticlique

Un **clique** es un subconjunto de vertices tal que cualquier par de ellos esta unido por una arista, también llamado ***clan***.

- El numero de clique $\omega(G)$ es el cardinal del clique máximo.

Un **anticlique** es un subconjunto de vertices tal que cualquier par de vertices no esta unido por una arista, también llamado conjunto independiente.

- El numero de independencia $\alpha(G)$ es el cardinal del anticlique máximo.

Un *clique/anticlique* es maximal si no es un subconjunto de otro*.*

## Cubrimiento de Vertices

Sea $G$ un grafo, $S \subset V(G)$ es un cubrimiento de vertices si y solo si cualquier arista $uv \in E(G)$ tiene uno de sus extremos en $S$.

- El invariante $\beta(G)$ define el cardinal del mínimo cubrimiento
- Un cubrimiento de vertices es minimal si este no incluye a otro cubrimiento de vertices.

$$
\alpha + \beta = n
$$

Si $T$ es un conjunto independiente de vertices, no hay ninguna arista entre cualquier par de vertices del conjunto, luego cualquier arista en $G$ tiene incide al menos una vez en $V(G) - T$, luego este será un cubrimiento de vertices.

## Dominación de Vertices

Sea $G$ u grafo, $S \in V(G)$ es un conjunto de vertices dominantes *sii* $\bigcup_{v \in S}$ $\Gamma(v) = V(G)$. Este es fuertemente dominante si se cumple la propiedad con el entorno cerrado $\Gamma[v)$

- Se define el numero de dominancia $\gamma(G)$ como el cardinal del mínimo dominante
- Se define el numero fuerte de dominancia $\gamma_s(G)$ como el cardinal del mínimo fuertemente dominante

## Apareamiento

Al igual que con los vertices, un apareamiento es un conjunto independiente de aristas (dos aristas son independientes si no tienen un vértice común).

Un apareamiento será maximal si no es subconjunto propio de otro ***matching*** y es máximo si no hay otro con mayor cardinal.

- El cardinal del máximo apareamiento se denomina $\alpha'(G)$, y se conoce como ***numero de matching***.
- Un ***matching*** es perfecto si es a su vez, un cubrimiento de aristas.

## Cubrimiento de Aristas

Análogo al cubrimiento de vertices. $S$ es un cubrimiento de aristas si y solo cualquier vértice del grafo es alcanzado por una de las aristas del cubrimiento.

Un cubrimiento de aristas será minimal si no incluye a otro ***matching*** y es mínimo si no hay otro con menor cardinal.

El numero del cardinal mínimo se denota $\beta'(G)$ se conoce como numero de cubrimiento de aristas

De forma análoga, se demuestra que:

$$
\alpha' + \beta' = n
$$

Sea $S$ un apareamiento máximo, el conjunto de vertices que no pertenecen al apareamiento es un conjunto independiente, luego para cubrirlos se necesita al menos una arista para cada uno. Luego, la forma mas óptima de seleccionar el resto de vertices es con una arista para cada par de vertices, lo cual se obtiene seleccionando $S$.
