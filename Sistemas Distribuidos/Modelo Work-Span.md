Es un modelo más cercano a la realidad para estimar optimizaciones. Provee una cota inferior y una cota superior para el speedup.

- El *work*, o trabajo, de un cómputo ejecutado por $p$ procesos es la cantidad total de operaciones primitivas realzadas por todos los procesos.
- El *span* es la longitud de la mayor cadena de operaciones que deben realizarse secuencialmente (camino crítico).
- El costo expresa el tiempo total invertido por todos los procesadores.

Luego, se define:

- $T_1$: Tiempo en ejecutar el algoritmo con un solo proceso.
- $T_\infty$: Tiempo en ejecutar el camino crítico de la operación.

Entonces, las cotas serán:

- $\text{Cota Superior} = \min (P, T_1/T_\infty)$
- $\text{Cota Inferior} = (T_1 - T_\infty) / P + T_\infty$
