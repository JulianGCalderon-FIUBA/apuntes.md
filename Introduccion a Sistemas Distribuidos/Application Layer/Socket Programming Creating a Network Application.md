---
title: Socket Programming Creating a Network Application
---

Existen dos tipos de aplicaciones de red. Aquellas que implementan una operación especificada en un estándar de protocolo, como en un RFC. Estas aplicaciones se suelen considerar ***"open"***. Por otro lado, tenés las redes que implementan un protocolo propietario, que no fue publicado de forma libre.

## 1. Socket Programming with UDP

Para poder utilizar UDP, debemos añadir la dirección y el puerto de destino al paquete antes de enviarlo a través del *socket*. Este viaja a través de la red y llegará a destino sin ningún tipo de seguridad. Cuando este llega a destino, este inspeccionará sus contenidos y tomará la acción correcta.

Cuando se crea un ***socket,*** se asocia a un identificador conocido como port number. Al enviar un paquete, la dirección y el puerto del emisor también será aclarada en el mismo. Esto permite al receptor del paquete poder comunicarse con el emisor.

## 2. Socket Programming with TCP

El protocolo TCP, por otro lado, es orientado a conexiones. Antes de que dos hosts puedan comunicarse entre sí, está la fase de ***handshake.***

Cuando se crea una conexión TCP, debe indicarse la dirección y el puerto de destino. De esta forma, para enviar información una vez creado el ***socket*** no es necesario indicar el destinatario.

Una vez creado el ***socket***, el cliente inicia un ***handshake*** de tres pasos y establece una conexión con el servidor. Primero el cliente le envía un mensaje a un servidor, que contiene un listening ***socket*** esperando a establecer conexiones con los clientes. Este, al recibir el mensaje, creará una conexión TCP particular para este cliente.

Desde el punto de vista de la aplicación, los ***sockets*** están directamente conectados a través de una tubería.
