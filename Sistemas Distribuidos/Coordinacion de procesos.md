Hay distintas razones por las cuales se busca coordinar actividades:

- Distribución: donde cada nodo hace un trabajo distinto, y luego otro nodo unifica la información
- Replicación: donde cada nodo hace el mismo trabajo, y luego se llega a un consenso. Esto agrega redundancia
- Acceso a recursos compartidos: donde múltiples nodos acceden a un recurso compartido, y se necesita coordinar su acceso.

## MPI

Es un estándar basado en transmisión y recepción de mensajes. Implementa un middleware de comunicación de grupos.

La ejecución se vuelve transparente a la cantidad de nodos involucrados.

## Apache Flink

Es una plataforma para procesamiento distribuido de datos. Incluye un motor de ejecución de pipelines de transformación. Las consultas se pueden especificar en un formato similar a SQL.

El framework permite define un *dataflow*, que es un [[Direct Acyclic Graph|DAG]] de operaciones sobre un flujo de datos.

Algunos casos de uso comunes son:

- **ETL**: *extract, transform and load*
- **Data Pipelines**: Tareas de procesamiento recurrentes, basadas en la ocurrencia de eventos.

Se pueden utilizar múltiples pipelines de Flink que procesan distintos datos y colaboran entre sí.

## Beam

Es un modelo de definición de pipelines de procesamiento de datos con portabilidad de lenguajes y motorse de ejecución.

Soporta distintos lenguajes de programación, y distintos runners (como por ejemplo [[#Apache Flink]]).

El pipeline se define de forma similar a Flink.
