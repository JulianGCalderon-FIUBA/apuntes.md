## DAG

Similar al patrón de pipelines, pero ya no es lineal.

Los nodos indican tareas, y las aristas flujo de información.

Permite calcular trabajo total para una tarea (camino crítico)

Algunas ventajas del modelo:

- Es la representación natural de flujos de datos.
- La carga de procesamiento se puede paralelizar.
- Admite procesar solo nodos requeridos por dependencias.

Se pueden para calcular dependencias entre procesos. Si se encuentra un ciclo, entonces existe la posibilidad de un deadlock.
