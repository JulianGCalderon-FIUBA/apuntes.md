---
title: What is the internet
---

¿Qué es el internet? Podemos responder esta pregunta de diversas formas. La primera sería analizar el internet desde el software y hardware básico que lo compone, pero otro enfoque podría ser describir el internet como una infraestructura que provee un servicio a las aplicaciones distribuidas.

## 1. A Nuts-and-Bolts Description

El internet es una red de computadoras que interconecta miles de millones de dispositivos. En la jerga del internet, todos estos dispositivos se denominan *hosts* o *end systems.*

Estos dispositivos están conectados entre sí por una red de *communication links* y *packet switches*. Los diferentes links pueden transmitir información a diferentes tasas, con la *transmission rate* medida en *bits/second.*

Cuando un dispositivo quiere enviar información a otro dispositivo, este se separa en pequeños segmentos, conocidos como *packets,* les agrega un encabezado, y son enviados de forma separada a través de los links. Estos paquetes son enviados a destino, donde son reensamblados en la información original.

Un *packet switch* toma un *packet* de sus links de entrada y lo reenvía a uno de sus links de salida. La forma más común de *packet switches* es la de *routers* o *link-layer* *switches*. La secuencia de elementos que atraviesa un *packet* hasta llegar a su destino se denomina *route* o *path*.

Los hosts acceden al internet a través de los *Internet Service Providers (ISP)*. Cada uno de estos es, en sí, una red de *packet switches* y links. Los ISP de bajo nivel a su vez están conectados entre sí a través de ISP de mayor nivel. Cada red ISP es administrada de forma independiente, pero ejecuta el protocolo IP y se conforma con ciertas nomenclaturas y convenciones

Las piezas del internet utilizan protocolos para controlar el envío y la recepción de la información. Los protocolos de internet más importantes son: *TCP (Transmission Control Protocol)* e *IP (Internet Protocol).* Este último específica el formato de envío de información entre hosts y routers. Los protocolos principales de internet se conocen de forma colectiva como TCP/IP

Es importante que todos estén de acuerdo en que hace cada uno protocolo, para que se puedan crear sistemas que operen entre sí. Estos protocolos están definidos en documentos con estándares IEFT, conocidos como RFC *(requests for comments).*

## 2. A Service Description

Otra forma de describir el internet es como una infraestructura que provee servicios a distintas aplicaciones.

Las aplicaciones que involucran múltiples dispositivos conectados se determinan **aplicaciones distribuidas.** Estas aplicaciones son ejecutadas en hosts.

Los hosts conectados a internet proveen una *socket interface* que indican como un programa ejecutándose en un dispositivo le pide a la infraestructura de internet de entregar información a un programa ejecutándose en otro dispositivo. Esta interfaz se compone de una serie de reglas que tiene que respetar el programa para poder comunicarse correctamente.

## 3. What Is a Protocol?

Se necesitan dos (o más) entidades en comunicación siguiendo el mismo protocolo para lograr una tarea. Toda comunicación entre dos dispositivos se realiza siguiendo un protocolo.

> Un protocolo define el formato y el orden de los mensajes intercambiados entre dos o más entidades en comunicación, así como las acciones que se toman en la recepción o envío de estos mensajes.
