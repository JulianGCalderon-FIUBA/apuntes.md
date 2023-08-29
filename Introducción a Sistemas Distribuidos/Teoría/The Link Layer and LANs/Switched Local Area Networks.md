Debido a que los *switches* operan en la capa de enlace, lidian con *link-layer* *frames* en lugar de *network-layer datagrams*. En lugar de direcciones IP, tienen dirección de capa de enlace

## 1. Link-Layer Addressing and ARP

### MAC Addresses

Todos los adaptadores de hosts (interfaces de red) contienen una dirección propia de capa de enlace, esto no es así para los routers, los cuales no contienen direcciones de capa de enlace.

Estas direcciones son conocidas por varios nombres, como *LAN address*, *physical address*, o *MAC address*.

Típicamente, las direcciones MAC son anotadas en notación hexadecimal

Debido a que las direcciones MAC son manejadas por el IEEE, no existen dos direcciones MAC iguales en todo el mundo (en teoría). Además, estas direcciones son física e independientes de la localización (no tienen una jerarquía como las direcciones IP).

Cuando un adaptador quiere enviar un paquete a otro dispositivo, ocasionalmente el *switch* realizará un *broadcast* a todos los hosts de la red. Los hosts entonces inspeccionarán el paquete y lo descartarán si no fue dirigido para ellos.

A veces un adaptador quiere enviar un paquete a toda la red, en tal caso se utiliza la **MAC broadcast address**.

### Address Resolution Protocol

Debido a que existen tanto direcciones IP como direcciones MAC, existe una necesidad de traducir entre ellas. Para esto se utiliza el **Address Resolution Protocol (ARP)**.

Este protocolo es similar al DNS, pero con la salvedad de que ARP únicamente resuelve direcciones IP de los hosts y las interfaces que pertenecen a la misma *subnet.*

Todos los hosts tienen una tabla ARP que contiene *mapeos* entre direcciones IP y MAC. Además, las entradas de la tabla contienen un campo TTL para definir cuanto actualizar el valor, debido a que los *mapeos* no son permanentes.

Cuando un host quiere definir una dirección MAC, el adaptador enviara un paquete ARP conteniendo la petición y la enviara en *broadcast* a toda la subred.

Los hosts que contiene la dirección IP referida enviara en respuesta un paquete conteniendo el mapeo solicitado. La respuesta no se enviará en un paquete *broadcast*, sino dirigido al que realizo la petición.

Las tablas son configuradas automáticamente *(plug and play)* y no deben mantenidas por un administrador de red.

Este es un protocolo que se encuentra entre la capa de red y la capa de enlace, ya que contiene información relacionada con ambas capas.

### Sending a Datagram off the Subnet

Cuando enviamos un paquete a través de múltiples routers hacia un destino externo, debemos incluir la dirección MAC del router inmediato *(next hop)*. Si incluimos la dirección MAC del host de destino, ningún adaptador de la red tomará el paquete y este será descartado. Para conocer la dirección IP del próximo router inmediato, se utiliza el protocolo ARP.

## 2. Ethernet

Hoy en día, Ethernet es por lejos la tecnología de LAN con cable más prevalente en el mundo. Esta fue una tecnología más barata y simple que las otras hasta el momento, pero que ofrecía tasas de velocidad similares.

En los 90, las instalaciones de Ethernet utilizaban una topología de estrella *hub-based*. Un *hub* era un dispositivo intermedio entre el resto de dispositivos que ampliaba e intensificaba lo que recibía por cada interfaz y lo reenviaba al resto de interfaces. A partir de los 2000, se cambió el *hub* por un **switch**, pero continuaba siendo una topología de estrella. Los *switches* eran *collision less* y un *store-forward* *packet switch*.

Ethernet provee un servicio *connectionless* y no confiable a la capa de red. No se envía ningún tipo de *acknowledgments* positivos ni negativos, ni siquiera ante la corrupción de bits. La falta de confiabilidad es lo que le permite a Ethernet ser barato y simple.

### Ethernet Frame Structure

Los *Ethernet frames* tienen 6 campos:

- **Data Field (46 to 1500 bytes):** El MTU de Ethernet es de 1500, por lo cualquier paquete de mayor tamaño deberá ser fragmentado. Además, el mínimo tamaño de un *frame* es de 46 bytes, por lo que en caso de ser menor debe ser rellenado antes de ser enviado, para eliminarse utilizando el campo de *length*.
- **Destination Address (6 bytes):** Este campo contiene la dirección MAC del adaptador de destino.
- **Source Address (6 bytes)**: Este campo contiene la dirección MAC del adaptador de envío
- **Type Field (2 bytes):** Debido a que la capa de enlace debe poder manejar múltiples protocolos de red, se utiliza este campo para indicar a qué protocolo debe ser entregado en el adaptador de destino
- **Cyclic Redundancy Check (CRC) (4 bytes):** Como mencionado anteriormente, es utilizado para detectar errores
- **Preamble (8 bytes):** Son utilizados para despertar y sincronizar los relojes de los adaptadores. Tienen un valor fijo y utilizado durante todo el protocolo.

### Ethernet Technologies

Las versiones del protocolo tienen nombres determinados por sus características, como 10BASE-2, 100BASE-T, 1000BASE-LX, entre otros.

La primera parte indica la velocidad de transmisión del estándar, la segunda parte indica que funciona para *baseband Ethernet*, mientras que la última parte refiere al medio físico utilizado. 'T' refiere particularmente a los *twisted-pair copper wires*.

En los protocolos iniciales, Ethernet estaba limitado a cables de longitud máxima, debido a esto se utilizaban repetidores, dispositivos de capa física que únicamente reciben una señal y la reproducen (amplifican).

A lo largo de los años, Ethernet cambio mucho. Hoy en día la mayoría de las conexiones son punto a punto utilizando *twisted-pair copper wires* o *fiber-optic cables.*

Gigabit Ethernet es una extensión a los altamente exitosos 10 mbps y 100 mbps estándares de Ethernet, ofreciendo tasas de 40 GB.

- Utiliza el formato de *frames* estándar de Ethernet y es compatible con las tecnologías *10BASE-T* y *100BASE-T*.
- Permite tanto enlaces punto a punto como canales compartidos (los puntos a punto utilizan *switches* mientras que los compartidos utilizan *hubs*
- Utiliza *CMSA/CD* para medios compartidos (la máxima distancia entre nodos es limitada para maximizar eficiencia)
- Permite una operación **full-duplex** de *40gb* en ambas direcciones.

Ethernet era inicialmente una tecnología de enlace de *broadcast*, pero para resolver las colisiones, se introdujo el protocolo **CSMA/CD** y las conexiones punto a punto. Debido a que hoy en día se utilizan principalmente conexiones punto a punto con topologías de estrella con un *store-forward switch*, las direcciones *MAC* son casi no utilizadas.

## 3. Link-Layer Switches

Los *switches* son transparentes. Los adaptadores de red direccionan *frames* directamente a otros hosts de la subred, sin conocer los *switches intermedios*. La tasa de llegada puede ser mayor a la tasa de salida, por lo que los *switches* utilizan buffers para no descartar información

### Forwarding and Filtering

**Filtering** es la función que se encarga de determinar si un *frame* debe ser enviado a alguna interfaz o descartado. **Forwarding** es la función que determina a qué interfaz debe ser redireccionado cada *frame*.

Vemos tres posibles escenarios en la llegada de un *frame:*

- No hay una entrada en la tabla para la dirección especificada, en ese caso el *switch* envía el paquete a todas las interfaces excepto a la de llegada.
- Hay una entrada en la tabla asociada la dirección especificada, pero esta interfaz coincide con la interfaz de llegada, en ese caso el *switch* realiza la función de *filtering* y descarta el paquete.
- Hay una entrada en la tabla asociada a la dirección especificada y es distinta a la de la interfaz de llegada, en ese caso el *switch* realiza la función de *forwarding* y reenvía el paquete a la interfaz determinada.

### Self-Learning

Para configurar la tabla del *switch*, se utiliza un mecanismo de autoaprendizaje:

1. La tabla inicialmente estará vacía
2. Por cada *frame* que recibe, almacena en su tabla la dirección MAC del remitente del *frame* con la interfaz de llegada.
3. El *switch* elimina automáticamente una tabla si no recibe paquetes de esa dirección en un tiempo determinado.

Debido a estas reglas, los *switches* son dispositivos *plug-and-play*, ya que no requieren intervención del administrador de red o del usuario.

### Properties of Link-Layer-Switching

Podremos identificar múltiples ventajas de los *switches* por sobre las topologías **hub-based**

- **Eliminación de colisiones:** Debido a que las conexiones son punto a punto y los *switches* manejan el intercambio de información, no hay colisiones entre los paquetes. Nunca se envía más de un *frame* a la vez a través de un determinado enlace.
- **Links Heterogéneos:** Como los *switches* aíslan unos enlaces de otros, los diferentes links pueden operar a diferentes velocidades e incluso en distintos medios.
- **Manejo:** Además de proveer seguridad avanzada, los *switches* también facilitan el manejo de la red. Por ejemplo, si un adaptador falla y empieza a mandar paquetes continuamente, el *switch* puede detectar esto y desconectar internamente el adaptador fallado. Por otro lado, si un cable se desconecta, solo se perjudica aquel host conectado con ese enlace.

### Switches Versus Routers

Tanto los *switches* como los routers realizan **store-and-forward packet switching**, pero tienen diferencias fundamentales. Los routers operan con direcciones de capa de red, mientras que los *switches* operan con direcciones de capa de enlace.

Como vimos anteriormente, también existen dispositivos con estándar *OpenFlow* que utilizan la operación **match plus action** para funcionar como ambos (examinan 11 *headers* de distintas capas).

Un administrador debe decidir entre cuál de estos dispositivos utilizar para gestionar su red. Veremos algunas ventajas y desventajas de los *switches*.

- Los *switches* tienen tasas de filtrado y envío relativamente altas, ya que solo deben procesar *frames* hasta la capa de enlace
- Para prevenir envíos de *broadcast* cíclicos, la topología está limitada a un *spanning tree (grafo conexo acíclico)*
- Una gran red necesitaría grandes tablas de ARP y esto generaría un gran número de tráfico y procesamiento de ARP.
- Los *switches* son susceptibles a *broadcast storms*.

Por el otro lado, analizaremos algunas ventajas y desventajas de routers.

- Debido a que las estructuras son jerárquicas, los paquetes no atraviesan ciclos a lo largo del recorrido (a menos que haya una tabla mal configurada)
- Las redes no están restringidas a un *spanning tree* y pueden utilizar el mejor camino entre dirección de envío y dirección de destino.
- Debido a que las redes no están restringidas a un *spanning tree*, se pueden construir topologías complejas y de alta eficiencia
- Proveen protección de *firewall* ante ataque de *broadcast* de capa de enlace.
- No son *plug-and-play*, y requieren ser configurados por los administradores de red
- Usualmente tienen mayor tiempo de procesamiento por paquete que los *switches*.

En general, para redes pequeñas, los *switches* suelen ser suficientes. A medida que crece el tamaño de nuestra red, nos resultara conveniente optar por la utilización de routers.

## 4. Virtual Local Area Networks (VLAN)

Usualmente, las redes *switched LAN* son configuradas jerárquicamente, donde cada grupo contiene su propia *switched LAN* que es a su vez conectada con otros grupos a través de una jerarquía de *switches.* Podemos identificar tres inconvenientes principales de esta configuración:

- **Lack of Traffic Isolation:** Aunque las jerarquías localizan el tráfico del grupo en un único *switch*, el tráfico de *broadcast* debe aún recorrer toda la red completa. Limitar este tráfico incrementaría el rendimiento de la red. Para solucionar esto podríamos reemplazar el *switch central* (que conecta los *switches* de los distintos departamentos) con un router.
- **Inefficient use of Switches:** Si aumenta el número de grupos, pero se reduce el número de hosts por grupo, estaremos ante una situación donde o bien podríamos tener muchos *switches* y tener un uso ineficiente de los mismos, o bien tener un único *switch* pero sin proveer aislamiento de tráfico.
- **Managing Users:** Si un empleado se mueve de un grupo al otro, se debe modificar el cableado físico para reflejar este cambio en la red.

Afortunadamente, estas dificultades pueden ser resueltas utilizando un **Virtual Local Area Network (VLAN)**. Un *switch* que permite VLAN permite que múltiples VLAN sean definidas por sobre una única LAN física. En una *port-based VLAN*, los puertos del *switch* central son distribuidos entre los distintos grupos por el administrador de red (cada puerto es asociado a una VLAN distinta).

- Cuando se realiza un *broadcast*, el *switch* limita el *broadcast* a únicamente los puertos de ese grupo
- Podremos agrupar todos los *switches* en un solo *switch* central, separando los grupos virtualmente
- Si un empleado se mueve a otro grupo, simplemente debe reconfigurar a qué grupo está asociado su puerto designado en el *switch*.

Al aislar completamente los grupos, nos encontramos con un nuevo problema. Para resolverlo, se puede conectar un puerto de *switch* a un router externo y configurar para que este puerto este asociado a todos los grupos. De esa forma, para enviar un paquete entre dos grupos, deben pasar primero por el router externo antes de ser dirigido a otro grupo. Afortunadamente, existen dispositivos que contienen internamente un *VLAN switch* como un router.

¿Qué pasa si los dos grupos están situados en distintos edificios? En ese caso se utiliza la técnica de **VLAN trunking**. Se designa un puerto, en especial en cada *switch*, asociado con todos los grupos, que se utilizara para conectar ambos *switches*. Cuando se quiere enviar un paquete a un grupo externo, se enviara a este puerto, el cual utilizará el *VLAN tag* (campo del *header* de Ethernet) para determinar a qué grupo reenviar el paquete.

En las **MAC-based VLAN**, el administrador de red especifica que conjunto de direcciones MAC le pertenecen a cada grupo. También se permite que las redes VLAN se extiendan entre routers de IP, permitiendo islas de LAN interconectadas a través del mundo.
