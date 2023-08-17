---
title: The Network Edge
---

Los *end systems* se denominan así ya que se encuentran en el extremo final de la red. También denominados *hosts* ya que *hostean* (ejecutan) aplicaciones. Usaremos ambos términos indistintamente. *Los hosts* se suelen separar a su vez en *clientes* y *servidores*.

## 1. Access Networks

La red que conecta física los *hosts* a su primer *router (edge router)*.

### Home Access

En 2015, las dos formas principales de Acceso residencial de banda ancha eran:

#### DSL (Digital Subscriber Line)

Una residencia usualmente obtiene este acceso de internet *DSL* del mismo proveedor de línea de teléfono. Debido a esto, se usa cable de la línea de teléfono. Utilizando distintas frecuencias para transmitir tanto datos como señales telefónicas de forma simultánea:

- A high-speed downstream channel, in the 50 kHz to 1 MHz band
- A medium-speed upstream channel, in the 4 kHz to 50 kHz band
- An ordinary two-way telephone channel, in the 0 to 4 kHz band

Desde el lado del cliente, un *splitter* separa estas frecuencias y envía los datos al módem *DSL*. Desde el lado del proveedor de internet, un *DSLAM* los datos de las señales de teléfono y las envía a internet. Miles de dispositivos se conectan a un mismo *DSLAM*.

Como la descarga y la subida tienen distintas tasas, se dice que es de acceso asimétrico.

#### Cable

Este método hace uso del cable de televisión para proporcionar acceso a internet. Requiere de un tipo especial de módem llamado *cable modem*. Al igual que *DSL*, es de acceso asimétrico.

Cables coaxiales conectan un vecindario, compartidos entre varios usuarios (entre 500 y 5000). Todos ellos están conectados a un nodo, el cual se comunica con el proveedor a través de un cable fibra óptica. Debido a que el cable atraviesa varias casas antes de llegar a destino, si múltiples usuarios usan el internet al mismo tiempo, la velocidad de conexión baja. Como se usa tanto un cable coaxial como de fibra óptica, este sistema se suele denominar como *HFC* *(hybrid fiber coax)*

Desde el servidor, hay una estructura similar al DSLAM conocida como CMTS, transformando las señales analógicas de las casas a señales digitales.

#### Direct Fiber

Hay múltiples tecnologías en competencia por distribución óptica a los hogares, La más simple es conocida como *direct fiber*. Es un método muy veloz que consiste en que los cables de fibra óptica lleguen a las casas de los clientes. Usualmente, cada cable está compartido entre varias casas, el cual es separado utilizando *splitters.* Hay dos arquitecturas principales: **AONs Active Optical Networks** (este método es esencialmente *switched ethernet*) y **PONs Passive Optical Networks.** En este último, El splitter combina un número de casas (usualmente menor que 100) en un único cable compartido, el cual se conecta a un *Optical Line Terminator (OLT)* en la central de internet.

#### Other Methods

Otros métodos menos utilizados son: *Satellite Links* y *Dial-up Access.* Este último es utilizado en casas tradicionales. Tiene un esquema similar al *DSL*, pero mucho más lento.

### Access in the Enterprise (and the Home): Ethernet and WiFi

Para los dispositivos dentro de una casa, se utiliza una *LAN (local area network)* para proveer de internet a dispositivos cercanos. Se utilizan dos métodos principales para conectarse al *edge router*.

- **Ethernet:** Se utilizan cables de cobre conectados a un *ethernet switch,* el cual a su vez está conectado al *internet*.
- **Wifi:** Se utiliza para dar internet de forma inalámbrica a dispositivos cercanos a un *punto de acceso.

### Wide-Area Wireless Access: 3G and LTE

Las empresas de telecomunicaciones han hecho enormes inversiones en tecnologías de acceso a internet inalámbrico de largo alcance, como *LTE, 3G, 4G, etc.*

## 2. Physical Media

Consideremos un *bit* viajando de un *end system* a otro, a través de una serie de *links* y *routers.* Por cada *transmitter-receiver*, el *bit* se envía propagando ondas electromagnéticas o pulsos eléctricos a través de un medio físico.

Hay muchos medios por los cuales se envía la información a través de la red. Los medios se separan en dos categorías:

- **Guided Medium:** Las ondas se transmiten a través de un medio sólido, como un cable coaxial, de fibra óptica, o de cobre. El costo de estos nombres suele ser muy barato, en comparación con otros elementos de la red. (como la instalación en sí)
- **Non Guided Medium:** Las ondas se transmiten por la atmósfera, de forma inalámbrica.

### Twisted-Pair Copper Wire

El cable más barato y común que se puede encontrar, se utiliza hace más de un siglo. Cada cable consiste en un único *communication link*.

Dos cables de cobre giran sobre mismos para reducir interferencia eléctrica ocasionada por otros cables cercanos. Usualmente, varios pares de cables se juntan en uno solo y se envuelven con un escudo protector. Dentro de un edificio, se suele utilizar *UTP (Unshielded twisted pair)*

### Coaxial Cable

Como el anterior, consiste en dos conductores de cobre, concéntricos en lugar de paralelos. Este cable puede alcanzar altas velocidades. Este cable puede ser usado como un *shared medium,* múltiples sistemas se pueden conectar a un mismo cable.

### Fiber Optics

La fibra óptica es un medio fino y flexible que transmite pulsos de luz, cada uno representando un bit. Es extremadamente rápido y seguro, utilizado en conexiones de larga distancia.

Al ser más costoso, no es tan utilizado en distancias cortas como en el hogar.

### Terrestrial Radio Channels

Los canales de radio transmiten señales utilizando el espectro electromagnético. Son atractivos ya que no requiere cables y puede penetrar paredes. Se pueden separar en tres categorías, según su alcance: Distancia corta (uno o dos metros), áreas locales (decenas o cientos de metros) y áreas amplias (decenas de kilómetros).

### Satellite Radio Channels

Un satélite de comunicación conecta dos receptores/emisores de microondas, conocidos como *ground stations*. El satélite recibe señales en una banda de frecuencia, y replica la señal utilizando un repetidor, en otra frecuencia. Hay dos tipos de satélites: **Geostationary Satellites** permanentemente permanecen en el mismo punto de la tierra. Al estar bastante lejos de la tierra, tienen un sustancial *delay*. Los **low-earth orbiting (LEO) satellites** se colocan más cerca de la tierra y rotan alrededor de ella. Proveen cobertura continua en un área, pero muchos de estos satélites tienen que ser colocados en órbita
