## Información de Catálogo

Los gestores guardan distinto tipo de información de catálogo que es utilizada para estimar costos y optimizar consultas. Utilizaremos la siguiente notación teórica:

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

## Plan de Consulta y Plan de Ejecución

La optimización de una consulta se inicia con una expresión en álgebra relacional. La expresión se optimiza a través de una heurística, y utilizando reglas de equivalencia, obteniendo un **plan de consulta**.

Luego, cada plan de consulta lógico se materializa para obtener un **plan de ejecución** en el que se indica el procedimiento físico: estructuras de datos a utilizar, indices, algoritmos, etc.

Para comparar distintos planes de ejecución, necesitamos estimar su costo. Algunos de los factores que inciden en el rendimiento son:

- El costo de acceso a disco (lectura o escritura)
- El costo de procesamiento
- El costo de uso de memoria
- El costo de uso de red

Solo estudiaremos el costo de acceso a disco, por ser los de mayor envergadura en bases de datos relacionales centralizadas.

El esquema de procesamiento de una consulta, puede verse como:

![[Esquema de Procesamiento 1699995958.png|475]]
