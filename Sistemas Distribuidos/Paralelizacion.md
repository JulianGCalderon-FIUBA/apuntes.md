Los objetivos de la paralelización son:

- Reducir el tiempo de cómputo de una tarea (latencia)
- Incrementar la cantidad de tareas que se pueden realizar en paralelo (throughput)
- Reducir la energía consumida al realizar todas las tareas

Algunas definiciones útiles:

- Camino Crítico: Es la máxima longitud de tareas secuenciales a computar. Define el mejor rendimiento que se puede obtener al realizar un conjunto de tareas.
- Speedup: Se define el speedup como el ratio de optimización de una operación.

## Ley de Amdahl

> The effort expended on achieving high parallel processing rates is wasted unless it is accompanied by achievements in sequential processing rates of very nearly the same magnitude.

Permite obtener el beneficio de invertir en la paralelización de las tareas. Depende de la naturaleza del problema. Una tarea altamente secuencial no obtendrá beneficio si se paraleliza.

El speedup maximo se encuentra acotado por la fraccion de tiempo quen o puede ser paralelizable.

## Ley de Gustafson

> Speedup should be measured by scalling the problem to the number or processors, not by fixing the problem size.

Aumentar el paralelismo puede permitir la modificación del problema original para ejecutar más trabajo. Si el problema crece, caben dos alternativas:

- Parte serial disminuye => speedup aumenta
- Paralelismo aumenta => speedup aumenta

## Work-Span

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

## Estrategias

### Descomposición Funcional

Se separa el resultado en la agregación del resultado de distintas funciones, y las subfunciones se resuelven de forma paralela.

### Particionamiento de Datos

Se separa el resultado en la agregación del resultado de una única función con distintos conjuntos, y cada subconjunto se procesa de forma paralela.

### Patrones de Procesamiento

Los patrones de procesamiento son basados en algoritmos, no son tan abstractos como patrones de diseño. No incluyen detalles de implementación y son agnósticos al lenguaje. Algunos ejemplos son:

- Fork-Join
- Pack
- Pipeline
- Map-Reduce
