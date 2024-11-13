Se comunica a través de mensajes. Esto hace que la comunicación sea transparente al resto de aplicaciones.

Resuelve problemas de transparencia respectos a ubicaciones, fallos, escalabilidad.

## Modos de Operación

Tiene dos modos de operación:

- **Bus de información**: Pueden enviarse mensajes bajo ciertos tópicos, para que aquellos interesados lo reciban. Los mensajes se pierden si nadie los toma.
- **Cola de mensajes**: Pueden enviarse mensajes con un destinatario definido. Se quedan esperando hasta que este lo reciba.

## Sincronismo y Asincronismo

El middleware puede ser sincrónico o asincrónico:

- **Sincrónico**: Se modela una conexión punto a punto. Permite obtener respuestas instantáneas.
- **Asincrónico**: Se implementa utilizando colas. La arquitectura soporta periodos de discontinuidad del transporte. Se deben configurar alertas para cuando se llenan las colas. Tienen un tamaño límite, no existe la cola infinita. Si se quiere recibir respuesta a los pedidos, es necesario tener dos colas (una por cada cliente de la comunicación)

## Broker

El broker tiene las siguientes prioridades:

- El broker provee transparencia de localización entre emisor y receptor.
- Pueden soportar lógica en el middleware para filtrado y modificación de mensajes.
- Además, brindan un punto de control y monitoreo.
- Pueden ofrecer persistencia del mensaje en caso de que no haya nadie para recibirlo aun.
