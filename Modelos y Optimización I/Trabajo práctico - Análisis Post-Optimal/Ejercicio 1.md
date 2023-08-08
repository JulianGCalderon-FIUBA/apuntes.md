# Enunciado

El Ministerio evalúa dos alternativas para el plan: conseguir 4 drones más con los que formar equipos o destinar 4 de los 24 drones actuales para entrenamiento intensivo, con lo que no estarán disponibles para la formación de equipos, pero se podrá obtener una mejora de 18 puntos en la eficacia resultante. ¿Cuál de estas dos alternativas será la mejor?

# Resolución

Se proponen las siguientes dos alternativas:

1. La primera alternativa consiste en obtener cuatro drones más con los que formar equipos. En el modelo, esto se traduce a aumentar $b_4$ en $4$ unidades, hasta una disponibilidad de $28$ drones.
2. La segunda alternativa consiste en destinar cuatro drones de los ya existentes a entrenamiento intensivo. En el modelo, esto se traduce a reducir $b_4$ en $4$ unidades, hasta una disponibilidad de $20$ drones, pero aumentando el funcional total en $18$ puntos de eficacia.

Como observamos en el planteo inicial, los drones son un recurso ***saturado***, por lo que podría convenir conseguir más equipos. Sin embargo, en la tabla óptima del primal podemos observar que su valor marginal es de cero, lo que indica que aumentar la disponibilidad del recurso no modificará la solución optima. Esto se debe a que, si bien es un recurso saturado, se encuentra en un punto sobre definido. Aliviar una restricción no cambiará la solución óptima, ya que seguirá siendo limitada por el resto de restricciones del punto (intersección entre la segunda y la tercera restricción).

Inicialmente, descartamos la primer alternativa, debido a que no ofrece beneficios a efectos del modelo. Procederemos a analizar la segunda alternativa, para ver si esta beneficia la solución optima.

Calculamos el rango variación para el valor independiente de la restricción de los drones $(b_4)$, para saber con seguridad qué pasa si se consiguiera más o menos del recurso:

|  |  |  | $28$ | $16$ | $8$ | $b_4$ |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $Y_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ |
| $16$ | $Y_2$ | $5$ | $1/2$ | $1$ | $0$ | $1/2$ | $1/2$ | $-1/2$ | $0$ |
| $8$ | $Y_3$ | $8$ | $1$ | $0$ | $1$ | $2$ | $-2$ | $0$ | $-1$ |
|  |  | $Z = 144$ | $-12$ | $0$ | $0$ | $24-b_4$ | $-8$ | $-8$ | $-8$ |

Observamos que para que la solución siga siendo óptima se debe cumplir que $24 - b_4\le 0$, que es lo mismo que decir que $24\le b_4$. Por lo tanto, podemos confirmar lo que se mencionó previamente: conseguir más del recurso no va a modificar la solución óptima. No obstante, notamos que si se eligiera la segunda alternativa sí se modificaría la solución óptima, ya que $24 - 20 = 4\not \le 0$, por lo que debemos seguir iterando para hallar el nuevo punto óptimo.

Modificamos el termino independiente a $b_4 = 20$ y realizamos una iteración del método simplex para analizar la solución en este nuevo punto. Entra $Y_4$, y sale $Y_3$.

|  |  |  | $28$ | $16$ | $8$ | $20$ |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $Y_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ |
| $16$ | $Y_2$ | $3$ | $1/4$ | $1$ | $-1/4$ | $0$ | $1$ | $-1/2$ | $1/4$ |
| $20$ | $Y_4$ | $4$ | $1/2$ | $0$ | $1/2$ | $1$ | $-1$ | $0$ | $-1/2$ |
|  |  | $Z = 128$ | $-14$ | $0$ | $-2$ | $0$ | $-4$ | $-8$ | $-6$ |

En la siguiente tabla, podemos observar que los $z_j - c_j$ de las variables son negativos, indicando que nos encontramos en un punto óptimo. En este nuevo punto óptimo se obtiene una eficacia de $128$ puntos, y se modifica el esquema productivo al siguiente:

- Los drones siguen siendo un recurso saturado, pero ya no es más un punto degenerado, por lo que tienen un valor marginal de $4$ puntos de eficacia por unidad que se pueda conseguir.
- Los helicópteros no son más un recurso saturado, si no que tienen un sobrante de $2$ unidades.
- Se arman ahora $8$ equipos de Combate del Fuego y $6$ equipos de Apoyo Logístico.
- Se siguen utilizando todas las autobombas, que ahora tienen un valor marginal de $3$.
- Se siguen sin utilizar todas las brigadas, y sobran $6$.
- Se podrían armar $4$ equipos más de Combate del Fuego, y se seguiría cumpliendo la diferencia necesaria entre los distintos equipos.

Podemos observar de esta nueva alternativa que el funcional se reduce a $128$ puntos de eficacia, pero debemos agregarle artificialmente el valor aportado por el entrenamiento intensivo $(18)$. Obtenemos un puntaje final de $146$ puntos de eficacia, que es mejor a la solución inicial.

Por lo tanto, la segunda alternativa resulta más beneficiosa ya que, si bien se arman menos equipos de Apoyo Logístico, se logra mejorar la eficacia total, mientras que con la primera alternativa no se conseguirían más puntos, ni se modificaría el esquema original. 

## Análisis Grafico

Para la primera alternativa, graficamos el poliedro aumentando los drones. Como se puede observar en la imagen, al aumentar la cantidad de drones el poliedro no se agrandará, debido a que hay dos restricciones que impiden que eso suceda (disponibilidad de helicópteros y autobombas). Para cambiar el poliedro, debemos aflojar además alguna de ellas.

![[Ejercicio 1 1.png|Untitled]]

Para la segunda alternativa podemos observar que el poliedro de soluciones se achica, formando dos nuevos vértices, $E$ y $F$, donde el óptimo es el punto $E=(8,6)$ con $Z=128$. A pesar de que el poliedro, la alternativa sigue siendo beneficiosa, ya que debemos sumarle manualmente los $18$ puntos de eficacia que se obtiene al ceder los cuatro drones. Luego, la eficacia final del plan será de $146$, que es mejor a la original, de $144$.

![[Ejercicio 1 2.png|Untitled]]

## Análisis por Software

Por ***software***, podremos simplemente resolver el modelo con ambas alternativas, y observar la solución optima. Primero, evaluamos la primera alternativa.

![[Ejercicio 1 3.png|Untitled]]

Observamos que el punto óptimo permanece igual, con el mismo puntaje final.

Ahora, evaluamos la segunda alternativa:

![[Ejercicio 1 4.png|Untitled]]

Vemos, que el punto óptimo se encuentra en $X = (8,6)$, y el puntaje final es de $Z = 128$.