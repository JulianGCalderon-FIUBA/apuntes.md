Un nodo envía un mensaje, y el otro nodo responde con otro mensaje. Es sincrónico.

Podría ser asincrónico. Requeriría de 2 ciclos de request-reply. En el primero se hace un pedido. En el segundo se pide la respuesta del pedido.

## Tolerancia a Fallos

Ante la perdida del reply, tenemos 3 estrategias principales:

- **Sin control**: No tenemos certeza de si el mensaje se envió.
- **Reejecución**: Volvemos a enviar el mensaje, pero podría haber reejecución.
- **Retransmisión**: Implementamos un filtro de duplicados (con un ID, por ejemplo). Aseguramos que no hay reejecución.

Para el reintento, se puede utilizar exponential backoff con jitter para evitar saturar el servidor y agrupamiento de clientes.
