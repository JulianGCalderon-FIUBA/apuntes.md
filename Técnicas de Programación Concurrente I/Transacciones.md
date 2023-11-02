El modelo de transacciones está conformado por un conjunto de procesos independientes; cada uno puede fallar aleatoriamente.

Los errores en la comunicación son manejados transparentemente por la capa de la comunicación.

El almacenamiento es estable, se implementa con discos, y la probabilidad de perder los datos es extremadamente pequeña.

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

## Private Worskpace

También conocida como *snapshot isolation*. Al iniciar una transacción, el proceso recibe una copa de todos los archivos a los cuales tiene acceso.

Hasta que hace commit, el proceso trabaja  con la copia. Al hacer commit, se persisten los cambios.

Salvo por algunas optimizaciones, este algoritmo es extremadamente costoso.

## Writeahead Log

Los archivos se modifican *in-place*, pero se mantiene una lista de los cambios aplicados. Antes de commitear la transacción, se escribe un registro commit en el log.

Si la transacción se aborta, se lee el log de atrás hacia adelante para deshacer los cambios (rollback).

## Commit 