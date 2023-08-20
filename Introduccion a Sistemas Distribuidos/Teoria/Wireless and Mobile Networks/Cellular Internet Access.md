---
title: Cellular Internet Access
---

## 1. An Overview of Cellular Network Architecture

Para esta descripción, adoptaremos la terminología de los estándares ***Global System for Mobile Communications (GMS)***. Por lo general, las tecnologías de redes de celular pertenecen a una de varias generaciones.

- La primer generación **1G** era un sistema FDMA diseñado exclusivamente para comunicación por voz.
- Estos fueron reemplazados por sistemas de **2G**, los cuales también eran diseñados para voz, pero en ***2.5G*** se extendieron a soportar la transferencia de datos (internet).
- Los sistemas **3G** también soportan datos y voz, pero con énfasis en voz.
- Las tecnologías 4G es la mas desplegada hoy en día y esta basada en tecnología LTE. Provee transferencia de voz y datos a velocidades de los ***multi-megabit***.

### Cellular Network Architecture, 2G: Voice Connections to the Telephone Network

El termino ***celular*** proviene de que las regiones cubiertas por una red celular se conocen como ***celdas***. Cada celda contiene un ***base transceiver station (BTS**)* que transmite señal desde y hacia las estaciones mobiles dentro de la celda.

![[Cellular Internet Access 1.png]]

El área de cubrimiento de una célula depende de muchos factores, incluyendo el poder de transmisión de la BTS, de los dispositivos de usuario, de los edificios que obstruyen, las antenas, etc.

Los sistemas 2G utilizaban tanto FDM como TDM***.*** Esto permitía partir el canal en multiples sub-bandas, partiendo dentro de cada banda, en ***frames*** y ***slots***.

El ***base station controller (BSC)*** típicamente le daba servicio a decenas de BTS. Su trabajo era el de reservar canales de radio a los BTS, realizar ***paging*** (encontrar la celda a la cual pertenecía un usuario), y realizar el ***handoff*** de los usuarios. El conjunto de controladores y estaciones se conoce como ***base station subsystem (BSS)***.

Un ***mobile switching center (MSC)*** juega el rol central en la autorización de los usuarios, establecimiento y cierre de conexión, y ***handoff***. Usualmente, un único MSC contiene unos hasta cinco BSC.

Una red de proveedor celular tiene un número de MSC, con algunos especiales conocidos como ***MSC gateway***, que conectan la red del proveedor a la red telefónica pública.

## 2. 3G Cellular Data Networks: Extending the Internet to Cellular Subscribers

Para poder transferir datos correctamente, los dispositivos debe poder mantener conexiones TCP estables mientras están en movimiento.

![[Cellular Internet Access 2.png]]

### 3G Core Network

Esta red conecta redes de acceso con radio al internet publico. Para hacerlo, interoperar con los componentes ya existentes de las redes de 2G. El enfoque tomado fue la de mantener la red por voz ya existente, extendiéndola para permitir servicios de datos.

Existen dos tipos de nodos en estas redes: ***Serving GPRS Support Nodes (SGSN)*** y *Gateway GPRS Supports Nodes (GGSN). GPRS* significa ***Generalized Packet Radio Service,*** este era un servicio para servicio de datos en las redes **2G**.

- Un SSGN es el responsable de recibir datagrams intercambiar datagramas entre los dispositivos móviles con los que esta relacionado. Interactúa con los MSC del area, y provee autorización y ***handoff***, manteniendo información sobre los usuarios activos. También, envía paquetes entre el GGSN y los dispositivos móviles
- Un GGSN actúa como un ***gateway***, conectando multiples SGNS con el internet. Para el mundo exterior, un GGSN actúa como cualquier otro ***gateway router***. La movilidad de los dispositivos es transparente al mundo exterior.

### 3G Radio Access Network: The Wireless Edge

La ***radio access network*** es la primera ***wireless first-hop network*** que vemos como un usuario. El ***Radio Network Controller (RNC)*** típicamente controla multiples BTS, similar a la BSC a las que vimos en las redes ***2G.*** Un RNC conecta tanto ***circuit-switched cellular voice network*** a través de MSC, y ***packet-switched internet*** a través de SGSN. Mientras que los servicios de voz y de datos usan redes centrales distintas, comparten la ***radio access network*** y el RNC.

Un cambio significativo entre las redes 3G UMTS y las redes **2G** es que en lugar de utilizar el esquema de GMS ***FDMA/TDMA***, utiliza una técnica de CDMA conocida como **Direct Sequence Wideband CDMA (DW-WCDMA)**, dentro de slots de TDMA.

## 3. On to 4G: LTE

Hay dos innovaciones importantes que surgieron con la llegada de los sistemas 4G

![[Cellular Internet Access 3.png]]

### 4G System Architecture: An All-IP Core Network

Existen dos importantes observaciones de la arquitectura **4G:**

- ***A unified, all-IP network architecture.*** A diferencia de las redes 3G, la arquitectura 4G utiliza datagramas de IP para tanto trasferencias de voz como transferencias de datos. Con la llegada de **4G**, desapareció los últimos vestigios de las redes de telefonía, dando lugar a un servicio universal de IP.
- **A clear separation of the 4G data plane and 4G control plane.** Esta distinción es similar a la del plano de datos y el plano de control que vimos en IP.
- **A clear separation between the radio access network, and the all-IP-core network.** Los datagramas de IP son enviados desde el usuario *(UE)* hacia el ***gateway*** (***P-GW)*** a través de una red interna de **4G**. Los paquetes de control son intercambiados dentro de la misma red.

Los principales componentes de la arquitectura *4G* son:

- El ***eNodeB*** es el descendiente lógico de una BSC de **2G** y un RNC de **3G**. Los datagramas del UE son encapsulados en el ***eNodeB*** y enviados hacia el ***P-GW*** a través de la ***all-IP enhanced packet core (EPC)*** de la red **4G**. Esta túnel es similar al de ***IPv6*** cuando busca atravesar routers ***IPv4***. Ademas, los túneles puede tener asociadas garantías de ***Quality of Service (QoS).***
- El ***Packet Data Network Gateway (P-GW)*** reserva direcciones IP para el usuario y realiza ***QoS enforcement***. Ademas, realiza encapsulamiento y des-encapsulamiento ya que se encuentra en un extremo de la encapsulación.
- El ***Serving Gateway (S-GW)*** es el punto de anclaje de la movilidad del ***data-plane***. Todo el trafico de los usuarios pasa por aquí, y conecta directamente con el ***P-GW***.
- El ***mobility management entity (MME)*** realiza manejo de conexiones y movilidad para los usuarios de la celda que controla.
- El ***home subscriber server (HSS)*** contiene información de usuarios como el acceso a roaming, información de autenticación, perfiles de ***QoS***.

### LTE Radio Access Network

LTE utiliza una combinación de FDM y TDM para el canal de descarga, conocido como ***orthogonal frequency division multiplexing (OFDM)***. Esto permite que rangos de frecuencias vecinas no interfieran mucho entre si, incluso cuando no tienen mucho espacio entre si.

En LTE, para cada nodo activo se reserva uno o mas ***timeslots*** de ***0.5ms*** en uno o mas canales de frecuencias. Estas (re)reservas pueden realizarse hasta una vez por milisegundo, y pueden utilizarse distintos esquemas de modulación dependiendo de la circunstancia.

La reserva particular no esta gestionada por el estándar de LTE, sino que la decision de quienes podrán transmitir se determinan por algoritmos de ***scheduling*** provistos por los vendedores de LTE y operadores de red.

El ***opportunistic scheduling varia*** el protocol de capa física según las condiciones del canal para optimizar el uso del medio. Ademas, las prioridades del usuarios y el nivel se servicio contratado puede ser utilizado para favorecer las transmisiones de descarga de algunos usuarios.
