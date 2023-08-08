# 1. The TCP Connections

El protocolo ***TCP*** es ***connection-oriented*** debido a que antes de que una aplicación pueda comenzar a enviar datos a otra, debe primero ocurrir un saludo inicial entre ambos procesos. Las conexiones ***TCP*** no son una conexion ***end-to-end*** como la de un ***circuit-switched-network***, sino son conexiones lógicas donde el estado común reside únicamente en el ***TCP*** de los ***end systems***. Los elementos de red en el centro de la red no contienen esta información.

Una conexión ***TCP*** provee un servicio ***full-duplex,*** un proceso A puede enviar información al proceso B al mismo tiempo que este le envía información en sentido contrario al proceso A. Se dice que esta conexión es ***point-to-point*** ya que conecta únicamente dos ***end systems***.

Debido a que se envían tres segmentos de información en el procedimiento de establecimiento de la conexión, se refiere usualmente como ***three-way handshake.*** Los primeros dos segmentos no contienen información de la aplicación, mientras que el último puede hacerlo. Una vez establecida la conexión los procesos envían información a través del ***socket***. ***TCP*** redirige esta información al ***send buffer*** de su conexión, el cual se configura durante el saludo inicial. De vez en cuando, ***TCP*** tomará pedazos de información del ***send buffer*** y la enviará a la capa de red.

La cantidad máxima de información que puede ser enviada a la vez es limitada por el ***MMS (maximum segment size)***. Este es usualmente determinado por el tamaño del mayor ***link-layer frame*** que puede ser enviado por el ***local sending host***, este es llamado ***MTU (maximum transmission unit)***. El ***MMS*** se configura para asegurarse que el segmento completo pueda caber en un único frame. ***TCP*** empareja cada ***chunk*** de datos con un header, formado los ***TCP segments***.

***TCP*** utiliza ***pipelining***, permitiendo que el remitente tenga múltiples segmentos transmitidos pero no confirmados en cualquier momento. Este mecanismo puede incrementar drásticamente el ***throughput*** de una sesión. La cantidad específica de paquetes que puede tener sin confirmación dependerá de los mecanismos de control de flujo y control de congestión.

# 2. TCP Segment Structure

Como el protocolo ***UDP***, el ***header*** de ***TCP*** contiene los puertos de destino y envio utilizados, y un campo de ***checksum***. Además, contiene los siguientes campos:

- ***sequence number field (32bit)***
- ***acknowledgment number field (32bit)***
- ***receive window field (16bit)***
- *header length field (5bit)*
- ***options fields,*** son opcionales y de tamaño variable, dependerán del contexto de la comunicación
- ***flag field (8bits):***
    - ***ACK bit:*** Indica que el valor almacenado en el ***ack field*** es valido.
    - ***RST, SYN, FIN bits***: Utilizados en el ***setup*** y ***teardown*** de la conexión
    - ***CWR, ECE bits***: Utilizados en las notificaciones explícitas de congestión.
    - ***PSH*** bit: Indica que el receptor de enviar los datos a la capa de arriba de forma inmediata
    - ***URG*** bit: Indica que hay información en el segmento que es marcada como segmento. La dirección del último ***bit*** de información urgente es indicado en el ***urgent data pointer field***.

![[Apuntes/Introducción a Sistemas Distribuidos/3 Transport Layer/Attachments/5 Connection-Oriented Transport TCP 1.png|Untitled]]

## Sequence Numbers and Acknowledgment Numbers

El protocolo ***TCP*** ve a la información como un desestructurado pero ordenado ***stream*** de ***bytes.*** El ***sequence number*** de un segmento es entonces el número de ***byte*** del primer ***byte*** del segmento. Por otro lado, el ***acknowledgment number*** es el ***sequence number*** del próximo segmento que espera recibir. ***TCP*** confirma todos los ***bytes*** hasta el primer faltante, por lo que se dice que provee ***cumulative acknowledgments***.

Ante recibir un segmento fuera de orden, Existen dos implementaciones válidas:

- El receptor inmediatamente descarta el segmento fuera de orden
- El receptor guarda los ***bytes*** y esperan a los ***bytes*** faltantes para completar la información

La segunda alternativa es utilizada usualmente debido a su eficiencia en términos de ancho de banda de red.

Para minimizar la posibilidad de que un segmento que aún está presente en la red de una conexión ya terminada sea equivocado por un segmento válido en una conexión posterior, el primer número de secuencia se elige de forma aleatoria.

Cuando el ***acknowledgment*** es enviado a través del segmento que lleva nueva información, se dice que el *acknowledgment fue piggybacked.*

# 3. Round-Trip Time Estimation and Timeout

TCP utiliza un ***timeout/retransmit mechanism*** para recuperar los segmentos perdidos. ¿Qué intervalo deberíamos elegir para los ***timeouts?***

## Estimating the Round-Trip Time

El ***`SampleRTT`*** se calcula para un segmento como el tiempo entre su envió y su confirmación. La mayoría de las implementaciones calculan uno a la vez, generando un nuevo valor aproximadamente una vez por ***RTT***.

Debido a la fluctuación de estos valores, se creará un promedio `EstimatedRTT` que es calculado iterativo de forma iterativa de la siguiente forma, con un $\alpha$ de $1/8$

$$
\text{EstimatedRTT} = (1{-}\alpha) \cdot \text{EstimatedRTT} + \alpha \cdot \text{SampleRTT}
$$

Este promedio es llamado, ***exponential weighted moving average***, le da más peso a las muestras más recientes. Por otro lado, también aporta valor considerable calcular la variabilidad del ***RTT***, utilizando la siguiente fórmula, con un $\beta = 1/4$

$$
\text{DevRTT} = (1{-}\beta) \cdot \text{DevRTT} + \beta\cdot |\text{SampleRTT} - \text{EstimatedRTT}|
$$

Finalmente, calculamos el intervalo de la siguiente forma, con un intervalo inicial de un segundo.

$$
\text{TimeoutInterval} =\text{EstimatedRTT} + 4\cdot\text{DevRTT}
$$

# 4. Reliable Data Transfer

***TCP*** entonces crea un servicio confiable de transferencia de datos encima de el servicio ***best-effort*** del **IP**.

Si bien conceptualmente podemos asumir la utilización de un ***timer*** por paquete, en la practica esto es muy costoso por lo que se suele utilizar un único ***timer*** de retransmisión para multiples paquetes transmitidos no todavía confirmados.

Veremos primero una implementación simple del protocolo ***TCP***. En la llegada de información de la aplicación, ***TCP*** envía encapsula los datos en un segmento y los envía a internet, comenzando el ***timer*** si este aun no esta corriendo. Ante un ***timer interrupt***, ***TCP*** retransmite el primer paquete sin confirmación y reinicia el timer. Ante la llegada de un ***acknowledge***, ***TCP*** reinicia el ***timer*** (de ser necesario).

## Doubling the Timeout Interval

En esta modificación, el tiempo del intervalo es duplicado con cada retransmisión, pero vuelve a ser restablecido ante alguno de los otros dos eventos. Los intervalos crecen exponencialmente luego de cada retrasmisión. Esta modificación provee una forma limitada de congestión de control. 

Usualmente la perdida de información es causada por congestión en la red, por lo que si cada usuario sigue retransmitiendo los paquetes a la misma taza, es posible que empeore la situación.

## Fast Retransmit

Muchas veces, el remitente puede detectar perdida de paquetes incluso antes de que ocurra el ***timer interrupt,*** a partir de la llegada de ***ACKs*** duplicados.

Cuando un receptor recibe un segmento fuera de orden, este detecta un salto en el ***data stream***. Esto puede ser causado por perdida de información o un reordenamiento en la red. El receptor envía inmediatamente una confirmación para el ultimo paquete recibido en orden, indicando al remitente que se perdió un paquete.

Cuando el receptor recibe tres ***ACKs*** duplicados, entonces realiza un ***fast retransmit***, retransmitiendo el segmento perdido antes del ***timer interrupt***.

## Go-Back-N or Selective Repeat

Un remitente **TCP** debe únicamente mantener el menor numero de secuencia transmitido pero no confirmado, y el numero de secuencia del proximo ***byte*** a enviar. En este sentido, es similar a un protocolo *GBN.* Sin embargo, tiene algunas diferencias importantes: en primer lugar, muchas implementaciones de ***TCP*** almacenan paquetes recibidos correctamente pero fuera de orden; por otro lado ***TCP*** únicamente retransmite el primer paquete recibido no confirmado ante un ***interrupt,*** en lugar de todos.

Una posible modificación de ***TCP*** consiste en el llamado ***selective acknowledgment*** que permite a un receptor confirmar paquetes fuera de orden de forma selectiva, en lugar de utilizar ***cumulative acknowledging***. Si lo combinamos con ***selective retransmission,*** nuestro protocolo ***TCP*** se parecerá bastante a nuestro protocolo genérico **SR**.

# 5. Flow Control

Cuando una conexión *TCP* recibe información correcta y en secuencia, la coloca en el ***receive buffer***. Si la aplicación es relativamente lenta en leer esta información, el receptor puede fácilmente causar un ***overflow*** en el buffer de lectura. El servicio de ***flow-control*** elimina la posibilidad de que esto ocurra, provee un servicio de ***speed-matching*** para emparejar la velocidad de lectura con la velocidad de bajada. Este servicio el distinto al de ***congestion control;*** ambos producen el mismo efecto, pero por razones distintas.

Para implementar este mecanismo, un host ***mantener la siguiente información:

- ***`LastByteRead`:* El numero del ultimo byte que fue leído por la aplicación
- ***`LastByteRcvd`:* El numero del ultimo byte que fue recibido a través de la red
- `r***wnd`:* Tambien conocida como ***receiver window.*** Definida a partir de las anteriores variables como el espacio libre en el ***buffer***

El host agregara este ultimo campo a los paquetes transferidos a través de la red, para comunicarle al otro ***host*** del estado actual del ***buffer***. Este a su vez deberá mantener las siguientes variables:

- `LastByteSend`: ***El numero del ultimo byte que fue enviado a través de internet
- *`LastByteAck`:* El numero del ultimo byte que fue confirmado por el host.

A partir de estos dos valores, podremos calcular la cantidad de datos sin verificar que fueron enviados. El protocolo tratara de que esta cantidad nunca sea mayor al tamaño de la ventana del receptor.

Para permitir que un ***host*** que únicamente recibe información le comunique al otro ***host*** su ***window***, entonces este valor también se agregara a los mensajes de ***ACKs.***

## 6. TCP Connection Management

Cuando una aplicación quiere iniciar una conexión ***TCP,*** este le informa al  cliente ***TCP*** el cual procederá a establecer una conexión con el servidor.

1. El cliente enviara un segmento especial llamado ***SYN segment***, el cual no tiene información y contiene el ***SYN bit*** en 1. Este seleccionará automáticamente un numero de secuencia
2. El servidor recibirá el segmento, reservara las variable necesarias para la conexión y enviara el ***ack*** con el ***SYN bit en 1***. Este segmento es conocido como ***SYNACK.*** Al igual que el cliente, seleccionará un numero aleatorio para su numero de secuencia.
3. El cliente al recibir el segmento, reserva las variables necesarias para la conexión y envía un ***ack*** con el ***SYN bit*** en 0 ya que la conexión ya esta establecida. Este paquete puede contener información.

Debido a estos tres pasos, este procedimiento se conoce como ***three-way handshake***.

Cualquiera de los dos procesos puede elegir terminar la conexión, al ocurrir esto, se liberan los recursos utilizados en la misma.

1. El cliente envía un ***close command***, con el ***FIN*** ***bit*** en 1.
2. El servidor lo recibe y envía un ***ACK*** para el segmento recibido
3. El servidor envía su propio segmento de cierre, con el ***FIN bit*** en 1
4. Finalmente, el cliente envia el ACK ***para el segmento de cierre y ambos hosts*** liberan los recursos utilizados.

Durante la vida de una conexión ***TCP***, los ***hosts*** atraviesan distintos estados:

![[Apuntes/Introducción a Sistemas Distribuidos/3 Transport Layer/Attachments/5 Connection-Oriented Transport TCP 2.png|Client State Diagram]]

Client State Diagram

![[Apuntes/Introducción a Sistemas Distribuidos/3 Transport Layer/Attachments/5 Connection-Oriented Transport TCP 3.png|Server State Diagram]]

Server State Diagram

El ultimo estado del cliente (***time wait***) se utiliza para reenviar un ***ack*** en caso de que este se haya perdido en la red.

Cuando un cliente envía un ***SYN SEGMENT*** a una dirección y puerto en el que no hay ningún ***listening socket***, este le reenviará un segmento especial de ***reset*** con el ***RST*** bit en 1.