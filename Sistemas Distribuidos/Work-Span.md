Es un modelo más cercano a la realidad para estimar optimizaciones. Provee una cota inferior y una cota superior para el speedup.

Se toman las siguientes suposiciones:

- Paralelismo imperfecto: no todo el trabajo paralelizable se puede ejecutar al mismo tiempo.
- Greedy scheduling: Si un proceso está disponible, se ejecuta la tarea
- El tiempo de acceso a memoria es despreciable.
- El tiempo de ejecución entre procesos es despreciable.
- Posibilidad de analizar la operación o el algoritmo en caja blanca.

Luego, se define:

- $T_1$: Tiempo en ejecutar el algoritmo con un solo proceso.
- $T_\infty$: Tiempo en ejecutar el camino crítico de la operación.

Entonces, las cotas serán:

- $\text{Cota Superior} = \min (P, T_1/T_\infty)$
- $\text{Cota Inferior} = (T_1 - T_\infty) / P + T_\infty$
