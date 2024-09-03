## Descomposición Funcional

Se separa el resultado en la agregación del resultado de distintas funciones, y las subfunciones se resuelven de forma paralela.

## Particionamiento de Datos

Se separa el resultado en la agregación del resultado de una única función con distintos conjuntos, y cada subconjunto se procesa de forma paralela.

## Patrones de Procesamiento

Los patrones de procesamiento son basados en algoritmos, no son tan abstractos como patrones de diseño. No incluyen detalles de implementación y son agnósticos al lenguaje. Algunos ejemplos son:

- Fork-Join
- Pack
- Pipeline
- Map-Reduce
