Hay distintas formas de coordinar actividades:

- Coordinación: Cada nodo hace un trabajo distinto, y luego otro nodo unifica la información
- Replicación: Cada nodo hace el mismo trabajo, y luego se llega a un consenso. Esto agrega redundancia
- Acceso a recursos compartidos: Hay un nodo que se encarga de serializar el acceso a un recurso

## MPI

Es un estándar basado en transmisión y recepción de mensajes. Implementa un middleware de comunicación de grupos.

La ejecución se vuelve transparente a la cantidad de nodos involucrados.

## Flink

Es una plataforma para procesamiento distribuido de datos. Incluye un motor de ejecución de pipelines de transformación. Las consultas se pueden especificar en un formato similar a SQL.

El framework permite define un *dataflow*, que es un [[Direct Acyclic Graph|DAG]] de operaciones sobre un flujo de datos.

Algunos casos de uso comunes son:

- ETL (Extract, Transform and Load)
- Data Pipelines: Tareas de procesamient orecurrentes, basadas en la ocurrencia de eventos.
