Es similar al patrón de [[Pipeline]], pero ya no es lineal.

![[Direct Acyclic Graph 1731464176.png|350]]

En el gráfico, los nodos indican tareas, y las aristas flujo de información. La forma del grafo nos forma las dependencias entre las tareas.

Esto tiene las siguientes ventajas

- Es la representación natural de flujos de datos.
- La carga de procesamiento se puede paralelizar.
- Nos indica en qué momento la información se puede reutilizar.
- Admite procesar solo nodos requeridos por dependencias (lazy loading).

Se pueden utilizar para calcular dependencias entre procesos. Si se encuentra un ciclo, entonces existe la posibilidad de un deadlock.
