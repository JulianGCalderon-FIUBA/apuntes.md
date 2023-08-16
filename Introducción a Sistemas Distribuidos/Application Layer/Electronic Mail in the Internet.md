---
title: Electronic Mail in the Internet
---

El sistema de e-mails tiene tres componentes principales: ***user agents, mail servers,*** and the ***simple mail transfer protocol*** (SMTP). Los user agents permiten a los usuarios interactuar con los mensajes. Estos envían mensajes a los ***mail servers*** y estos se colocan en la cola de mensajes salientes del servidor. Estos son enviados al ***mail server*** de destino, el cual los coloca en el buzón adecuado. Cuando un user agent quiere recibir un mail, recupera sus mensajes del de su buzón de entrada en su mail server.

## 1. SMTP

El protocolo ***SMPT*** es un sistema mucho más antiguo que ***HTTP*** Debido a esto, el protocolo tiene algunas restricciones, como que todos los mensajes deben ser codificados en ***7-bit ascii***.

Para el envío de mensaje entre servidores, primero se establece una conexión TCP. En la etapa de ***handshake*** el cliente envía la dirección del remitente y la del destinatario. A continuación, envía el mensaje en cuestión.

## 2. Comparison with HTTP

En primer lugar, el protocolo HTTP es principalmente un ***pull protocol***. Por el otro lado, ***SMTP es un*** transfer protocol. Por otro lado, como fue indicado anteriormente, los mensajes *SMTP* deben ser codificados en 7-bit ascii. Por último, **HTTP** utiliza un mensaje distinto para cada objeto, mientras que ***SMTP*** utiliza un único mensaje.

## 3. Mail Message Formats

Cuando enviamos un ***mail***, se deben agregar ***header lines*** antes que el cuerpo en sí, utilizando una línea en blanco como separación.

Todos los ***headers*** deben contener el "***From:"***, "***To:"***. De forma opcional, puede contener ***"Subject:".***

## 4. Mail Access Protocols

Usualmente, el usuario ejecuta un ***user agent*** localmente, accediendo a su buzón almacenado en un ***mail server***. Generalmente, este es mantenido por el ***ISP***.

Se utilizan protocolos de acceso especiales para transferir mensajes del servidor a la computadora local. Entre ellos, está POP3, IMAP, e incluse HTTP.

### POP

**POP3 (Post Office Protocol - Version 3)** es un protocolo extremadamente simple. Progresa a través de tres etapas: authorization, transaction, and update. Durante la primera fase, el *user agent* envía el usuario y su contraseña. Durante la segunda fase, el ***user agent*** recupera los mensajes, durante esta fase también puede marcar mensajes para el borrado y obtener estadísticas. Durante la primera fase, se actualiza el buzón de entrada.

En el modo ***download-and-delete***, el usuario emite los comandos: ***list, retr,*** and **dele**. En el modo ***download-and-keep***, el usuario deja los comandos en el buzón luego de descargarlos.

### IMAP

Este protocolo permite asociar mensajes a distintas carpetas y que este ordenamiento se mantenga en el servidor. Además, permite al usuario obtener componentes individuales de los mensajes.

### Web-Based E-Mail

Con este servicio, un navegador web puede ser usado para comunicarse con el buzón, a través de mensajes HTTP
