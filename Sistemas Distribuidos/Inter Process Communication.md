---
aliases:
  - IPC
---

Existen distintos mecanismos para la comunicación entre procesos. Son provistos por el sistema operativo y su creación y destrucción exceden la vida del proceso. Suelen ser identificados por un nombre.

- Signals: Hay distintos tipos de señales, cada proceso decide como manejarlas.
- Shared Memory: Su tamaño se define al ser creada. No existe esta abstracción entre threads, ya que se puede utilizar el heap.
- File locks: Se puede solicitar un lock exclusivo o compartido a un archivo.
- Pipes y FIFOs: Son pasajes de comunicación directa entre procesos.
	- Pipes: Comunicación entre procesos padre e hijo. Mueren al finalizar el proceso.
	- FIFOs: Comunicación entre procesos cualesquiera. Exceden la vida del proceso.
- Message queues: Los procesos escriben y reciben bloques de bytes. Existe un campo `mtype` que identifica el tipo de mensaje.
- Sockets: Permite comunicar procesos a traves de un canal de comunicacion (endpoint).
