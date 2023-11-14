El esquema de procesamiento de una consulta, puede verse como:

![[Esquema de Procesamiento 1699995958.png|475]]

## Información de Catálogo

Los gestores guardan distinto tipo de información de catálogo que es utilizada para estimar costos y optimizar consultas. Utilizaremos la siguiente notación:

- $n(R)$: Cantidad de tuplas de la relación $R$.
- $B(R)$: Cantidad de bloques de almacenamiento que ocupa $R$
- $V(A,R)$: Cantidad de valores distintos que adopta el atributo $A$ en $R$ (variabilidad).
- $F(R)$: Cantidad de tuplas de $R$ que entran en un bloque (factor de bloque).

$$
F(R) = \frac{n(R)}{B(R)} \implies B(R) = \frac{n(R)}{F(R)}
$$

También se almacena información sobre la cantidad de niveles que tienen los índices construidos, y la cantidad de bloques que ocupan sus hojas.

- $\text{Height}(I(A,R))$: Altura del índice de búsqueda $I$ por el atributo $A$ de la relación $R$.
- $\text{Length}(I(A,R))$: Cantidad de bloques que ocupan las hojas del índice $I$.

Actualiza la información de catálogo en cada operación de ABM puede ser muy costoso. Los gestores suelen hacerlo concierta periodicidad, o cuando están ociosos, o cuando el usuario lo indica explícitamente.
