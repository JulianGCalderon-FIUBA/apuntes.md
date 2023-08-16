---
title: Connectionless Transport UDP
---

DNS es un ejemplo de una protocolo de capa de aplicación que típicamente utiliza ***UDP***. Hay múltiples razones por las cuales una aplicación puede preferir este protocolo por sobre el método confiable ***TCP***.

- **Control fino de la información que se envía, y cuando:** En ***UDP***, tan pronto como le proceso de aplicación pasa la información a ***UDP***, este crea un segmento y lo envía a través de la red. Por el otro lado, ***TCP*** puede retrasar el envió debido a su mecanismo de control de congestión. Por otro lado, ***TCP*** continuará enviando el segmento si no recibe un ***acknowledge*** de su llegada. Las aplicaciones de tiempo real utilizan ***UDP*** ya que pueden aceptar cierto grado pérdida de información.
- ***Sin establecimiento de la conexión***: ***TCP*** utiliza un ***three-way handshake*** antes de empezar a transferir información, por lo que puede generar ***delay*** adicional en el envío de información.
- ***Sin estado de la conexión:*** ***TCP*** mantiene un estado de la conexión en los ***end systems,*** incluye ***buffers***, y una numerosa cantidad de parámetros, por lo que puede ser más pesado que la utilización de un protocolo minimalista como ***UDP***.
- **Pequeño **header overhead***:** El segmento ***TCP*** tiene 20 ***bytes** de **header***, a diferencia del segmento ***UDP*** que contiene únicamente 8 ***bytes***.

Existen múltiples razones por las cuales una aplicación preferiría utilizar ***UDP***, en especial aquellas aplicaciones de multimedia. Aunque es común, la utilización de ***UDP*** es controversial y a que no contiene un mecanismo de control de congestión.

Cuando la tasa de pérdida de paquetes es baja, y con algunas organizaciones bloqueando el tráfico ***UDP*** por razones de seguridad, el protocolo ***TCP*** es cada vez más atractivo para el transporte de ***streaming media***.

## 1. UDP Segment Structure

Los datos de la aplicación ocupan el ***data field*** del segmento. El ***UDP header*** tiene únicamente cuatro campos, los primero dos son los mencionados anteriormente (dirección y puerto de destino). Luego, sigue el ***length field*** el cual tiene el largo explícito del segmento. Este es importante ya que puede variar entre un segmento y otro. El último campo, ***checksum,*** es utilizado para verificar si hubo algún error durante el envío del segmento

## 2. UDP Checksum

El ***UDP checksum*** se utiliza para determinar si los ***bits*** dentro del segmento fueron alterador. Desde el lado del remitente, se realiza el complemento a uno de la suma de todas las palabras de ***16 bits*** en el segmento, dando la vuelta en caso de un **overflow**. Este valor se introduce en el campo de ***checksum***. Si el segmento llega correctamente, entonces la suma desde el lado del receptor debe tener los ***16 bits*** en *1*. Por lo que sabremos si hubo alguna alteración durante el envío.

Si bien los protocolos de capa de ***link*** implementan verificación de errores, no tenemos garantías de que todos los ***links*** lo hicieron. Además, el error puede haber ocurrido cuando el segmento se almaceno en la memoria del router. ***UDP*** debe asegurarse de proveer detección de errores ***end-to-end***. Esto es lo que se conoce ***end-end principle***.

Algunas implementaciones de ***UDP*** simplemente descartan el segmento alterado, mientras que otras se lo envían a la aplicación como advertencia.
