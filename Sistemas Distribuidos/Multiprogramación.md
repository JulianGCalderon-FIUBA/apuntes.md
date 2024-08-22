Existen distintas variantes de la multiprogramación:

- Multi-threading: Hilos compartiendo memoria
- Multi-processing: Procesos con memoria independiente
- Multi-computing: Distintas computadoras independientes

## Multi-threading

Hay recursos compartidos (heap, data segment, file descriptors, code segment)

Para sincronizar hilos hay distintas alternativas:

- Soporte de threading del sistema operativo (mutex)
- Soporte de threading del runtime
- Inter Process Communication (IPC)

Algunas características clave de esta variante son:

- Es sencillo compartir información.
- Alto acoplamiento entre los componentes
- Estabilidad escasa, ya que un hilo defectuoso afecta todo el sistema.
- Escalabilidad muy limitada.

## Multi-processing

Hay menos recursos compartidos (code segment)

Para sincronizar procesos, dependeremos de Inter Process Communication (IPC). Algunas opciones son: señales, pipes, memoria compartida, semáforos, colas, locks, sockets.

Algunas características clave de esta variante son:

- No es trivial compartir información entre procesos.
- Los componentes están separados, en general simples.
- Mayor escalabilidad y estabilidad que el multi-threading.
- No hay tolerancia a fallos del hardware o del sistema operativo.
