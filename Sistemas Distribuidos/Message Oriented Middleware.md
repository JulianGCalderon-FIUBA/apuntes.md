## Modos

Tiene dos modos de operación:

- **Bus de información**: Pueden enviarse mensajes bajo ciertos tópicos, para que aquellos interesados lo reciban. Los mensajes se pierden si nadie los toma.
- **Cola de mensajes**: Pueden enviarse mensajes con un destinatario definido. Se quedan esperando hasta que este lo reciba.

## Sincrónico

Se modela una conexión punto a punto. Permite obtener respuestas instantáneas.

## Asincrónico

Se implementa utilizando colas. La arquitectura soporta periodos de discontinuidad del transporte.

Se deben configurar alertas para cuando se llenan las colas. Tienen un tamaño límite, no existe la cola infinita.

Si se quiere recibir respuesta a los pedidos, es necesario tener dos colas (una por cada cliente de la comunicación)

## Operaciones

Algunas operaciones comunes son:

- `Put`: Publicar un mensaje.
- `Get`: Esperar hasta que un mensaje sea detectado, luego eliminarlo y retornarlo.
- `Poll`: Revisa mensajes pendientes, sin bloquear.
- `Notify`: Asocia un _callback_ utilizado por el middleware para ser ejecutado frente a publicación de ciertos mensajes.

## Broker

Proveen transparencia de localización entre emisor y receptor.

Pueden soportar lógica en el middleware para filtrado y modificación de mensajes.

Brindan un punto de control y monitoreo.
