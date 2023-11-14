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

**Búsqueda con índice primario:** Cuando $A_i$ es un atributo clave del que se tiene un índice primario, solo una tupla puede satisfacer la condición:

$$

\text{cost}(S_{3a}) = \text{Height}(I(A_i, R)) + 1

$$

**Búsqueda con índice de clustering:** Cuando $A_i$ no es clave, pero se tiene un índice de ordenamiento *(clustering)* por él. Las tuplas se encuentran contiguas en los bloques, los cuales estarán disjuntos.
$$

\text{cost}(S_5) = \text{Height}(I(A_i, R)) + \Big\lceil\frac{B(R)}{V(A_i, R)}\Big\rceil

$$
Como no sabemos en qué bloque se encuentra, debemos buscar todos los bloques. Pero como están ordenados, entonces la cantidad de bloques es menor. Podemos aproximar dividiendo la cantidad de bloques entre la cantidad de valores distintos.

**Búsqueda con índice secundario:** Cuando $A_i$ no tiene un índice de *clustering*, pero existe un índice secundario asociado a él, entonces.

$$

\text{cost}(S_6) = \text{Height}(I(A_i, R)) + \Big\lceil\frac{n(R)}{V(A_i, R)}\Big\rceil

$$
### Selecciones Complejas

Si la selección involucra la conjunción de varias condiciones simples, pueden adoptarse distintas estrategias:

- Si uno de los atributos tiene un índice asociado, se aplica primero esta condición, y luego se selecciona del resultado a aquellas tuplas que cumplen con las demás condiciones.
- Si hay un índice compuesto que involucra a atributos de más de una condición, se utiliza este índice y luego se seleccionan las tuplas que cumplen los demás criterios.
- Si hay índices simples para varios atributos, se utilizan los índices por separado y luego se intersecan los resultados.

Si la selección involucra una disyunción de condiciones simples, debemos aplicar las mismas por separado y luego unir los resultados. Si uno de los atributos no dispone de índice, hay que usar fuerza bruta.

## Proyección

Dividiremos el análisis de la proyección $\pi_X(R)$ en dos casos.

Si $X$ es superclave, no es necesario eliminar duplicados, por lo que el costo será:

$$

cost(\pi_X(R)) = B(R)

$$
Si $X$ no es superclave, entonces debemos eliminar duplicados. Llamaremos $\hat\pi_X(R)$ a la proyección de multiconjuntos.

Podemos ordenar la tabla en memoria si la tabla entra en memoria, en caso contrario el costo usando un ordenamiento externo será:

$$

\text{cost}(\pi_X(R)) = \text{cost}(\text{ord}_M(R)) = 2B(R) \cdot [\log_{M-1}(B(R))] - B(R)

$$
También podemos utilizar una estructura de *hash*. Si no entra en memoria, el costo usando un *hashing* externo será de:
$$

\text{cost}(\pi_X(R)) = B(R) + 2\cdot B(\hat\pi_X(R))

$$
Si la consulta de SQL no incluye `DISTINCT`, entonces el resultado es un multiconjunto y el costo es siempre $B(R)$.

## Unión e Intersección

Primero, ordenamos las tablas $R$ y $S$. Si alguno no entra en memoria, utilizamos un *sort* externo.

Asumimos que no se devuelven repetidos (comportamiento por defecto de SQL). Se puede modificar sencillamente en caso de querer repetidos.

Procesaremos ambas tablas ordenadas haciendo un *merge* que avanza por las filas $r_i$ y $s_i$ ordenadas de cada tabla, el costo es:

$$

\text{cost} = \text{cost}(\text{ord}_M(R)) + \text{cost}(\text{ord}_M(S)) + 2B(R) + 2B(S)

$$
Los algoritmos utilizados sobre las filas $r_i$ y $s_i$ serán los algoritmos clásicos de operaciones entre conjuntos.
