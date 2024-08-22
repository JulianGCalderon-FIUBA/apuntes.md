---
aliases:
  - IPC
---

Existen distintos mecanismos para la comunicación entre procesos. Son provistos por el sistema operativo y su creación y destrucción exceden la vida del proceso. Suelen ser identificados por un nombre.

- Signals: Hay distintos tipos de señales, cada proceso decide como manejarlas.
- Shared Memory: Su tamaño se define al ser creada. No existe esta abstracción entre threads, ya que se puede utilizar el heap.
- File locks: Se puede solicitar un lock exclusivo o compartido a un archivo.
- Pipes y FIFOs: Es 
