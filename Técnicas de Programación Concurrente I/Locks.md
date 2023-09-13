Los locks sirven para realizar exclusión mutua entre procesos. Nos permite que los procesos entren a la [[Corrección#Sección Crítica|sección crítica]] uno a la vez.

Se implementan mediante variables del tipo `lock`, que contienen el estado del mismo. Estos tienen dos métodos principales:

- Método `lock()`: El proceso se bloquea hasta obtener el lock.
- Método `unlock()`: El proceso libera el lock que tomó previamente.

Para la implementación, se necesita soporte tanto del *hardware* como del sistema operativo.

## Locks en UNIX

En UNIX, los locks son un mecanismo de sincronización de acceso a un archivo.
