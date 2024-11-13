El paralelismo es una forma de computación en la cual varios cálculos pueden realizarse simultáneamente,​ basado en el principio de dividir los problemas grandes para obtener varios problemas pequeños, que son posteriormente solucionados en paralelo.

Los objetivos de la paralelización son:

- Reducir el tiempo de cómputo de una tarea (latencia)
- Incrementar la cantidad de tareas que se pueden realizar en paralelo (throughput)
- Reducir la energía consumida al realizar todas las tareas

## Speedup

Se define el **speedup** como el ratio de optimización de una operación.

## Camino Crítico

El **camino crítico** es la máxima longitud de tareas secuenciales a computar. Define el mejor rendimiento que se puede obtener al realizar un conjunto de tareas.

## Modelos de Análisis

[[Ley de Amdahl]]

### Ley de Gustafson

> Speedup should be measured by scalling the problem to the number of processors, not by fixing the problem size.

Tiene un enfoque menos pesimista al calcular el speedup. Si no se puede mejorar la solucion, podemos modificar el problema para aprovechar mas los recursos.

Aumentar el paralelismo puede permitir la modificación del problema original para ejecutar más trabajo, aunque la parte serial no se pueda mejorar.

### Work-Span

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
