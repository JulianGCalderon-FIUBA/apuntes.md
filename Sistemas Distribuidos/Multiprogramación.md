En la multiprogramación, más de un programa está activo al mismo tiempo. Hay más de una unidad de procesamiento *logica*.

Existen distintas variantes de la multiprogramación:

- Multi-threading: Hilos compartiendo memoria
- Multi-processing: Procesos con memoria independiente
- Multi-computing: Distintas computadoras independientes.

## Multi-threading

Los distintos programas se ejecutan concurrentemente en distintos hilos del sistema operativo.

Esto implica que **hay** recursos compartidos (heap, data segment, file descriptors, code segment)

Para sincronizar hilos, se necesita soporte del sistema operativo, como por ejemplo, utilizando un *mutex* o IPC (*inter process communication*). En el caso de que sean hilos ligeros, se puede resolver con soporte del *runtime* del lenguaje.

Al pertenecer al mismo proceso, es más sencillo compartir información, pero los componentes están muy acoplados.

La escalabilidad es muy limitada, ya que está limitada por las capacidades de la computadora. Además, hay poca estabilidad, ya que hay un único punto de falla.

## Multi-processing

Los distintos programas se ejecutan concurrentemente en distintos procesos del sistema operativo.

Esto implica que hay menos recursos compartidos (code segment).

Para sincronizar procesos, dependeremos nuevamente de soporte del sistema operativo, como por ejemplo, con IPC (señales, memoria compartida, sockets, pipes, fifos, semaforos, colas, locks).

Al ser procesos distintos, compartir información no es tan trivial, aunque esto ofrece menor acoplamiento entre los procesos.

Hay mayor escalabilidad y estabilidad, aunque sique limitado por las capacidades de la computadora.

### Múltiples Procesadores

El sistema puede contar con una única CPU (el caso más común), o con múltiples CPU, que se comunican a través de un bus para acceder a recursos compartidos. Esto puede generar complicaciones.

![[Multiprogramación 1739230468.png]]

Los diseños de memoria pueden ser simétricos o asimétricos:

- UMA (Uniform Memory Access): El tiempo de acceso a la memoria es igual para todos los procesadores, y el ancho de banda es compartido. Es un sistema con performance balanceada para el uso general.
- NUMA (Non-Uniform Memory Access): Cada procesador tiene memoria local, para la cual tiene mayor ancho de banda. Recientemente se empezó a ofrecer en *cloud*.

![[Multiprogramación 1739230968.png]]

### Taxonomía de Flynn

Es una clasificación de sistemas de acuerdo a la cardinalidad del flujo de instrucciones y flujo de datos:

- **SISD - Single Instruction Single Data**: Es el modelo estándar de procesamiento.
- **SIMD - Single Instruction Multiple Data**: Los procesadores modernos suelen tener soporte para esto, y permite realizar múltiples operaciones a la vez.
- **MISD - Multiple Instruction Single Data:** Ofrecen redundancia cuando no se confía que los procesadores funcionen correctamente. No es una arquitectura común.
- **MIMD - Multiple Instruction Multiple Data**: Requiere sincronizar y coordinador el acceso a la memoria, y no es necesariamente uniforme, ya que existen modelos asimétricos que benefician la afinidad. Se puede implementar con un modelo *multiprocessor*, con memoria y clock compartidos, o con un modelo *multicomputing*.

## Multi-computing

Los distintos programas se ejecutan en computadoras distintas, totalmente independientes. Esta categoría se acerca más a la idea de un [[Sistema Distribuido]]

Al ser computadoras distintas, no hay recursos compartidos.

Para sincronizarse, dependen mensajes enviados entre computadoras. Además, no poseen un [[Relojes|reloj]] central que permita sincronizarlas fácilmente.

Este sistema es altamente escalable y estable, ya que una falla en una computadora no afecta a las otras.
