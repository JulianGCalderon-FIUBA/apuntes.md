---
title: Archivos y Directorios
---

En este capítulo, trataremos una pieza crítica para la virtualización de la computadora: **almacenamiento persistente.** Para eso, utilizaremos discos que almacenan información de forma permanente (o al menos, durante un largo tiempo).

Necesitamos dos abstracciones claves para la virtualización del almacenamiento. El primero es un **archivo**, un archivo es simplemente un vector lineal de bytes. Todos los archivos tienen un nombre de bajo nivel, usualmente un número, que utilizaremos para referirnos a él. Solemos referirnos a este nombre como el **inodo**

La segunda abstracción necesaria es la de un **directorio**. Un directorio también tiene un **inodo**, pero sus contenidos son específicos. Contiene una lista de pares *user-level-name, low-level-name.* La jerarquía de directorias comienza en el directorio raíz `/.`

Los nombres de los archivos se separan en dos partes, separadas por un punto: `name.extension`. La primera parte es el nombre, a nivel de usuario, del archivo. La segunda parte es la extensión, le indica a los usuarios de que forma interpretar el archivo.

## Interfaz del Sistema de Archivos

Para interactuar con el sistema de archivos, el kernel provee una serie de abstracciones que permiten interactuar con el disco. Por dentro, estas *syscalls* son *wrappers* de las implementaciones de cada sistema de archivos particular.

### Creación de Archivos

Para crear archivos, utilizaremos la *syscall* `open()` con el flag `O_CREAT`. Esta función se usa para abrir un archivo, pero con los flags correctos puede abrir un archivo con las configuraciones necesarias. El flag `O_WRONLY` indica que el archivo se abre para la escritura, y el flag `O_TRUNC` indica que si el archivo existía previamente, entonces debe borrar sus contenidos.

Esta *syscall* devuelve un **file descriptor**. Este es un entero, único y privado para el proceso, mediante el cual puede interactuar con el archivo. Se puede pensar como un puntero a un archivo. Se utiliza un vector estático para llevar cuenta de los archivos abiertos por cada proceso.

### Lectura y Escritura

Para leer un archivo, utilizaremos la *syscall* `open()` con los flags `O_RDONLY` o `O_WRONLY`. Una vez abierto, podemos leer del archivo utilizando la *syscall* `read()` o escribir con `write()`.

Una vez finalizada la operación deseada con el archivo, es necesario cerrarlo con `close()`.

El sistema operativo contiene una tabla de archivos abiertos: *ftable*, donde se guardan todos los archivos abiertos por el sistema.

#### Escritura Instantánea

Cuando llamamos a `write()`, entonces estos datos se guardan en un *buffer* y son escritos en el futuro, por razones de rendimiento. Si queremos escribir de forma instante, utilizaremos la *syscall* `fsync()`.

#### Secuencialidad

Muchas veces queremos operar con un archivo, pero no de forma secuencial. Para eso, utilizaremos la *syscall* `lseek()`. Utilizaremos un *offset* que nos permitirá leer de una dirección particular. El parámetro *whence* nos permite determinar cómo se va a realizar este *seek*.

- **SEEK_SET:** Nos permite movernos al offset indicado.
- **SEEK_CUR:** Nos permite movernos desde la posición actual del archivo.
- **SEEK_END:** Nos permite movernos desde la posición final del archivo.

### Archivos Compartidos

Cuando se realiza un `fork()` con un archivo abierto, entonces no se genera una nueva entrada en la tabla de archivos. Cuando un proceso modifica el *offset*, este se modifica en los otros procesos.

Para cerrar este archivo, todos los procesos que contienen la referencia a este archivo deben cerrarlo. Se utilizan **referencias contables.**

Otra forma de hacerlo, es utilizando la *syscall* `dup()`, este clona un *file descriptor,* pero la referencia es la misma.

### Renombramiento de Archivos

Para renombrar un archivo (o también moverlo de directorio), utilizaremos la *syscall* `rename()`. Esta operación suele realizarse de forma atómica, para evitar problemas de concurrencia.

### Acceso a Metadata

La *syscall* `stat()` se utiliza para acceder a la metadata de un archivo. Esta tiene información sobre su inodo, tamaño, los permisos, e información sobre cuando un archivo fue accedido o modificado, entre otras cosas.

## Operaciones con Directorios

### Creación de Directorios

Como no se puede escribir o leer un directorio de la forma convencional, se provee una interfaz distinta para interactuar con estos. Para crearlo, se utiliza la ***syscall*** `mkdir()`

Todos los directorios siempre se crean con dos entradas iniciales:

- `.` Refiere al propio directorio.
- `..` Refiere al directorio padre.

### Lectura de Directorios

En lugar de abrirlos como un archivo regularmente, utilizaremos la *syscall* `opendir()`. Una vez abierto, utilizaremos `readdir()` para leer secuencialmente cada entrada del directorio.

### Borrar Directorios

Podemos borrar directorios utilizando la *syscall* `rmdir()`, aunque para que funcione, el directorio tiene que estar vacío.

## Links

### Hard Links

La *syscall* `link()` se utiliza para crear una nueva forma de referirse a un mismo archivo. Se crea una nueva entrada en el directorio que refiere al mismo *inode number*. No se pueden generar *hard links* a directorios, para evitar referencias circulares.

Cuando creamos un archivo, estamos haciendo dos cosas. En primer lugar, creamos una estructura inodo para tener información del archivo, luego estamos *linkeando* este inodo a un archivo legible por un usuario.

La operación inversa se conoce como `unlink()`, que elimina una referencia a una archivo. Cuando esta es la última referencia a un archivo, entonces este es eliminado. Para esto, utilizamos referencias contables, los archivos que están *linkeados* a un inodo particular.

### Symbolic Links

Hay otro tipo de *link* que se conoce como *symbolic link* o *soft link.* Este tipo de links es un archivo en sí mismo, que tiene referencia al *hardlink* del cual se generó. Si se elimina el archivo original, entonces se generan *dangling references.*

## Permisos sobre Archivos

### Bits de Permisos

Los archivos son compartidos entre todos los procesos del sistema, por lo que debe existir una forma de proteger el disco. Para hacer esto, todos los archivos tienen *permission bits,* que guardan información sobre lo que se puede hacer con los archivos. Por lo general, existe algún tipo de *superuser* o *root* que puede acceder a todos los archivos, sin importar sus privilegios.

Los permisos se asignan según tres grupos, cada uno con privilegios distintos sobre el archivo.

- **Owner:** Indica los permisos que tiene el dueño del archivo sobre el mismo
- **Group:** Indica los permisos que tienen los que pertenecen a un grupo.
- **Other:** Indica los permisos que tiene cualquier sobre el archivo.

Los permisos, a su vez, se separan en tres. La lectura se denota con el carácter 'r', La lectura se denota con el carácter 'r', La lectura se denota con el carácter 'r'. El dueño de un archivo puede cambiar los permisos del mismo (`chdmod`).

Para el caso de directorios, el bit de ejecución indica que puede moverse a ese directorio, utilizando `cd`. Junto con el bit de escritura, se podrían agregar archivos al directorio.

### Access Control List

Algunos sistemas de archivos incluyen un control más sofisticado sobre los archivos. Estas listas son una forma más general y poderosa de representar quién puede acceder a cada recurso. Se puede crear una lista de quienes tienen permisos sobre un archivo.

## Creación y Montaje

Para crear un sistema de archivos, la mayoría de sistemas proveen una herramienta **MKFS** *(make filesystem)* que permite esto.

Una vez un sistema de archivos es creado, este debe ser montado para acceder a sus contenidos. Para hacer esto, utilizamos la *syscall* `mount()`. Esta rutina copia el sistema de archivos al punto de montado. Para poder ser accedidos desde el sistema de archivos padre.

El montaje permite unificar muchos sistemas de archivos bajo un mismo árbol, permitiendo sistemas de archivos anidados. El usuario puede interactuar con estos archivos independientemente de su sistema, utilizando las *syscalls* del kernel.
