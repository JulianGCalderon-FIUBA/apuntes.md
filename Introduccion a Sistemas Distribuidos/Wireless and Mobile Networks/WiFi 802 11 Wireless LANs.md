---
title: WiFi 802 11 Wireless LANs
---

A lo largo de los años, se desarrollaron muchas tecnologías y estándares de redes ***LAN*** inalámbricas, la clase mas utilizada es la de standards 802.11, o ***Wi-Fi***.

Existen muchos estándares para esta clases, todos ellos comparten algunas características comunes. Todos utilizan el mismo protocolo de acceso al medio, ***CSMA/CA.*** Todos reducen su tasa de transmisión para llegar a mayores distancias, y todos son ***backwards compatible***. La mayor diferencia, radica en la capa física.

Existen dos rangos frecuencias principales, ***2.4*** y ***5.8***. Las redes ***5.8*** tienen menor rango para un nivel de potencia dado, y sufren más de propagación ***multipath***. Los estándares mas recientes utilizan multiples antenas (tanto receptoras como emisoras), y utilizan antenas inteligentes para direccionar las mismas en dirección del receptor. Esto redujo la interferencia e incremento la distancia alcanzada para una tasa dada.

## 1. The 802.11 Architecture

El bloque fundamental de construcción de la arquitectura de 802.11 es el ***basic service set (BSS).*** Este contiene una o mas estaciones inalámbricas, y una estación base central, conocida como ***access point (AP).*** En una red típica de hogar, hay un **AP** y un ***router,*** típicamente integrados en la misma unidad.

Las redes ***LAN*** inalámbricas que despliegan un ***access point*** son frecuentemente referidas como ***infrastructure wireless LANs***. Las estaciones, a su vez, pueden concentrase con otras estaciones formando una red descentralizada ***(ad hoc).***

### Channels and Association

Cuando un administrador de red instala un ***access point***, deben configurarse dos parámetros. El ***Service Set Identifier (SSID),*** y el numero de canal. Las redes de *2.4GHz operan entre 2.4GHz y 2.4835Ghz*, definiendo *11* canales parcialmente superpuestos. Dos canales no se superponen si distan a 4 o mas canales.

Una jungla ***Wi-Fi*** es una cualquier punto donde se reciben suficientemente fuertes, señales de dos o mas ***access points***. Cuando un dispositivo se encuentra en una jungla, para obtener acceso al internet, debe asociarse con exactamente uno de estos AP**s.** Asociarse implica crear un cable virtual entre el y dicho **AP**.

Para que los dispositivos conozcan a un dado **AP**, este periódicamente envía ***beacon frames***, que incluyen el ***SSID*** de la red y una ***MAC*** address. El dispositivo, escanea los 11 canales para hallar las direcciones *Wi-Fi cercanas.* Este proceso se conoce somo *passive scanning*. ***Un dispositivo también puede realizar ***active scanning***, al enviar un ***probe frame*** que será recibido por todos los access points en el rango. Los access points responderán con un probe request frame.

Una vez seleccionado el **AP** al cual desea conectare, enviara un ***association request frame*** a dicho **AP**. Este responderá con un ***association response frame***. Este intercambio es necesario incluso tras un escaneo activo, debido a que los **AP**s no saben con cual **AP** deseara conectarse, luego del escaneo. Una vez recibida la confirmación, el dispositivo puede pedir una dirección **IP** utilizando el protocolo ***DHCP***.

En algunas situaciones, un ***host*** necesitará autenticarse para crear una conexión. Existen diversas formas de realizarlo. Un enfoque podría ser utilizando la dirección ***MAC*** del dispositivo, otro enfoque, mas utilizado, podría ser la utilización de usuarios y contraseñas. En general, esta autenticación se realiza a partir de un servidor de autenticación, con el protocolo ***RADIUS***.

## 2. The 802.11 MAC Protocol

El protocolo de acceso al medio utilizado por ***Wi-Fi*** es el protocolo **carrier sends multiple access with collision avoidance (CSMA/CA)**. Este difiere del protocolo de ***ethernet CSMA/CD*** en algunos aspectos. En primer lugar, en lugar de *collision detection*, ***802.11*** utiliza ***collision avoidance***. En segundo lugar, ***802.11*** utiliza una técnica de capa de enlace de ***acknowledges/retransmisiones.*** (ARQ).

Hay dos razones principales por las cuales, 802.11 no implementa ***collision detection***.

- La habilidad de detectar colisiones requiere de la habilidad de enviar y recibir al mismo tiempo. Esto es muy dificil para las redes inalámbricas debido a que la señal recibida es mucho menor de la señal emitida.
- Incluso si el adaptador pudiese enviar y recibir al mismo tiempo, el adaptador podría incluso no detectar colisiones debido a los problemas ya mencionados, ***hidden terminal problem*** y ***fading***.

Una vez que una estación comienza a transmitir, lo transmite completo. Esto puede ocasionar que en situaciones con muchas colisiones, se reduzca significativamente el rendimiento del protocolo. Luego, el protocolo buscara evitar a toda costa las colisiones.

Si un dispositivo quiere enviar un ***frame***, entonces escuchara el canal. Si no hay nadie transmitiendo, lo transmite. Si hay alguien transmitiendo, elige un valor aleatorio de ***backoff*** utilizando ***binary exponential backoff*** y comienza la cuenta regresiva (contando únicamente cuando el canal esta vacío luego del ***DIFS***). Una vez que la cuenta finaliza, envía el ***frame***.

Cuando un estación recibe un paquete completo, espera un pequeño periodo de tiempo llamado Short Inter-Frame Spacing (SIFS) y luego reenvía un ack. Si el remitente no recibe el ***ack*** en un periodo determinado, entonces entra en la siguiente etapa de ***exponential backoff*** y elige un valor aleatorio mayor para el intervalo.

### Dealing with Hidden Terminals: RTS and CTS

El protocolo incluye un opcional esquema de reservación para evitar colisiones en presencia de ***hidden*** terminals*.* Para evitar este problema el protocolo define la utilización de un pequeño ***frame*** de control ***Request to Send (RTS)*** y otro ***Clear to Send (CTS)***.

Cuando un dispositivo quiere enviar información, primero envía un frame ***RTS*** al **AP** indicando el tiempo total requerido para la transmisión (tanto de los datos como del ***ack***). Cuando el **AP** lo recibe, reenvía un ***CTS*** frame. Este le indica al dispositivo que puede enviar el paquete, y al resto de dispositivos que deben esperar un tiempo determinado.

Esto soluciona el problema de la terminal oculta, y limite las colisiones a los ***frames*** ***RTS*** y ***CTS***, que son cortos. Por otro lado, introduce retrasos y consume recursos del canal. Debido a esto, solo es utilizado para el envío de paquetes largos. En muchas situaciones, incluso no es utilizado.

### Using 802.11 as a Point-to-Point Link

Si dos nodos tienen antenas direccionales, pueden apuntar las antenas entre si y utilizar para una comunicación barata, incluso a grandes distancias.

## 3. The IEEE 802.11 Frame

Aunque comparte muchas similitudes con el ***Ethernet frame***, tiene campos específicos para el uso de enlaces inalámbricos.

### Payload and CRC Fields

El ***payload*** de frame contiene el datagrama de **IP** o un paquete ***ARP***. Típicamente, tiene una longitud menor a ***1500*** ***bytes***. Al igual que el ***ethernet frame***, contiene un ***32-bit cyclic redundancy check (CRC)***.

### Address Fields

A diferencia de ***ethernet***, se tienen cuatro direcciones ***MAC.*** La primer dirección es la de la estación inalámbrica que recibe el ***frame***. La segunda reacción es la de la estación que envía el ***frame***.

La tercera dirección indica la dirección ***MAC*** del router al cual se le quiere enviar el paquete, una vez llegado a la estación. Recordemos que la ***BBS*** es parte de una subnet que se conecta con otras para ***subnets*** a través de ***routers***. Los routers no conocen la estaciones base intermedias entre el host y ellos, ya que estas no utilizan IP.

La cuarta dirección se utiliza cuando el **AP** le envía ***frames*** a otros en un modo centralizado, pero no nos centraremos en esta infraestructura.

### Sequence Number, Duration, and Frame Control Fields

Debido a la existencia de ***acknowledgments***, los ***frames*** deben contener un numero de secuencia para detectar aquellos paquetes repetidos.

El campo de ***duration*** se utiliza para indicar la duración de la transmisión que queremos solicitar, a través de los ***frames*** ***RTS*** y ***CTS***.

Finalmente, tiene un numero de campos de control, los mas importantes son:

- ***type*** y ***subtype*** se utilizan para distinguir entre ***association, RTS, CST, ACK,*** y los ***data frames***.
- **to** y ***from*** se utilizan para definir el significado de los distintos campos de ***address***.
- *WEP* se utiliza para indicar si se utilizo encriptación o no.

## 4. Mobility in the Same IP Subnet

Para incrementar el rango físico de una red inalámbrica, a veces se despliegan multiples ***BBS*** a través de multiples estaciones. Los dispositivos mobiles muchas veces se mueven a través de multiples ***BBS***. ¿Cómo hacen para mantener una conexión ***TCP*** durante estos cambios de red?

Como las distintas ***BBS*** pertenecen a la misma subred, entonces el dispositivo puede mantener su dirección **IP** a través de las distintas estaciones.

A medida que un dispositivo se va alejando de una estación central, empieza a escanear otras estaciones a las que pueda conectarse. Una vez encuentra otra estación, se asocia con un y se desasocia con la otra.

¿Que ocurre cuando hay un ***switch*** conectado a ambas estaciones centrales? Como estudiamos, los ***switches*** son ***self-learning*** y automáticamente construyen sus tablas de envió. Una solución es que la nueva estación envíe un ***broadcast*** indicándole a la subred del cambio de dirección.

## 5. Advanced Features in 802.11

### 802.11 Rate Adaptation

Como vimos anteriormente, las diferentes técnicas de modulación pueden ser apropiadas para diferentes escenarios de ***SNR***. Si se pierde un paquete, entonces se reduce la tasa de transmisión, pero si se envían correctamente diez paquetes seguidos, entonces esta se aumenta.

Esta técnica utiliza la misma tecnología de ***probing*** que utiliza el control de congestión de ***TCP***.

### Power Management

La energía es un recurso preciado en los dispositivos mobiles, por lo que 802.11 provee formas para permitir que los nodos minimicen el tiempo utilizado en lectura y transmisión.

Un nodo le indica al **AP** que entrara en modo de ***dormido*** enviándole un 1 en un campo especial del *header* de 802.11. Luego, se configura un ***timer*** para despertar al nodo justo antes de que el **AP** le envía un ***beacon frame*** (unos 100ms). El **AP** guardara los frames destinados a este dispositivo hasta que este se despierte, para enviarlos despues.

Una vez se despierta el nodo, recibe de el beacon frame una lista de nodos cuyos paquetes fueron guardados. Si el propio nodo no se encuentra en la lista, puede volver a dormir. Si se encuentra en la lista, entonces puede pedir explícitamente recibir estos paquetes enviando un ***polling message***.

Esto permite que si el nodo no tiene nada para recibir o enviar, el *99%* del tiempo, el nodo este dormido, ahorrando una increible cantidad de energía.

## 6. Personal Area Networks: Bluetooth and Zigbee

Existen dos protocolos en la familia de estándares ***802*** comúnmente utilizados:

### Bluetooth

Es una tecnología de bajo alcance, costo, y consumo de energía. Se utiliza comúnmente para conectar periféricos con una computadora. Estas redes, llamadas 802.15.1, a veces son conocidas como ***wireless personal area networks (WPANs)***.

Operan en el rango de los *2.4Ghz*, con time slots de *625ms*. Durante cada uno de estos ***time*** slots, un remitente envía por uno de los 79 canales, siendo el canal elegido de forma psuedo-aleatoria. Esta forma de cambio de canales se conoce como ***frequency-hopping spread spectrum (FHSS).*** Puede proveer tasas de hasta ***4Mbps***.

Las redes 802.15.1 son ***ad hoc***, sin una infraestructura necesaria para conectar los dispositivos. Primero son organizados en un ***piconet*** desde hasta 8 dispositivos activos. Uno de los dispositivos sera el ***master***, mientras que el resto serán ***slaves***. Los ***masters*** pueden enviar en cada ***time slot*** impar, y los ***slaves*** solo pueden contestar al ***master*** cuando este en el ***slot anterior*** se comunico con ellos. Ademas de estos nodos activos, puede haber hasta *255* dispositivos estacionados que no pueden comunicarse hasta que se les cambie el estado a activo por el master node.

### Zigbee

Una segunda red personal, estandarizado por el ***IEEE***, es el estándar 802.15.4, conocido como ***Zigbee***. Mientras que *bluetooth pr*ovee un replace del cable a una tasa de megabits, el enfoque de esta red es el de una red incluso de menor costo y poder. No todos los dispositivos necesitan altas tasas de transferencia, por lo que este estandar es utilizados en dispositivos pequeños y sin neceisdad de altas tasas de transferencia.

Existen dos tipos de nodos en una red de ***Zigbee***. Los ***reduced-function devices*** operan como esclaves ante el control de un único ***full-function device***. Estos funcionan de forma similar a ***bluetooth***. Ademas, los ***full-function device*** de distintas redes pueden conectarse para formar una red completa donde ***full-function devices*** se envían ***frames*** entre si.

Este protocolo utiliza ***acknowledgements*** similares a los de ***802.11***, y protocolos de ***CSMA*** con ***binary exponential backoff***. Ademas, permite la reserva de ***timeslots*** fijos y garantizados, similar a ***DOCSIS***.

Estas redes dividen al tiempo en ***timeslots*** activos e inactivos. Durante los ***timeslots*** inactivos, todos los dispositivos duermen, para ahorrar energía. Durante los ***timeslots*** activos, se puede enviar información a través de ***CSMA.*** Algunos de los ***timesltos*** serán reservados por el controlador para algunos dispositivos seleccionados.
