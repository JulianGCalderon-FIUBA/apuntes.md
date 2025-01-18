Es un modelo más cercano a la realidad para estimar optimizaciones.

- El *work*, o trabajo, de un cómputo ejecutado por $p$ procesos es la cantidad total de operaciones primitivas realzadas por todos los procesos. Es equivalente al tiempo que toma ejecutar el cómputo en un solo procesador, denotado como $T_1$.
- El *span* es la longitud de la mayor cadena de operaciones que deben realizarse secuencialmente (camino crítico).
- El costo expresa el tiempo total invertido por todos los procesadores.

El speedup $S_p$ se define como la mejora al usar $p$ procesos con respecto a una ejecución serial: $S_p = T_1 / T_p$.

El tiempo en ejecutar el camino crítico se puede denotar como $T_\infty$, equivalente al tiempo de realizar el cómputo con infinitos procesadores.

El modelo provee una cota superior y una copa inferior para el tiempo que toma ejecutar el cómputo en $p$ procesadores:

$$
\max(\text{work}/p, \text{span}) <= T_p < \text{work}/p + \text{span}
$$