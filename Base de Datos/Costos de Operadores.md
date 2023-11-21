A partir de la [[Esquema de Procesamiento#Información de Catálogo|información de catálogo]], podemos estimar el costo de las distintas operaciones, según la estructura del disco.

Analizaremos los costos en función de cuantos accesos a discos se requiere

## Selección

Partimos de una selección básica del tipo $\sigma_\text{cond}(R)$, en donde $\text{cond}$ es una condición atómica. Analizaremos distintas situaciones para la comparación por igual.

### Búsqueda lineal

Si no tenemos índices, entonces debemos recorrer el disco en busca de los registros que cumplen con la condición. Consiste en explorar cada registro, analizando si se verifica la condición.

$$
	\text{cost}(\sigma) = B(R)
	$$

### Búsqueda con índice primario

Si contamos con índices, entonces podremos realizar consultas más eficientes. Este método se utiliza cuando $A_i$ es un atributo clave del que se tiene un índice primario, solo una tupla puede satisfacer la condición. Necesitaremos un acceso por cada nivel de árbol, más un acceso más por el bloque que contiene las tuplas.

$$

\text{cost}(\sigma) = \text{Height}(I(A_i, R)) + 1

$$

### Búsqueda con índice de ordenamiento

Se utiliza cuando $A_i$ no es clave, pero se tiene un índice de ordenamiento *(clustering)* por él. Las tuplas que coincidan con la condición se encuentran contiguas en distintos bloques.
$$

\text{cost}(\sigma) \approx \text{Height}(I(A_i, R)) + \Big\lceil\frac{B(R)}{V(A_i, R)}\Big\rceil

$$
Como los bloques están ordenados, aproximamos la cantidad de bloques con el valor buscado como la división entre la cantidad de bloques y la variabilidad.

### Búsqueda con índice secundario

Se utiliza cuando $A_i$ no tiene un índice de *clustering*, pero existe un índice secundario asociado a él. Las tuplas que coincidan con la condición se encuentran dispersas en distintos bloques.

$$

\text{cost}(\sigma) \approx \text{Height}(I(A_i, R)) + \Big\lceil\frac{n(R)}{V(A_i, R)}\Big\rceil

$$
Aproximaremos la cantidad de valores posibles, como la división entre la cantidad de tuplas y la variabilidad. Luego asumimos el peor caso (no están ordenados), cada una de estas tuplas está en un bloque distinto.
### Selecciones complejas

Si la selección involucra la conjunción de varias condiciones simples, pueden adoptarse distintas estrategias:

- Si uno de los atributos tiene un índice asociado, se aplica primero esta condición, y luego se selecciona del resultado a aquellas tuplas que cumplen con las demás condiciones.
- Si hay un índice compuesto que involucra a atributos de más de una condición, se utiliza este índice y luego se seleccionan las tuplas que cumplen los demás criterios.
- Si hay índices simples para varios atributos, se utilizan los índices por separado y luego se intersecan los resultados.

Si la selección involucra una disyunción de condiciones simples, debemos aplicar las mismas por separado y luego unir los resultados. Si uno de los atributos no dispone de índice, hay que usar fuerza bruta.

## Proyección

Dividiremos el análisis de la proyección $\pi_X(R)$ en dos casos.

### Con superclave

Si $X$ es superclave, no es necesario eliminar duplicados, por lo que el costo será:

$$

cost(\pi) = B(R)

$$
### Sin superclave

Si $X$ no es superclave, entonces debemos eliminar duplicados. Llamaremos $\hat\pi_X(R)$ a la proyección de multiconjuntos.

Podemos ordenar la tabla en memoria si la tabla entra en memoria, en caso contrario el costo usando un ordenamiento externo será:

$$

\text{cost}(\pi) = \text{cost}(\text{ord}_M(R)) = 2B(R) \cdot [\log_{M-1}(B(R))] - B(R)

$$
También podemos utilizar una estructura de *hash*. Si no entra en memoria, el costo usando un *hashing* externo será de:
$$

\text{cost}(\pi) = B(R) + 2\cdot B(\hat\pi_X(R))

$$
Si la consulta de SQL no incluye `DISTINCT`, entonces el resultado es un multiconjunto y el costo es siempre $B(R)$.

## Unión e Intersección

Primero, ordenamos las tablas $R$ y $S$. Si alguno no entra en memoria, utilizamos un *sort* externo.

Asumimos que no se devuelven repetidos (comportamiento por defecto de SQL). Se puede modificar sencillamente en caso de querer repetidos.

Procesaremos ambas tablas ordenadas haciendo un *merge* que avanza por las filas $r_i$ y $s_i$ ordenadas de cada tabla, el costo es:

$$

\text{cost}(\cup | \cap) = \text{cost}(\text{ord}_M(R)) + \text{cost}(\text{ord}_M(S)) + 2B(R) + 2B(S)

$$
Los algoritmos utilizados sobre las filas $r_i$ y $s_i$ serán los algoritmos clásicos de operaciones entre conjuntos.

## Junta

Existen distintos métodos para calcular una junta. Solo indicaremos el costo de lectura de datos y cálculo del resultado. Para calcular el costo de almacenamiento, es necesario estimar la cardinalidad del resultado.

### Loops anidados por bloque

Dadas dos relaciones $R$, $S$, se utiliza cuando no tenemos índices, y consiste en tomar cada par de bloques de ambas relaciones, y comparar todas sus tuplas entre sí.

El costo de procesar cada bloque de $R$ es de $1 + B(S)$, y el total es de: $B(R)\cdot(1+B(S))$, suponiendo que utilizamos $R$ como pivote. Elegiremos como pivote el más conveniente (el de menor cantidad de bloques):

$$

\text{cost}(R*S) = \min(B(R) + B(R)\cdot B(S), B(S) + B(S) \cdot B(R))

$$
Esta estimación es un peor caso, suponiendo que solo podemos tener un bloque de cada tabla simultáneamente en memoria. Si pudiéramos cargar una de las tablas completa en memoria, sobrará un bloque, tendríamos el mejor caso:

$$

\text{cost}(R*S) = B(R) + B(S)

$$
### Método de único loop

Si el atributo de junta $A_i$ tiene un índice asociado en $R$, por ejemplo, podemos recorrer las tuplas de $S$ y para cada una de ellas buscar en el índice las tuplas de $R$ en que el atributo coincide. Luego, el costo será $B(S)$, sumado al costo de selección multiplicado por la cantidad de tuplas.

Si el índice es primario, entonces el costo será:

$$

\text{cost}(R*S) = B(S) + n(S)\cdot(\text{Height}(I(A_i, R)) + 1)

$$
Si el índice es de ordenamiento, entonces el costo será:

$$

\text{cost}(R*S) = B(S) + n(S)\cdot(\text{Height}(I(A_i, R)) + \Big\lceil\frac{B(R)}{V(A_i, R)}\Big\rceil

)

$$
Si el índice es secundario, entonces el costo será:

$$

\text{cost}(R*S) = B(S) + n(S)\cdot(\text{Height}(I(A_i, R)) + \Big\lceil\frac{n(R)}{V(A_i, R)}\Big\rceil

)

$$
> [!note] Nota
> En caso donde las tablas son chicas, no siempre es mas efectivo este método

### Método de sort-merge