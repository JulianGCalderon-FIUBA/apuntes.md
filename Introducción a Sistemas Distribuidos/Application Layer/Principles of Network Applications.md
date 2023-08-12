## 1. Network Application Architectures

En el centro del desarrollo de aplicaciones de red está la escritura de programas que se ejecutan en distintos end systems y se comunican entre ellos a través de la red.

Desde el punto de vista del desarrollador, la arquitectura de red es fija y provee un conjunto específico de servicios a las aplicaciones. La arquitectura de aplicación, por otro lado, es diseñada por el diseñador y dicta como se estructura la aplicación en diversos ***end systems***. Hay dos paradigmas de arquitectura que se utilizan en las aplicaciones modernas.

En la arquitectura cliente-servidor, siempre existe un ***host*** constantemente encendido con dirección fija y conocida, denominado ***server,*** que provee servicio a múltiples ***hosts,*** denominados clientes. En esta arquitectura, los clientes no se comunican de forma directa entre sí.

Comúnmente en estas arquitecturas, un único servidor es incapaz de resolver todos los pedidos de los clientes. Por esta razón, un ***data center***, juntando un gran número de servidores, es utilizado para crear un poderoso ***server*** virtual.

En la arquitectura peer-to-peer existe mínima o nula dependencia en un servidor dedicad. En su lugar, la aplicación explota la comunicación entre pares, llamados ***peers***.

Una de las características más importantes de esta arquitectura es su ***self-scalability***. La velocidad de descarga aumenta a medida que aumenta el número de ***peers***.

## 2. Processes Communicating

En la jerga de los sistemas operativos, no son los programas los que se comunican, sino los procesos. Los procesos en dos ***end systems*** diferentes se comunican intercambiando mensajes a través de la red.

### Client and Server Processes

Por cada par de procesos en comunicación, normalmente etiquetamos a uno como el ***cliente*** y otro como el ***servidor***. En una arquitectura P2P, el que envía el archivo se denomina ***servidor*** y el que lo recibe se denomina ***cliente***.

Los procesos intercambian mensajes a través de una interfaz de ***software conocida como*** socket. Esta interfaz también es conocida como la ***API*** entre la aplicación y la red. El desarrollador no tiene control de lo que ocurre en esta interfaz, salvo por la elección de que protocolo usar o la configuración de algunos parámetros de la misma.

### Addressing Processes

Para identificar un proceso receptor, necesitamos dos piezas de información: La dirección del ***host*** y un identificador que especifica el proceso receptor ***del host***.

En el internet, el ***host*** se identifica con la dirección **IP,** mientra que el proceso receptor se identifica con el ***port number***. Las aplicaciones populares tienen puertos específicos asignados, un servidor web se identifica con el número de puerto 80.

## 3. Transport Services Available to Applications

Cuando desarrollamos una aplicación, debemos seleccionar el protocolo de ***transport-layer*** que queremos utilizar. Estos se pueden clasificar según los servicios que proveen.

### Reliable Data Transfer

Este servicio garantiza que los datos enviados por la aplicación llegaran a destino correctamente y en el orden especificado. Cuando un protocolo de transporte no provee este servicio, algunos de los paquetes enviados a destino no llegaran al proceso receptor. Esto es aceptable para ***loss-tolerance applications***, como aplicaciones multimedia

### Throughput

Debido al congestionamiento de la red, el ***throughput*** puede fluctuar a lo largo del tiempo. Este servicio garantiza que se podrá proveer un ***throughput*** constante a lo largo de toda la comunicación.

Aquellas aplicaciones que tienen este tipo re requerimientos se conocen como ***bandwidth-sensitive applications***. Por otro lado, las ***elastic applications*** pueden funcionar con cualquier *throughput* que obtengan.

### Timing

Este tipo de servicio puede tener distintos aspectos. Un ejemplo es el de garantizar que cualquier bit de información que se envía llegue a destino en no más de $t$ tiempo.

### Security

Finalmente, un protocolo puede proveer uno o más servicios de seguridad. Un ejemplo es el de la encriptación y desencriptación de data en la capa de transporte, para asegurarse que los datos viajen protegidos a lo largo de la red. Otro ejemplo puede ser el de proveer **end-point authentication.**

## Transport Services Provided by the Internet

El internet usa principalmente dos protocolos de transporte. ***UDP*** y ***TCP***.

### TCP Services

Este modelo de servicio incluye un servicio orientado a conexiones y envío confiable de información.

Este protocolo consiste en un intercambio inicial de información antes de que los mensajes de aplicación se envíe, conocido como el ***handshaking procedure***. Una vez finalizada esta fase, se dice que existe una conexión ***TCP*** entre los ***sockets*** de ambos ***end points***. Esta conexión permite tanto el envío como la recepción de mensajes.

Por otro lado, provee un servicio de envío confiable, que asegura que todos los paquetes enviados llegaran a destino en el orden correcto.

Por último, TCP posee un mecanismo de control de congestión, un servicio para el bienestar de internet, más que un cliente en particular.

Si bien este protocolo no ofrece encriptación, se puede utilizar el protocolo ***SSL Secure Sockets Layer*** para enviar mensaje encriptados. Este protocolo está construido encima de ***TCP,*** por lo que no se considera una protocolo de transporte en sí, sino una mejora de ***TCP***.

### UDP Services

Este protocolo es un protocolo de transporte minimalista. No ofrece ningún servicio ni garantía. Los mensajes pueden incluso llegar en desorden. Tampoco ofrece un mecanismo de control de congestión.

Las aplicaciones de telefonía a través de internet, como ***Skype***, suelen utilizar este protocolo. Pueden tolerar cierta perdida de información.

### Services Not Provided by Internet Transport Protocolos

Ninguno de los dos protocolos mencionados provee el servicio de ***throughput*** o **timing.** Esto es así porque no existe ningún protocolo que los provea. Las aplicaciones fueron desarrolladas para que puedan funcionan sin este tipo de garantía, utilizando técnicas alternativas.

## 5. Application-Layer Protocols

Estos protocolos definen los tipos de mensajes intercambiados, su sintaxis, la semántica de sus campos, y las reglas que determinan el flujo de la comunicación.

Algunos protocolos son de dominio público, especificados en los ***RFCs,*** mientras que otros pertenecen a organismos propietarios.

Es importante distinguir una aplicación de red de un protocolo de aplicación. Un protocolo es una pieza de una aplicación de red, la cual a su vez incluye más componentes. Igualmente, en esta materia nos referimos a los protocolos como aplicaciones de red.
