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

Para sincronizar procesos, dependeremos nuevamente de soporte del sistema operativo, como por ejemplo, con IPC.

Al ser procesos distintos, compartir información no es tan trivial, aunque esto ofrece menor acoplamiento entre los procesos.

Hay mayor escalabilidad y estabilidad, aunque sique limitado por las capacidades de la computadora.

## Multi-computing

Los distintos programas se ejecutan en computadoras distintas, totalmente independientes. Esta categoría se acerca más a la idea de un [[Sistema Distribuido]]

Al ser computadoras distintas, no hay recursos compartidos.

Para sincronizarse, dependen mensajes enviados entre computadoras. Además, no poseen un [[Relojes|reloj]] central que permita sincronizarlas fácilmente.

Este sistema es altamente escalable y estable, ya que una falla en una computadora no afecta a las otras.
