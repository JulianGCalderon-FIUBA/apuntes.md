---
aliases:
  - MOM
---

Basan su funcionamiento en el concepto de comunicar mensajes entre aplicación. La comunicación de grupo es transparente a las aplicaciones que la requieren.

Resuelve problemas de transparencia respectos a ubicaciones, fallos, escalabilidad.

Se le puede agregar lógica de negocio para resolver problemas específicos, o se pueden utilizar soluciones generales.

Algunos ejemplos son:

- RabbitMQ
- Kafka
- ZeroMQ

## Modos de Operación

Tiene dos modos de operación:

- **Bus de información**: Pueden enviarse mensajes bajo ciertos tópicos, para que aquellos interesados lo reciban. Los mensajes se pierden si nadie los toma.
- **Cola de mensajes**: Pueden enviarse mensajes con un destinatario definido. Se quedan esperando hasta que este lo reciba. En general, no se garantiza orden de recepción.

![[Message Oriented Middleware 1739232501.png]]

## Sincronismo y Asincronismo

El middleware puede ser sincrónico o asincrónico:

En el caso **sincrónico**, se modela una conexión punto a punto. Permite obtener respuestas instantáneas. No permite implementar transparencia frente a errores.

En el caso **asincrónico** se implementa utilizando colas. La arquitectura soporta periodos de discontinuidad del transporte. Si se quiere recibir respuesta a los pedidos, es necesario tener dos colas (una por cada cliente de la comunicación)

## Colas

Pueden existir varias colas definidas dentro del middleware, y estas tienen un nombre. También pueden existir colas anónimas privadas.

Se deben configurar alertas para cuando se llenan las colas, ya que tienen un tamaño límite. No existe la cola infinita.

Gracias a las colas, se le da garantía al emisor de que el mensaje es insertado.

## Broker

El broker es un nodo central que provee transparencia de localización entre los emisores y los receptores.

Algunas características de la utilización de un broker:

- Soportar lógica para filtrado y modificación de mensajes.
- Brinda un punto de control y monitoreo.
- Ofrecer persistencia del mensaje en caso de que no haya nadie para recibirlo aún.

## Diferencia con TCP

A diferencia de TCP, que es un protocolo simple, *stream oriented*, y para comunicación uno a uno, un MOM ofrece las siguientes características:

- Comunicación uno a muchos, o muchos a muchos.
- Monitoreo.
- Persistencia.
- Replicación.
- Confirmaciones de mensajes semánticos, no solo de segmentos de TCP (por ejemplo: se procesó determinada consulta).
- Expiración de mensajes.
- Prioridades.
- Routing de mensajes.
