El modelo de transacciones está conformado por un conjunto de procesos independientes; cada uno puede fallar aleatoriamente.

Los errores en la comunicación son manejados transparentemente por la capa de la comunicación.

## Almacenamiento

Existen tres tipos de almacenamiento. La memoria RAM se borra cuando se apaga el sistema. El almacenamiento en disco persiste, pero puede perderse cuando este *crashea*.

El almacenamiento estable se implementa con múltiples discos, sincronizando la información entre ambos.

Si ocurre un error durante una escritura, se puede comparar los contenidos con otro de los discos. La probabilidad de perder los datos es extremadamente pequeña.

## Primitivas

Tendremos cinco primitivas:

- `BEGIN TRANSACTION`: Marca el inicio de la transacción,
- `END TRANSACTION`: Finaliza la transacción y trata de hacer *commit*.
- `ABORT TRANSACTION`: Finaliza forzadamente la transacción, y restaura los valores anteriores.
- `READ`: Lee datos de una archivo u otro objeto.
- `WRITE`: Escribe datos a un archivo u otro objeto.

## Propiedades ACID

Tendremos cuatro propiedades importantes que buscaremos respetar:

- **Atómicas:** La transacción no puede ser dividida
- **Consistentes:** La transacción cumple con todos los invariantes del sistema
- **Aisladas:** Las transacciones concurrentes no interfieren con ellas mismas
- **Durables:** Una vez que se *commitean* los cambios, son permanentes.

## Private Workspace

También conocida como *snapshot isolation*. Al iniciar una transacción, el proceso recibe una copia de todos los archivos a los cuales tiene acceso.

Hasta que hace commit, el proceso trabaja con la copia. Al hacer commit, se persisten los cambios.

Una primera optimización consiste en que si una transacción debe únicamente leer un archivo. No es necesario que lo copie (a menos que haya sido cambiado desde que comenzó la transacción).

Una segunda optimización consiste en clonar únicamente los índices de los archivos. Estos apuntarán a donde efectivamente esté guardado el archivo. Cuando se modifican, se crea un nuevo bloque y se escribe la actualización allí, actualizando los índices. Si una transacción tiene los índices viejos, no verá las actualizaciones.

## Writeahead Log

Los archivos se modifican *in-place*, pero se mantiene una lista de los cambios aplicados. Antes de commitear la transacción, se escribe un registro commit en el log.

Si la transacción se aborta, se lee el log de atrás hacia adelante para deshacer los cambios (rollback).

Si otra transacción dependía de un cambio realizado por una transacción que está abortando, esa transacción también se debe deshacer.

## Commit de dos Fases

El coordinador es aquel proceso que ejecuta la transacción, y quiere sincronizar un *commit* entre múltiples procesos participantes.

1. En la primera fase, el coordinador escribe *prepare* en su log y envía el mensaje *prepare* al esto de procesos. Los procesos que recibe el mensaje escriben *ready* en el log y envían *ready* al coordinador.
2. En la segunda fase, el coordinador hace los cambios y envía el mensaje *commit* al resto de los procesos. Los procesos que reciben el mensaje escriben *commit* en el log y envían *finished* al coordinador.
3. Si alguno no le responde, entonces el coordinador escribe un mensaje de *abort* y se lo envía al resto de procesos.

## Lock de dos Fases

Existen dos fases:

- Fase de expansión: Se toman todos los locks usar.
- Fase de contracción: Se liberan todos los locks. No se puede tomar un lock después de liberar otro.

Esto garantiza la propiedad de serializabilidad para las transacciones, pero pueden ocurrir deadlocks. Una forma de prevenirlos puede ser utilizar un órden canónico para tomarlos.

En el **strict two-phase locking**, la contracción ocurre después del commit. Esto asegura la recuperabilidad de las transacciones (sin rollbacks en cascada).

## Concurrencia Optimista

El proceso modifica los archivos sin ningún control, esperando que no haya conflictos. Al *commitear*, se verifica si el resto de las transacciones modificó los mismos archivos. Si es así, se aborta la transacción.

Este modelo es libre de deadlocks y favorece el paralelismo, pero rehacer todo puede ser costoso en condiciones de alta carga.

## Timestamps

Existen *timestamps* únicos globales para garantizar orden. Cada archivo tiene:

- Un *timestamp* de lectura
- Un *timestamp* de escritura
- Qué transacción hizo la misma operación

Cada transacción al iniciarse recibe un timestamp, se compara el timestamp de la transacción con los timestamps del archivo:

- Si es mayor, la transacción está en orden y se procede con la operación.
- Si es menor, la transacción se aborta.

Al commitear, se actualizan los timestamps del archivo.
