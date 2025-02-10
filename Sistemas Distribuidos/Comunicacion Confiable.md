Una comunicación es confiable, o *reliable*, si se garantiza integridad, validez, y atomicidad en la entrega de mensajes.

En una comunicación de uno a uno, es trivial si contamos con protocolos como TCP y una red segura.

En una comunicación de uno a muchos, la atomicidad requiere atención especial. Además, debemos definir el [[Orden de Mensajes]] que garantizamos.

## Atomicidad

Si los mensajes deben entregarse a múltiples procesos de forma atómica, entonces surge la necesidad de tener ACK, y demorar la entrega de los mensajes.

No es lo mismo la recepción de un mensaje (a nivel de capa de transporte), a la entrega del mensaje a la capa de aplicación. La capa de transporte puede demorar o eliminar un mensaje que ya recibió, sin entregarlo a la capa de aplicación.

## Perdida de Mensajes

Ante la perdida de un mensaje, tenemos 3 estrategias principales:

- **Sin control**: No tenemos certeza de si el mensaje se envió.
- **Reejecución**: Volvemos a enviar el mensaje, pero podría haber reejecución.
- **Retransmisión**: Implementamos un filtro de duplicados (con un ID, por ejemplo). Aseguramos que no hay reejecución.

Para el reintento, se puede utilizar *exponential backoff* con *jitter* para evitar saturar el servidor y agrupamiento de clientes.
