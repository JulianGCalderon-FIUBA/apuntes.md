Es una plataforma para procesamiento distribuido de datos. Incluye un motor de ejecución de pipelines de transformación.

Ofrece distintos niveles de abstracción para desarrollar las aplicaciones:

- SQL: Lenguaje de alto nivel para especificar consultas
- Table API: Es un DSL declarativo para especificar consultas
- DataStream: Es la interfaz principal, y o

El framework permite definir un *dataflow*, que es un [[Direct Acyclic Graph|DAG]] de operaciones sobre un flujo de datos.

Algunos casos de uso comunes son:

- **ETL**: *extract, transform and load*
- **Data Pipelines**: Tareas de procesamiento recurrentes, basadas en la ocurrencia de eventos.

Se pueden utilizar múltiples pipelines de Flink que procesan distintos datos y colaboran entre sí.
