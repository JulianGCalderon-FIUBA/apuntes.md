Basan su funcionamiento en el concepto de comunicar mensajes entre aplicación. La comunicación de grupo es transparente a las aplicaciones que la requieren.

Resuelve problemas de transparencia respectos a ubicaciones, fallos, escalabilidad.

Algunos ejemplos son:

- RabbitMQ
- Kafka
- ZeroMQ

## Modos de Operación

Tiene dos modos de operación:

- **Bus de información**: Pueden enviarse mensajes bajo ciertos tópicos, para que aquellos interesados lo reciban. Los mensajes se pierden si nadie los toma.
- **Cola de mensajes**: Pueden enviarse mensajes con un destinatario definido. Se quedan esperando hasta que este lo reciba. En general, no se garantiza orden de recepción.

## Sincronismo y Asincronismo

El middleware puede ser sincrónico o asincrónico:

En el caso sincronico, se modela una conexión punto a punto. Permite obtener respuestas instantáneas.

No permite implementar transparencia frente a errores.

En el caso asincronico se implementa utilizando colas. La arquitectura soporta periodos de discontinuidad del transporte.

  Se deben configurar alertas para cuando se llenan las colas, ya que tienen un tamaño límite. No existe la cola infinita.

  Si se quiere recibir respuesta a los pedidos, es necesario tener dos colas (una por cada cliente de la comunicación)

## Colas

## Broker

El broker es un nodo central que provee transparencia de localización entre los emisores y los receptores.

Algunas caracteristicas de la utilización de un broker:

- Soportar lógica para filtrado y modificación de mensajes.
- Brinda un punto de control y monitoreo.
- Ofrecer persistencia del mensaje en caso de que no haya nadie para recibirlo aún.
