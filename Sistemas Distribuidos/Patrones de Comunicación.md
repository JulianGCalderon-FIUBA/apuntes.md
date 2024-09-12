## Request-Reply

Un nodo envía un mensaje, y el otro nodo responde con otro mensaje. Es sincrónico.

Podría ser asincrónico. Requeriría de 2 ciclos de request-reply. En el primero se hace un pedido. En el segundo se pide la respuesta del pedido.

Ante la perdida del reply, tenemos 3 estrategias principales:

- **Sin control**: No tenemos certeza de si el mensaje se envió.
- **Reejecución**: Volvemos a enviar el mensaje, pero podría haber reejecución.
- **Retransmisión**: Implementamos un filtro de duplicados (con un ID, por ejemplo). Aseguramos que no hay reejecución.

Para el reintento, se puede utilizar exponential backoff con jitter para evitar saturar el servidor y agrupamiento de clientes.

## Producer-Consumer

Existen 2 tipos de nodos:

- **Producers**: Generan información
- **Consumers**: Consumen información para realizar algún tipo de procesamiento.

Se usa para el procesamiento de tareas.

## Publisher-Subscriber

Basado en eventos.

Existen 2 tipos de nodos:

- Publishers: Emisores de eventos. Tienen la posibilidad de generar algún elemento de interés.
- Subscribers: Son los receptores. Esperan la aparición de algún evento de su propio interés sobre el cual efectuaran alguna acción.

Hay dos posibles arquitecturas:

- Basada en tópicos: Publicación y subscripción indicando el tipo de evento.
- Basada en canales: Publicaciones y suscripciones orientadas a canales específicos.

## Pipelines

Los datos de entrada forman un flujo donde distintos filtros o procesadores se conectan entre sí para procesarlos de manera secuencial.
