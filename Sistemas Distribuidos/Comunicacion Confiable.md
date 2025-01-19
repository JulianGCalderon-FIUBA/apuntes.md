Una comunicación es confiable, o *reliable*, si se garantiza integridad, validez, y atomicidad en la entrega de mensajes.

En una comunicación de uno a uno, es trivial si contamos con protocolos como TCP y una red segura.

En una comunicación de uno a muchos, la atomicidad requiere atención especial. Ademas, debemos definir el [[Orden de Mensajes]] que garantizamos.

## Atomicidad

Si los mensajes deben entregarse a múltiples procesos de forma atómica, entonces surge la necesidad de tener ACK, y demorar la entrega de los mensajes.
