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

Rust provee locks compartidos y locks exclusivos en el tipo de dato `RwLock`. No se provee una política específica, sino que es dependiente del sistema operativo. Se requiere que el tipo de dato compartido implemente los *trait markers* `Send` y `Sync`.

El método `read` obtendrá un lock de acceso compartido, mientras que el método `write` obtendrá un lock de acceso exclusivo. El método `try_write` trata de obtener el lock, pero no bloquea el hilo de ejecución. Únicamente devuelve éxito o error, dependiendo del caso.

Ambos métodos devolverán una *guarda* al elemento compartido. Esto quiere decir que el *unlock* se ejecuta automáticamente cuando la variable se va del *scope*.

### Traits

Un *trait marker* es aquel que no provee ningún método al implementarlo. Sirven como simples marcadores.

El *trait marker* `Send` indica que el *ownership* del tipo que lo implementa puede ser transferido entre hilos. Casi todos los tipos de datos de Rust lo implementan.

Los tipos de datos compuestos que están formados por tipos que implementan `Send`, implementan automáticamente `Send`.

El *trait marker* `Sync` indica que es seguro que el tipo de dato sea referenciado desde múltiples hilos. Esto es: si `T` implementa `Sync`, entonces `&T` implementa `Send`.

Los tipos primitivos implementa `Sync`, y los tipos compuestos que están formados por tipos de datos que implementan `Sync`, implementan automáticamente `Sync`.

### Locks Envenenados

Un lock se encuentra envenenado cuando un hilo que lo toma de forma exclusiva realiza ejecuta `panic!`.

Las posteriores llamadas a `read()`, y `write()` sobre el mismo *lock* devolverán un error.
