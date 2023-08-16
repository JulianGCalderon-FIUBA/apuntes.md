---
title: Análisis de Sensibilidad
---

## Conceptos Básicos

### Recursos Sobrantes y Saturados

Cuando un recurso no tiene sobrante, entonces se dice que este recurso es un recurso saturado. En otro caso, diremos que es un recurso sobrante.

Cuando aumentamos la disponibilidad de un recurso sobrante, podemos esperar que aumente el funcional, pero esto no ocurrirá siempre.

### Significado de $z_j - c_j$

Los valores de $z_j - c_j$ tienen un significado

- Si la columna le pertenece a real del problema, entonces diremos que el valor representa el costo de oportunidad del producto (CO).
- Si la columna le pertenece a una variable slack, diremos que él representa el valor marginal del recurso (VM).

### Costo de Oportunidad

El costo de oportunidad es distinto de cero cuando la variable correspondiente al producto no está en la base (porque vale cero)

El costo de oportunidad de un producto índica cuanto va a desmejorar el funcional si tenemos la obligación de fabricar una unidad de ese producto.

En el software LINDO, visualizaremos estos valores bajo la columna *reduced cost.*

### Valor Marginal

El valor marginal es distinto de cero cuando la variable slack de la restricción no está en la base (porque vale cero)

El valor marginal indica cuanto va a mejorar el funcional si esa restricción se afloja en una unidad

- Si la restricción es de menor o igual, aflojar la restricción implica aumentar el término independiente
- Si la restricción es de mayor o igual, aflojar la restricción implica disminuir el término independiente

En el software LINDO, visualizaremos estos valores bajo la columna *dual cost.*

## Análisis de Sensibilidad

### Rango de Variación

Si planteamos genéricamente un coeficiente $c_k$, podremos calcular los $z_j - c_j$ de las columnas afectadas para analizar el rango de coeficientes para el cual la solución sigue siendo estructuralmente la misma (intersección de las mismas restricciones).

Si en lugar de analizar los coeficientes del funcional, queremos analizar el rango de variación de los términos independientes $b_k$, dependeremos del [[Planteo Dual]].

Debido a que los términos independientes del planteo primal serán los coeficientes del planteo dual, podremos realizar un análisis de curva de oferta para el planteo dual.

El rango de variación del coeficiente $c_j$ del problema dual, será el rango de variación del término independiente $b_i$ asociado en el problema primal. Recordemos que el término independiente de la restricción $j$ del problema primal será el coeficiente $c_j$ del problema dual.

> [!example]- Rango de Variación
> 
> 
> Partiremos de una tabla óptima para un problema dado
> 
> | | | | $2$ | $2$ | $5$ | $0$ | $0$ |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
> | $2$ | $x_2$ | $3.5$ | $-1.5$ | $1$ | $0$ | $-0.5$ | $0.5$ |
> | $5$ | $x_3$ | $6.5$ | $-0.5$ | $0$ | $1$ | $-0.5$ | $-0.5$ |
> | | | $39.5$ | $-7.5$ | $0$ | $0$ | $-3.5$ | $-1.5$ |
> 
> Ahora, plantearemos un valor genérico para $c_2$ y analizaremos los $z_j - c_j$ para cada caso afectado, notemos que los elementos de la base no serán afectados, ya que su $z_j - c_j$ siempre será cero.
> 
> | | | | $2$ | $c_2$ | $5$ | $0$ | $0$ |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
> | $c_2$ | $x_2$ | $3.5$ | $-1.5$ | $1$ | $0$ | $-0.5$ | $0.5$ |
> | $5$ | $x_3$ | $6.5$ | $-0.5$ | $0$ | $1$ | $-0.5$ | $-0.5$ |
> | | | $39.5$ | $-1.5c_2 - 4.5 $ | $0$ | $0$ | $-0.5c_2 -2.5$ | $0.5c_2 - 2.5$ |
> 
> Para que la solución sea algebraicamente la misma, entonces los $z_j - c_j$ deberán ser todos negativos (o positivos, en caso de que nos encontremos con un problema de maximización)
> 
> $$-1.5c_2 - 4.5 \leq 0 \implies c_2 \geq -3$$
> 
> $$ -0.5c_2 - 2.5 \leq 0 \implies c_2 \geq -5 $$
> 
> $$ 0.5c_2 - 2.5 \leq 0 \implies c_2 \leq 5 $$
> 
> Luego, el rango de variación de $c_2$ será de:
> 
> $$ -3 \leq c_2 \leq 5$$
> 
> Este rango es únicamente válido si mantenemos el resto de coeficientes como constante, luego en análisis de variación se realizara de a un coeficiente a la vez.
> 
> Notemos que si hay algún $z_j - c_j$ fuera de la base con valor cero, estaremos ante soluciones alternativas, se considera este caso como aún estructuralmente equivalente (ya que una de las soluciones óptimas lo será, aunque surgirá otra).

> [!example]- Análisis con LINDO
> 
> En lindo, podremos visualizar el rango de variación para tanto los coeficientes del funcional como los términos independientes de las restricciones.
> 
> ```jsx
> RANGES IN WHICH THE BASIS IS UNCHANGED:
> 
> 		  OBJ COEFFICIENT RANGES
> 
> VAR     CURRENT   ALLOWABLE  ALLOWABLE
> 				 COEF     INCREASE   DECREASE
> 
> X1       8.0       2.0        3.0
> X2       10.0      6.0        2.0
> 
> 		  RIGHTHAND SIDE RANGES
> 
> ROW      CURRENT   ALLOWABLE  ALLOWABLE
> 		   RHS     INCREASE   DECREASE
> 
> AZ       600.0     200.0      100.0
> CR       600.0     INFINITY   200.0
> AL       800.0     100.0      200.0
> ```

### Curva de Oferta

La curva de oferta es una gráfica que muestra, a los distintos valores que puede tomar el coeficiente $c_j$ de ese producto, qué cantidad de producto $x_j$ conviene fabricar.

La forma de esta gráfica será una función escalonada no decreciente (en caso de un problema de maximización). Dentro de cada rango de variación, los valores que tomarán las variables serán constantes (soluciones estructuralmente equivalentes). Por lo que para cada rango, tendremos un valor fijo de $x_j$.

Para calcular la curva de oferta para un coeficiente $c_k$ y una variable $x_k$:

1. Hallamos el rango de variación del coeficiente $c_k$ en la solución óptima y el valor asociado $x_k$
2. Proponemos un nuevo $c_k$ para cada valor en los extremos del rango y calculamos la tabla en la solución alternativa.
3. Repetimos el algoritmo hasta hallar todos los rangos faltantes (debemos ocupar el rango completo de los números reales)
4. Graficamos la curva de oferta a partir de cada rango y el valor del $x_k$ asociado.

Notemos que al modificar los coeficientes, no modificamos el poliedro de soluciones factibles, sino la dirección del funcional (esto puede ocasionar que el punto óptimo se mueva). Debido a esto, las cantidades máximas de producto serán constantes en cada intervalo (solo modificamos que punto será el óptimo, pero no su posición)

### Gráfico de Valor Marginal

De la misma forma que se realiza la curva de oferta, podríamos graficar a los distintos valores que puede tomar el término independiente $b_j$ de una restricción, el valor marginal de la variable $x_j$. En caso de un problema de maximización, esta será una función escalonada no creciente. Esto se debe a que a mayor cantidad tenga de un recurso, menor será el valor marginal del mismo.

Para calcular la curva, el procedimiento será el mismo, pero desde la tabla óptima del planteo dual. Recordemos que el término independiente $b_j$ del problema primal, será el coeficiente $c_j$ del problema dual, y que el $z_j - c_j$ del problema primal, será el $y_j$ de su variable asociada en el problema dual.

Notemos que al modificar los términos independientes, estamos modificando el poliedro de soluciones factibles. Particularmente, estamos desplazando las restricciones de forma paralela. Debido a esto cambiará la posición de los puntos óptimos, por lo que su valor variará linealmente en el rango, lo que ocasionará que el costo de oportunidad de cada producto sea constante.

En los saltos de valor marginal, se encuentran soluciones alternativas. Ambos valores marginales son válidos. Si obtenemos recurso, nos quedaremos con el valor marginal inferior. Si entregamos recurso, nos quedaremos con el valor marginal superior.

### Variación Simultánea de Dos Recursos

Los rangos de variación no servirán, ya que estos planteaban una sola variable y el resto de valores permanecían constantes.

Tenemos la posibilidad de aumentar el término independiente de una restricción, reduciendo el término independiente de otra.

Para resolverlo, debemos (a partir de la relación entre los cambios de ambos términos) plantear genéricamente ambos términos, pero a partir de una sola variable.

> [!example]- Rango de Variación
> 
> Sea $b_1$ el término independiente original de la primera restricción, y $b_2$ el término independiente original de la segunda restricción.
> 
> Luego, se nos ofrece intercambiar productos de $b_1$ a razón $\beta$ productos de $b_2$. Es decir, por cada unidad de $b_1$ que obtengamos, perderemos $\beta$ unidades de $b_2$.
> 
> Podremos plantear genéricamente los términos como:
> 
> $$b_1' \to b_1 + \alpha$$
> 
> $$b_2' \to b_2 - \beta\alpha$$
> 
> Una vez tenemos una sola variable, podremos hallar el rango de variación con las técnicas vistas anteriormente.
