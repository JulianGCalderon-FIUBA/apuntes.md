Existen dos versiones de **IP**. Primero examinaremos la conocida versión del protocolo, usualmente referida como ***IPv4***.

## 1. IPv4 Datagram Format

Los campos clave de un datagrama ***IPv4*** son:

- ***Version number:*** Especifican la versión del protocolo **IP** del ***datagram***
- ***Header length:*** Debido a que el datagrama puede contener un número variable de opciones, este campo determina dónde comienza el ***payload.***
- ***Type of service:*** Permiten distinguir los paquetes según el tipo de servicio que ofrecen, permitiendo a las redes detectar paquetes de tiempo real del resto.
- ***Datagram length:*** Incluye el tamaño total del ***datagram***, medido en ***bytes***.
- ***Identifier, flags, fragmentation offset:*** Estos tres campos son utilizados en el conocido ***IP fragmentation***.
- ***Time-to-live:*** Se usa para indicar cuándo tiempo podrá circular un ***datagram*** en la red, este número es decrementado por cada ***router*** que atraviesa el ***datagram***.
- ***Protocol:*** Este campo es típicamente utilizado una vez el paquete llega a destino, para determinar que protocolo de capa de transporte específico se está utilizando.
- ***Header checksum:*** Permite al router detectar errores a nivel de ***bit*** dentro del paquete. El segmento es tratado como un arreglo de números de dos bytes y sumandolos con complemento a uno. Este valor deberá ser recalculado y actualizado luego de cada ***router***, ya que usualmente se actualizan valores (como el TTL)
- ***Source and destination ***IP addresses:*** Cuando una fuente crea un datagrama, inserta la dirección de destino y de origen para que el internet conduzca el paquete correctamente.
- ***Options:*** Se utilizan raramente y permiten que el protocolo **IP** se extienda.
- ***Data:*** Este campo contiene el segmento de capa de transporte que debe ser entregado a destino.

### 2. IPv4 Datagram Fragmentation

No todos los protocolos de capa de enlace permiten llevar paquetes del mismo tamaño. La máxima cantidad de información que puede ser enviado a través de un ***link-layer frame*** se conoce como ***maximum transmission unit (MTU).***

La solución es fragmentar el ***payload*** de un ***IP datagram*** en múltiples pequeños *datagrams*, referidos como *fragments.* Estos fragmentos serán enviados a través de la red para únicamente ser reensamblados en el ***destination host***.

Cuando un ***destination host*** recibe una serie de ***datagrams*** de una misma fuente, debe determinar si alguno de todos esos ***datagrams*** proviene de un ***datagram*** original de mayor tamaño. Cuando un ***datagram*** es creado, el remitente estampa el paquete con un número de identificación, el cual se incrementa con cada paquete enviado. Cuando un ***router*** fragmenta un paquete, coloca el mismo número de identificación en todos los fragmentos. Para indicar que un fragmento es el último de un paquete, se utiliza el ***flag bit*** (establecido en 0). Para indicar el orden de los fragmentos, se utiliza el campo ***offset (***el cual se incrementará de fragmento a fragmento). A partir de esta información, el ***host*** de destino puede construir los ***datagrams*** a partir de los segmentos y entregarlos a la capa de transporte.

## 3. IPv4 Addressing

Un ***host*** típicamente tiene un único enlace para conectarse a la red. Cuando el protocolo de red del ***hosts*** quiere enviar un ***datagram,*** lo hace a través de este ***link***. La frontera entre el ***host*** y el enlace es conocida como ***interfaz***. La frontera entre un ***router*** y cualquiera de sus ***links*** también se conoce como ***interface***. Un ***router*** entonces puede tener múltiples interfaces, cada una con un ***link***. El protocolo **IP** requiere que cada una de estas interfaces tenga su propia dirección.

Cada dirección *IP* tiene un tamaño de 32 bits y está anotado en ***dotted-decimal notation***. Cada byte está separado por un punto y escrito en notación decimal. Una porción de la dirección IP de una interfaz estará determinada por la ***subnet*** a la cual está directamente conectada.

Para determinar una ***subnet***, se desconectan todas las interfaces de su host o ***router*** asociado, creando islas aisladas llamadas ***subnets***.

La estrategia de asignamiento de direcciones de internet se conoce como ***Classless Interdomain Routing (CIDR)***. La dirección **IP** se divide en dos secciones y tiene la forma `a.b.c.d/x`, donde `x` indica el número de ***bits*** en la primer parte de la dirección. Esta sección es conocida como el prefijo.

Una organización suele ser asignado un rango de conexiones con un prefijo común. Fuera de la organización, únicamente se utilizarán los ***bits*** del prefijo para enviar el paquete. Esto reduce considerablemente el tamaño de las ***forwarding tables***. Los restantes ***bits*** serán usados dentro de la organización para distinguir las direcciones **IP,** es posible que los ***bits*** restantes a su vez estén organizados en otras estructuras de **subredes**.

La habilidad de utilizar un único prefijo para anunciar múltiples redes se conoce como ***address aggregation***.

La ***IP de*** broadcast `255.255.255.255` es utilizada cuando un host quiere enviar un mensaje a todos los ***hosts*** de la misma ***subnet***.

### Obtaining a Block of Addresses

Para obtener un bloque de direcciones **IP**, un administrador de red puede comunicarse con su ***ISP***, el cual puede proveer direcciones de un gran bloque de direcciones ya reservado para el ISP. A nivel mundial, las direcciones **IP** están manejadas detrás de la autoridad de **Internet Corporation for Assigned Names and Numbers (ICANN)**. El rol de esta organización sin fines de lucro no es solo reservar direcciones **IP**, sino también manejar los servidores raíz ***DNS***. Esta organización reserva direcciones para los registros de internet regionales.

### Obtaining a Host Address: The Dynamic Host Configuration Protocol

Una vez la organización obtiene un bloque de direcciones, puede asignarlas individualmente a las interfaces de la organización. Un administrador de red puede configurar manualmente la direcciones de los routers, pero también puede configurar manualmente las direcciones de los ***hosts*** a partir del protocolo ***Dynamic Host Configuration Protocol (DHCP)***

Este protocolo permite a un ***host*** obtener una dirección **IP** automáticamente. Un administrador de red puede configurar el protocolo para que reciba la misma dirección cada vez que se conecta, o que asigne direcciones ***IP*** temporales que serán distintas para cada conexión.

Debido a la habilidad de automatizar la conexión de ***hosts*** en una red, este protocolo suele ser referido como ***plug-and-play*** o ***zeroconf***. Esto permite que los usuarios móviles puedan acceder a internet de forma automática al conectarse a una nueva red.

El protocolo ***DHCP*** tiene una arquitectura cliente servidor. En el caso más simple, cada ***subnet*** tiene su propio ***DHCP server*** o un ***relay agent*** (típicamente un ***router***) que conoce la dirección del ***DHCP*** server. Este protocolo es un proceso de cuatro pasos:

1. ***DHCP server discovery:*** El ***host*** recién llegado envía un ***DHCP discover message*** dentro de un paquete ***UDP*** al puerto `67`, usando la dirección de destino ***broadcast `255.255.255.255`, y la dirección de fuente `0.0.0.0`.*
2. ***DHCP server offer(s):*** El servidor responde al cliente con un ***DHCP offer message***, nuevamente con la dirección de destino ***broadcast***. Debido a que múltiples servidores *DHCP* son permitidos, el cliente a veces tiene la opción de elegir entre varias ofertas. Este mensaje contiene la **ID** de transacción del ***discover message***, la dirección **IP** propuesta para el cliente, la máscara de red y la ***address lease time*** (el tiempo durante el cual la dirección es válida
3. ***DHCP request:*** El cliente elige la oferta deseada y envía un ***DHCP request message***, con la configuración recibida.
4. ***DHCP ACK:*** El servidor responde con un ***DHCP ACK message***, confirmado los parámetros.

Una vez terminado el proceso, el ***host*** podrá usar la **IP** durante un tiempo determinado. Debido a que muchas veces el ***cliente*** querrá usar la dirección más allá del tiempo predefinido. ***DHCP*** provee un mecanismo para renovar el alquiler de la dirección **IP**.

Debido a que una dirección **IP** nueva es obtenida cada vez que el nodo se conecta a una nueva ***subnet***, no es posible mantener una conexión ***TCP*** a medida que el ***nodo*** atraviesa múltiples ***subnets***.

## 4. Network Address Translation (NAT)

Para enviar paquetes a través de la red local, se utiliza la dirección de subnet `10.0.0/24`. Esta es una de las tres porciones de direcciones **IP** reservadas para redes privadas o reinos de direcciones privadas. Un reino de direcciones privadas refiere a una red cuyas direcciones solo tienen significado a los dispositivos dentro de esa misma red.

Un ***NAT-enabled*** ***router*** luce, ante el mundo exterior, como un único dispositivo con una única dirección **IP**. Este esconde los detalles de la red interna del mundo exterior. Para decidir a que dispositivo de la red enviar los paquetes entrantes, se utiliza una ***NAT translation table***.

Veamos el escenario en el que un ***host*** quiere conectarse con un servidor *web.* Cuando el host crea un socket en un puerto arbitrario y envía el datagrama a la red local, el router NAT recibe el datagrama, genera un nuevo puerto local para este datagrama y reemplaza la dirección de fuente con la dirección publico router y el nuevo puerto. También, genera una entrada en la tabla para corresponder el nuevo puerto con el ***host*** *local* y puerto indicado. Cuando el router ***NAT*** recibe la respuesta del servidor, indexa en la tabla para descubrir a que dirección local debe enviar este paquete.

Algunos pueden argumentar que los números de puerto deben ser utilizados para indexar procesos y no ***hosts*** (y a su vez sus procesos). Esto puede traer problemas, por ejemplo, a la hora de bindear servidores a puertos conocidos. Para solucionar esto, se utilizan las herramientas de ***NAT traversal*** y *Universal Plug and Play (UPnP),* un protocolo que permite a un host descubrir y configurar un NAT cercano.

Los más puristas de la arquitectura argumentan que un router debería ser de capa de red y no debería interferir con los paquetes, mucho menos sus números de puertos. Se quiera o no, NAT es un componente importante del internet así como otros llamados ***middleboxes***. Las middle boxes no realizan envío de datagramas tradicional, sino que realizan funcionan funciones como ***NAT, load balancing***, ***traffic firewalling***, y más.

Existen dos mecanismos populares como defensa de ataques de paquetes maliciosos. Los ***firewalls*** los ***intrusion detection systems (IDs)***. Un ***firewall*** inspecciona los datagramas y los ***header*** ***fields***, denegando información sospechosa que pueda entrar a la red. Los ***firewalls*** pueden también bloquear paquete basados en las direcciones de destino y origen. Incluso, pueden ser configurados para registrar conexiones ***TCP***, permitiendo que únicamente los paquetes provenientes de conexiones aprobadas entren a la red.

Un ***IDS*** usualmente está situado en el borde de la red e inspecciona profundamente los paquetes, examinando no solo los headers sino el ***payload***. Utiliza una base de datos de paquetes que pueden formar parte de un ataque, esta base de datos se actualiza automáticamente a medida que paquetes son descubiertos. Si se encuentra una coincidencia, se crea una alerta. Un ***intrusion prevention system (IPS)*** es similar, ya que además de crear alertas, bloquea los paquetes.

## 5. IPv6

La motivación para el desarrollo de las dirección ***IPv6*** es la realización de que el espacio de direcciones de ***IPv4*** se estaba utilizando. Los desarrolladores tomaron esta oportunidad para mejorar algunos aspectos de ***IPv4***, basados en la experiencia ganada por ***IPv4:***

- **Expanded addressing capabilities:** Se aumenta el tamaño de una dirección **IP** de 32 bits a 128 bits. Ahora cada grano de arena del planeta puede tener una dirección única.
- ***Streamlines 40-byte header:*** Algunos campos de **IPv4** fueron eliminados o marcados como opcionales, disminuyendo el tamaño del header fijo a ***40 bytes***.
- ***Flow labeling:*** Permite etiquetar los paquetes como proviniendo de un flujo particular al cual el remitente pide un manejo especial, como servicio de calidad no por defecto o un servicio en tiempo real.

Se definen entonces, los siguientes campos:

- **Versión:** Este campo de 4 bits identifica el número de versión **IP**. Para la *IPv6* se utiliza el valor 6.
- ***Traffic class:*** Este campo de 8 bits es usado para dar más prioridad a ciertos datagramas dentro de un flujo.
- ***Flow label:*** Campo de 20 bits que permite identificar un flujo de ***datagrams***.
- ***Payload length:*** Valor de 16 bits que muestra el tamaño en bytes del payload del paquete.
- ***Next header:*** Identifica el protocolo al cual los datos del paquete serán entregados (por ejemplo, a TCP o UDP).
- ***Hop limit:*** Indica la cantidad de saltos que permite el paquete. Por cada ***router*** que atraviesa se reduce en uno el número, hasta finalmente descartar el paquete.
- ***Source and destination addresses:*** Direcciones de origen y destino en formato ***IPv6***. (*128 bits*)
- ***Data:*** El payload del paquete ***IPv6***.

Notamos que algunos ***headers*** ya no están presentes:

- ***Fragmentation/Reassembly:*** El protocolo no permite fragmentación y desfragmentación en los ***routers*** intermediarios. Esta operaciones únicamente pueden ser en el destino o en el origen. Si se recibe un paquete ***IPv6*** demasiado grande como para ser reenviado, entonces se ignora y se envía el mensaje de error ICMP ***"Packet Too Big"*** al remitente. Esto permite que el envio sea mas rapido, ya que esta era una tarea costosa.
- ***Header Checksum:*** Debido a que la capa de transporte y la de enlace ya realizan estos chequeos, los diseñadores decidieron que esta funcionalidad es redundante y que podía ser removida. El interés principal era la velocidad del protocolo.
- ***Options:*** El campo de opciones ya no esta disponibles, en su lugar, se utiliza el campo ***Next***.

### Transitioning from IPv4 to IPv6

El problema es que mientras que los sistemas ***IPv6*** son ***backward-compatible***, los sistemas ***IPv4*** no soportan el envío de datagrams ***IPv6***. La mayoría de los sistemas utilizan ***IPv4*** y la transición es un proceso muy costoso.

Para solucionar esto se utiliza la estrategia de ***tunneling.*** Esta estrategia consiste en que si dos nodos ***IPv6*** se quieren comunicar a través de una serie de ***routers*** que implementan únicamente ***IPv4***, entonces el paquete se encapsula dentro de un paquete IPv4. Este es enviado a través de los routers intermedios hasta que llegan al otro nodo ***IPv6***, el cual extrae el paquete IPv6 del payload del paquete ***IPv4***. Para identificarlo, observa el valor *41* en el campo del número de protocolo.

Introducir protocolos de aplicación es mucho más simple de realizarse, en comparación con la introducciones que nuevos protocolos de transporte, lo cual es muy costoso de realizarse.
