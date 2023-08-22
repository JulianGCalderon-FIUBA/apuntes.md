---
title: Introduction of the Link Layer
---

Llamaremos a cualquier dispositivo que ejecuta un protocolo de capa de enlace como un nodo, y a los canales de comunicación entre nodos adyacentes como enlaces.

## 1. The Services Provided by the Link Layer

Algunos posibles servicios ofrecidos por un protocolo de capa de enlace son:

- **Framming:** Consiste en encapsular el paquete de datos en un *frame* de capa de enlace y transmitirlo por sobre el link. Este contiene un *data field* y múltiples *header fields*.
- **Link Access:** El protocolo de *medium access control (MAC)* especifica las reglas por las cuales se transmite un *frame* a través de un enlace. Por enlaces punta a punta, este es relativamente simple (o inexistente). En los enlaces de *broadcast*, MAC ayuda a coordinar las transmisiones de múltiples nodos.

	Los dispositivos son identificados dentro de una red local de acceso múltiple, a partir de una dirección MAC.

- **Reliable Delivery:** Si un protocolo de capa de enlace ofrece envío confiable, garantiza que se moverán los datagramas de cada de red entre un enlace y otro sin errores. Este debe alcanzarse con acuses de recibo (ACK) y retransmisiones. Este servicio suele ser ofrecido en links con tasas de errores muy altas, pero puede ser innecesario en enlaces con baja tasa de errores.
- **Error Detection and Correction:** A partir de campos de detección de errores en el *frame*, se puede determinar si hubo alguna corrupción en el paquete enviado. La corrección de errores ocurre cuando se detecta en que parte del paquete surgió un error, para poder corregirlo.

## 2. Where is the Link Layer Implemented?

En su mayoría, la capa de enlace es implementada en un adaptador de red, también referido como **network interface card (NIC)**. Esta es un controlador de capa de enlace que implementa múltiples servicios, usualmente por hardware.

Desde el remitente, el controlador toma el datagrama, lo encapsula en un *frame* y lo transmite a través de uno de sus enlaces de comunicación, siguiendo un protocolo de acceso de enlace. Desde el receptor, este recibe un *frame* completo de un enlace, extrae el datagrama.
