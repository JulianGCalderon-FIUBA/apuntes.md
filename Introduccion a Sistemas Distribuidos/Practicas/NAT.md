El NAT o *Network Address Translation* es un mecanismo mediante el cual un router traduce direcciones IP entre dos espacios incompatibles. Suele ser utilizado en redes locales para aprovechar el uso de direcciones IP.

Los hosts dentro de una red local tienen asignada una IP únicamente dentro de esa subred. Cuando tratan de enviar un paquete a una dirección IP externa, el router NAT (y *default gateway* de la red) modifica la dirección IP del remitente e inyecta su propia IP antes de reenviar el paquete, asignando un puerto específico para esa traducción. También agrega una entrada a su tabla de traducciones en las que asocia el puerto especificado con la dirección IP local del remitente original.

Cuando la respuesta al paquete enviado llega al router NAT, este utiliza la tabla de traducciones para averiguar el remitente original del paquete (a partir del puerto), y reenvía el paquete a dicho host.

De esta forma, se simula tener más direcciones IP, utilizando los puertos de un router. Desde afuera, los paquetes de toda la subred parecen provenir de un único host.

Una tabla de traducción NAT mínimamente, tendría los siguientes campos:

| Puerto Router | Dirección Host | Puerto Host |
| ------------- | -------------- | ----------- |
| 23412         | 192.168.0.101  | 12412       |
| 11239         | 192.168.0.101  | 61231       |
| 31921         | 192.168.0.53   | 40032       |

El puerto del router será elegido de forma aleatoria, mientras que el puerto del host será, justamente, elegido por el host.
