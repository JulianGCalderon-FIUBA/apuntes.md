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

Soporta distintos lenguajes de programación, y distintos runners (como por ejemplo [[#Apache Flink]], o Google Cloud).

El pipeline se define de forma similar a Flink.

## Map Reduce

Es un paradigma desarrollado por Google en 2005. La idea es identificar tareas que pueden ser ejecutados en paralelo, y grupos de datos que puedan ser procesados en paralelo.

Algunas implementaciones de este paradigma son: Apache Hadoop, Amazon EMR, Google MapReduce.

Está inspirado en las funciones `map` y `reduce` de los lenguajes funcionales.

### Arquitectura

En el caso ideal, no existe la dependencia entre los datos. Estos pueden ser partidos en *chunks* del mismo tamaño (por lo general 64 MiB).

Cada proceso pueden trabajar con uno o múltiples chunks, de forma uniforme

El coordinador, o proceso **master**, es el encargado de:

- Dividir los datos en chunks.
- Enviar la ubicación de los chunks a los workers.
- Recibe la ubicación de los resultados de todos los workers.

Los workers, son los encargados de:

- Recibir la ubicación de los chunks del proceso master.
- Procesar los chunks de información.
- Envía la ubicación del resultado del procesamiento al master.

La cantidad de mappers y reducers es especificada por el usuario. En un caso idea, tendríamos un mapper por cada chunk.

 ![[Map Reduce 1737214860.png]]

### Funcionamiento

La lógica de negocio, provista por el usuario, son las funciones `map` y `reduce`.

La función `map` recibe un chunk y devuelve un resultado intermedio como un conjunto de pares clave-valor.

No se puede llamar a la función `reduce` hasta que se hallan procesados todos los datos, por lo que los datos intermedios se guardan en un archivo intermedio (IF). Una vez procesados todos los datos, se le notifica al master la ubicación del archivo master.

El proceso master toma los archivos intermedios y los agrupa por clave. Luego particiona los datos intermedios en regiones, una para cada reducer. Finalmente, el master le envía la ubicación de los archivos intermedios a los reducers.

Cada clave única es procesada por un único reducer, pero un reducer puede procesar más de una clave.

La función `reduce` recibe un conjunto de pares clave-valor. Esta función es llamada por cada clave única, y devuelve el resultado final del procesamiento.
