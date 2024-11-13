## Pipeline

Los datos de entrada forman un flujo donde distintos filtros o procesadores se conectan entre sí para procesarlos de manera secuencial.

Es utilizado bastante en los sistemas operativos de tipo Unix.

Admite dos modos de procesamiento:

- Worker por **filtro**: Se asigna una unidad de procesamiento a cada etapa del pipeline.
- Worker por **ítem**: Se asigna una unidad de procesamiento a cada ítem. El worker toma este ítem y lo acompaña a lo largo de todo el procesamiento, aplicando cada filtro.

Cada procesador funciona como una etapa, pudiendo ser:

- **Paralela**: Cada ítem a procesar es independiente de anteriores.
- **Secuencial**: No se puede procesar de forma paralela debido a la dependencia entre los ítems.