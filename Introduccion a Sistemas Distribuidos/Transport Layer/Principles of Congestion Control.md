---
title: Principles of Congestion Control
---

## 1. The Causes and the Costs of Congestion

A medida que la tasa de arribo de paquetes se acerca a la capacidad del medio, entonces se experimentan grandes ***queuing delays***.

Un remitente deberá realizar retransmisiones para compensar por los datos perdidos debido a ***buffer overflow***.

Las retransmisiones innecesarias ante los grandes delays pueden causar que el router gaste recursos en enviar copias innecesarias de un paquete.

Cuando un paquete es perdido a lo largo de un camino, la capacidad de transmisión utilizada en cada uno de los ***links*** que había enviado el paquete hasta ese punto termina siendo desperdiciada.

## 2. Approaches to Congestion Control

Examinaremos algunos enfoques específicos de TCP para lidiar con el control de congestión. En el nivel mas alto, podemos distinguir los distintos enfoques según la asistencia que provee la capa de red para el control de congestión:

- ***End-to-end congestion control***: En este enfoque, la capa de red no provee soporte explicito a la capa de transporte, incluso la presencia de congestión debe ser inferida por los ***end systems*** en función del comportamiento observado.
- ***Network-assisted congestion control:*** En este otro enfoque, los routers proveen ***feedback*** explicito a los ***hosts*** respecto al estado de congestión de la red. Existen dos formas para un ***router*** de comunicarse con los ***hosts:*** la primera opción consiste en enviar notificaciones ene la forma de un ***choke packet;*** la segunda opción (y la mas común) consiste en actualizar un campo en los paquetes que viajan entre los ***hosts*** para indicar congestión
