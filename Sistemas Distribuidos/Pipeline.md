Esta arquitectura también se conoce como "pipes and filters". Es utilizado bastante en los sistemas operativos de tipo Unix

```bash
cat in | grep pattern | sort | uniq > out
```

Los datos de entrada forman un flujo donde distintos filtros o procesadores se conectan entre sí para procesarlos de manera secuencial.

Esta arquitectura puede iniciar el procesamiento antes de que estén todos los datos, lo que permite trabajar con flujos infinitos de información, en modo de _stream_.

![[Pipeline 1739233025.png]]

Este patrón es útil para algoritmo online, donde se puede comenzar a procesar la tarea antes de terminar de recibir los datos, y situaciones donde los datos son un flujo infinito.

## Modelos de Procesamiento

Admite dos modos de procesamiento:

- Worker por **filtro**: Se asigna una unidad de procesamiento a cada etapa del pipeline.
- Worker por **ítem**: Se asigna una unidad de procesamiento a cada ítem. El worker toma este ítem y lo acompaña a lo largo de todo el procesamiento, aplicando cada filtro.

La arquitectura puede tener una combinación de ambos modos de procesamiento.

## Etapas secuenciales y paralelas

Cada procesador funciona como una etapa, pudiendo ser:

- **Paralela**: Cada ítem a procesar es independiente de anteriores.
- **Secuencial**: No se puede procesar de forma paralela debido a la dependencia entre los ítems.
