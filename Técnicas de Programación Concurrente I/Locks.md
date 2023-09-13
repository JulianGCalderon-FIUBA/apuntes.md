Los locks sirven para realizar exclusión mutua entre procesos. Nos permite que los procesos entren a la [[Corrección#Sección Crítica|sección crítica]] uno a la vez.

Se implementan mediante variables del tipo `lock`, que contienen el estado del mismo. Estos tienen dos métodos principales:

- Método `lock()`: El proceso se bloquea hasta obtener el lock.
- Método `unlock()`: El proceso libera el lock que tomó previamente.

Para la implementación, se necesita soporte tanto del *hardware* como del sistema operativo.

## Locks en UNIX

En UNIX, los locks son un mecanismo de sincronización de acceso a un archivo. También se pueden utilizar para sincronizar el acceso a cualquier otro recurso.

Son *advisory*, esto quiere decir que los procesos pueden ignorarlos.

Existen dos tipos de locks:

- **Shared locks:** Son locks de lectura. Más de un proceso puede tener el lock. Para tomar este tipo de lock, el proceso debe esperar hasta que sean liberados todos los *exclusive locks*.
- **Exclusive locks:** Son locks de escritura. Solo un proceso a la vez puede tener el lock. Para tomar este tipo de lock, el proceso debe esperar hasta que sean liberados todos los locks.

### Utilización

Para aplicar un lock a partir de un archivo abierto, tenemos tres opciones:

- Mediante `fcntl()`: A partir de una estructura `flock`, podemos definir la región del archivo en la cual establecer el lock.
- Mediante `flock()`.
- Mediante `lockf()`: Es una interfaz que utiliza por debajo a `fcntl()`, pero con uso más simple, sin capacidad de especificar la región.

## Locks en Rust

