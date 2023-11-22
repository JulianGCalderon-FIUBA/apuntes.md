Como parte de la estimación del [[Costos de Operadores]], es necesario a veces estimar el tamaño de las relaciones intermedias antes de calcularlas. Se espera que una estimación cumpla con los siguientes requisitos:

- Debe ser precisa
- Debe ser fácil de calcular
- No debe depender del método utilizado

## Proyección

Si la proyección no elimina duplicados, entonces podremos utilizar una regla simple para obtener la cantidad de bloques que ocupa una proyección. Necesitaremos el tamaño de los campos, la cantidad de tuplas, y el tamaño de los bloques.

$$
B(\pi_{\text{DNI}}(\text{Persona})) = \frac{\text{\#Tuplas} \cdot \text{size}(\text{DNI})}{\text{size}(\text{bloque})}
$$

Si se eliminan duplicados, utilizaremos la variabilidad para estimar de forma más precisa la cardinalidad de la proyección.

## Selección

La selección reduce el número de tuplas en el resultado, aunque mantiene el tamaño de cada tupla.

Para estimar el tamaño de una selección $\sigma_{A_i=c}(R)$, utilizaremos la variabilidad de $A_i$ en $R$, denominada $V(A_i, R)$.

$$
n(\sigma_{A_i=c}(R)) = \frac{n(R)}{V(A_i, R)}
$$

Se le suele llamar a la fracción $\frac{1}{V(A_i, R)}$ se denomina selectividad de $A_i$ en $R$.

Si quiero calcular la cantidad de bloques, podremos utilizar análogamente:

$$
B(\sigma_{A_i=c}(R)) = \frac{B(R)}{V(A_i, R)}
$$

Este método no nos permite selecciones con otros operadores, y asume una distribución uniforme.

## Selección con histograma

El histograma nos resume la distribución de los valores que toma un atributo en una instancia de relación dada. No necesariamente cubrirá a todos los valores.
