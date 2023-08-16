---
title: ICMP The Internet Control Message Protocol
---

El protocolo ***internet control message protocol*** es utilizado por ***hosts*** y ***routers*** para comunicar información de capa de red entre ellos. Uno de los usos mas típicos es el de reporte de errores, como el conocido mensaje **"Destination Network Unreachable".** En algún punto del recorrido, un ***router*** no pudo encontrar un paquete, por lo que el protocolo **IP** envía un mensaje de error al ***host***.

Suele ser considerado como una parte de **IP**, pero arquitectónicamente yace por encima de **IP**, ya que sus mensajes están contenidos en el ***payload*** de los datagramas. Los mensajes contienen un campo de ***type***, un campo de ***code***, y los headers y los primeros *8 bytes* del *datagram* que ocasionó el error.

Un mensaje de ***ping*** envía un mensaje ***ICMP*** de type **8** y ***code 0***. La respuesta es un ***type 0*** y ***code 0***. Usualmente las implementaciones de ***TCP/IP*** soportan el ***ping*** directamente en el sistema operativo.

Otro mensaje interesante es el ***source quench message***. Es utilizado por un ***router*** congestionado para forzar a un ***host*** a que reduzca su taza de envío, aunque en la practica no es utilizado debido al propio mecanismo de control de congestión de ***TCP***.

El comando ***Traceroute*** es implementado con mensajes ***ICMP***. Es envían multiples mensajes con puertos poco probables con crecientes ***TTL*** desde 1 hasta $n$, siendo $n$ la cantidad de ***routers*** intermedios (esta cantidad es desconocida inicialmente). Los ***routers*** recibirán estos mensajes, eliminándolos si su ***TTL*** llega a 0 y enviando un mensaje de advertencia al ***host*** con ***type 11***, ***code 0***.

A partir del ***round trip time***, se calcula el tiempo acorde a cada ***router***. El numero de ***routers*** $n$ es determinado cuando finalmente llega un paquete al ***host***. Debido a que el puerto no estará usado, recibirá una advertencia de puerto inalcanzable ***(type 3, code 3)***. Esto sera interpretado por ***Traceroute*** como que se alcanzo la dirección de destino.

Existe una nueva versión de ***ICMP***, definida para ***IPv6***. Esta agrega definiciones necesarias para el funcionamiento de ***IPv6***.
