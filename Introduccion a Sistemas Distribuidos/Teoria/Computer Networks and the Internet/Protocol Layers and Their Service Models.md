---
title: Protocol Layers and Their Service Models
---

¿Cómo podemos organizar la arquitectura de redes de forma ordenada?

## 1. Layered Architecture

Una **layered architecture** nos permite discutir una parte específica y definida de un sistema grande y complejo. Esta simplificación aporta mucho valor, ya que provee modularización. Nos permite fácilmente cambiar la implementación del servicio proporcionado por cada capa.

### Protocol Layering

Para proveer una estructura al diseño de protocolos de red, los protocolos se organizaron en capas o *layers*. Cada protocolo pertenece a una capa particular de la arquitectura. Los servicios que ofrece una capa a su capa superior son denominados el *service model* de la capa. Cada capa provee su servicio (1) realizando ciertas acciones dentro de esa capa y (2) usar los servicios de su capa inferior.

Estas capas pueden ser tanto implementadas en hardware como en software. Los *application-layer protocols* (como HTTP y SMTP) son generalmente implementados por software dentro de los hosts, así como los *transport-layer protocols*. Debido a que la *physical layer* y la *data link layer* son los responsables por manejar la comunicación en un link particular, son implementados por hardware en la placa de red. La *network-layer* suele tener una implementación mixta, tanto con software como con hardware.

Algunas personas se oponen a esta arquitectura, ya que en este enfoque algunas capas duplican comportamiento de capas inferiores, como la recuperación de errores. Otra desventaja es que algunas capas requieren información disponible en otra capa, rompiendo encapsulamiento.

Cuando se combinan, las varias capas de protocolo con conocidas como el **stack protocol.** El *IP stack* consiste en cinco capas: *physical, link, network, transport,* y las *application layers.*

### Application Layer

Aquí es donde residen las aplicaciones de red. En el internet, esta capa incluye muchos protocolos, como el HTTP (transferencia y pedido de documentos de web), SMPT (transferencia de emails), FTP (transferencia de archivos).

Estos protocolos se distribuyen en múltiples hosts para poder intercambiar información entre múltiples sistemas. En esta capa nos referimos a estos *packets* de información como *message.*

### Transport Layer

Esta capa se encarga de transferir los *messages* de la capa anterior entre los *endpoints.* Hay dos protocolos principales.

- TCP: Provee un servicio orientado a conexiones. Garantiza el envío y el flujo de control del mismo desde un *end-point* al siguiente. También se encarga de separar mensajes largos en pequeños *segments* y provee mecanismos de control de congestión.
- UDP: Provee un servicio no orientado a conexiones: Este servicio no provee confianza, ni ningún tipo de control.

En esta capa nos referimos a los *packets* de información como *segment.*

### Network Layer

Esta capa se encarga de mover los *segments* (denominados *datagrams*) entre los hosts. Esta capa recibe el *segment* y una dirección de envío y se encarga de enviar el segmento al destino correcto.

Esta capa incluye el conocido protocolo IP (de hecho, esta capa es muchas veces conocida como la capa IP)**.** Define los campos del *datagram* así como la forma de interactuar con ellos. También contiene protocolos de rutina que se encargan de determinar las rutas que toman los *datagrams* para llegar a destino. Cada administrador de red decide cuál protocolo usar.

### Link Layer

Para mover un *packet* de un nodo al siguiente, se utiliza la *link layer*. En cada nodo, *la network layer* le da el paquete a la *link layer*, el cual se encarga de enviar el mensaje al siguiente nodo. Esta capa provee confianza de envío de un nodo al siguiente.

Ejemplos de algunos protocolos en esta capa son: Ethernet, Wi-Fi, entre otros. Un mismo *packet* puede ser manejado por múltiples de estos protocolos a lo largo de su ruta.

### Physical Layer

A diferencia de la capa anterior que se encarga del envío de *packets*, el trabajo de esta capa es el del envío de bits individuales desde un nodo al siguiente.

El protocolo utilizado en esta capa dependen del medio del link utilizado

### The OSI Model

El *IP stack protocol* no es el único que se utiliza. El modelo **OSI (Open Systems Interconnection)** se utilizaba en los inicios del internet.

Este protocolo se separa en siete capas: *application layer, presentation layer, session layer, transport layer, network layer, data link layer,* y la *physical layer.*

Es un protocolo similar al *IP stack protocol,* con dos capas adicionales:

- **Presentation Layer**: Provee servicios que permiten que las aplicaciones en comunicación puedan interpretar correctamente los datos enviados. Estos servicios proveen encriptación, compresión y descripción de los datos. Libera a la aplicación de la preocupación de conocer el formato interno de los datos.
- **Session Layer:** Provee delimitación y sincronización de los datos intercambiados. Esto permite recuperar datos faltantes y construir *checkpoints.*

## 2. Encapsulation

Los *packet switches* no implementan todas las capas del *protocol stack,* suelen implementar las capas inferiores. *Link-layer switches* suelen implementar las capas 1 y 2 *(physical y link),* mientras que los routers además implementan la capa 3 *(network).* En otras palabras, las *link-layer switches* no son capaces de detectar direcciones IP como los routers, sino únicamente direcciones de protocolos de capa 2 (Ethernet, Wi-Fi). Los hosts implementan las 5 capas, esto se debe a que la mayoría de la complejidad de la red se encuentra en los extremos.

Cada capa le agrega información al mensaje que luego va a ser analizada por su contraparte. El *application-layer message* con el *transport-layer header information* forman un *segment*. La *transport layer* le pasa el **segment** a la *network-layer*, la cual le agrega la *network-layer header information*, formando un *datagram*. Este a su vez es pasado a la *link-layer* la cual le agrega su propio información de cabecera. De esta forma, el mensaje en cada etapa se puede separar en *header fields* y *payload field* (este último es usualmente el *packet* de la capa anterior). Esta información agregada va a ser analizada por su contraparte en el extremo receptor del link.

Este proceso de encapsulamiento puede ser más complejo. Un gran mensaje puede ser dividido en múltiples segmentos por la *transport layer* (a su vez, transformados en *datagrams).* Los cuales serán nuevamente reconstruidos en el extremo receptor.
