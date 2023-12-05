## Selección

### Estimación de costos

- **Búsqueda lineal:** $\text{cost}(\sigma) = B(R)$
- **Índice primario:** $\text{cost}(\sigma) = \text{Height}(I(A_i, R)) + 1$
- **Índice de ordenamiento:** $\text{cost}(\sigma) \approx \text{Height}(I(A_i, R)) + \Big\lceil\frac{B(R)}{V(A_i, R)}\Big\rceil$
- **Índice secundario:** $\text{cost}(\sigma) \approx \text{Height}(I(A_i, R)) + \Big\lceil\frac{n(R)}{V(A_i, R)}\Big\rceil$

## Proyección

- **Con superclave:** $cost(\pi) = B(R)$
- **Sin superclave:** 
	- **Sor**$cost(\pi) = B(R)$

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

Genéricamente, podemos calcular el costo, siendo $M$ la cantidad de memoria disponible (en bloques). Notemos que debemos guardar un bloque para el desfile, y otro bloque para los resultados.

$$

B(R) + \lceil B(R)/(M-2)\rceil \cdot B(S)

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

Si existe la consulta simétrica, entonces podremos calcular ambas estimaciones y elegir la más eficiente.

> [!note] Nota
> En caso donde las tablas son chicas, no siempre es mas efectivo este método

### Método de sort-merge

Este método consiste en ordenar los archivos de cada tabla por el atributo de junta. Si entran en memoria, el ordenamiento puede hacerse con *quicksort* y el costo de acceso a disco es solo $B(R) + B(S)$.

Si los archivos no caben en memoria, debe utilizarse un algoritmo de *sort* externo. El costo de ordenar $R$ y volverlo a guardar en disco es de aproximadamente $2B(R) \cdot \lceil\log_{M-1}(B(R))\rceil$

Una vez ordenados, se hace un *merge* de ambos archivos que solo selecciona aquellos pares de tuplas en que coinciden los atributos de junta. El *merge* recorre una única vez cada archivo, con un costo total de $B(R) + B(S)$.

El costo total entonces es:

$$

\text{cost}(R*S) = B(R) + B(S) + 2B(R) \cdot \lceil\log_{M-1}(B(R))\rceil + 2B(S) \cdot \lceil\log_{M-1}(B(S))\rceil

$$

### Método de junta hash GRACE

La idea de este método es particionar las tablas $R$ y $S$ en $m$ grupos utilizando una función de hash $h(X)$, aplicada sobre los atributos de junta $X$. El costo del particionado (y envío a disco) será de: $2 \cdot (B(R) + B(S))$. Notemos que si dos tuplas $r, S$ cumplen que $h(r.X) = h(s.X)$ no implica que $r.X = s.X$.

Luego, cada par de grupos se combina verificando si se cumpla la condición de junta con un enfoque de fuerza bruta. No es necesario combinar $R_i, S_j$, con $i \neq j$. El costo de la combinación de $R_i$ y $S_i$ es de $B(R_i) + B(S_i)$.

El número $m$ es escogido de manera que haya un bloque para cada partición, al momento de realizar el *hashing* (y sobre un bloque para el desfile), y cada partición entre completa en memoria en el momento de realizar la junta.

De igual forma, el número $m$ debe ser menor que la variabilidad, pues no sirve de nada tener particiones vacías.

El costo total entonces es:

$$

\text{cost}(R*S) = 3 \cdot (B(R) + B(S))

$$

### Pipelining

En muchos casos, el resultado de un operador puede ser procesado por el operador siguiente en forma parcial (es decir, sin necesidad de que el operador anterior haya terminado de generar todas las tuplas)

Esta estrategia se denomina *pipelining*, y los gestores suelen utilizarla en los planes de ejecución siempre que sea posible.

Al calcular el costo de dos operaciones anidadas $O_2(O_1(R))$, debemos considerar que en el caso de utilizar pipelining no será necesario tener todos los bloques de la salida de $O_1$ para comenzar a calcular $O_2$. En particular, no tendremos que materializar toda la salida de $O_1$ por falta de espacio en memoria.
