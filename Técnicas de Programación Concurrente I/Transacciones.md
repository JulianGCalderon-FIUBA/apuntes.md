El modelo de transacciones está conformado por un conjunto de procesos independientes; cada uno puede fallar aleatoriamente.

Los errores en la comunicación son manejados transparentemente por la capa de la comunicación.

El almacenamiento es estable, se implementa con discos, y la probabilidad de perder los datos es extremadamente pequeña.

## Primitivas

Tendremos cinco primitivas:

- `BEGIN TRANSACTION`: Marca el inicio de la transacción
- `END TRANSACTION`: Finaliza la transacción y trata de hacer *commit*
- `ABORT TRANSACTION`: Finaliza forzadamente la transacción, y restaura los valores anteriores.
- `READ`: Lee datos de una archivo u otro objeto
- `WRITE`: Escribe datos a un archivo u otro objeto.

##