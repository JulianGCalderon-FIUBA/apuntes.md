## Selección

Partimos de una selección básica del tipo $\sigma_\text{cond}(R)$, en donde $\text{cond}$ es una condición atómica. Analizaremos distintas situaciones para la comparación por igual.

Existen distintas estrategias de búsqueda, según los recursos con los que contamos.

### Métodos de File Scan

Estos métodos recorren el disco en busca de los registros que cumplen con la condición.

La búsqueda lineal consiste en explorar cada registro, analizando si se verifica la condición.

$$
	\text{cost}(S_{3a}) = 1
	$$

### Métodos de Index Scan

Estos métodos utilizan un índice de búsqueda.

**Búsqueda con índice primario:** Cuando $A_i$ es un atributo clave del que se tiene un índice primario, solo una tupla puede satisfacer la condición.

- Si utilizamos un árbol de búsqueda, entonces tendremos:
	$$
	\text{cost}(S_1) = B(R)
	$$
- Si utilizamos una clave de hash, entonces tendremos:
	$$
	\text{cost}(S_{3a}) = \text{Height}(I(A_i, R)) + 1
	$$

#### Búsqueda con índice de clustering

Cuando $A_i$ no es clave, pero se tiene un índice de ordenamiento (clustering) por él.
