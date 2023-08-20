---
title: Multiple Access Links and Protocols
---

Un ***point-to-point link*** consiste en un único remitente en un extremo de enlace y un único receptor en el otro extremo del enlace. Existen multiples protocolos para el envío de información a través de este enlace, entre ellos: **point-to-point protocol (PPP)** y **high-level data link control (HDLC)**.

Un ***broadcast link*** puede tener múltiples remitentes y receptores, todos conectados al mismo canal compartido. Las computadoras tienen protocolos, llamados multiple access protocols, mediante los cuales se regulan las transmisiones dentro del canal compartido. Aunque técnicamente los nodos acceden mediante un adaptador, trataremos a los nodos directamente como los remitentes y receptores.

Si dos nodos transmiten información al mismo tiempo, ambas señales colisionan, corrompiendo los datos. Debido a esto, debemos asegurar que las transmisiones de los nodos activos estén coordinadas de alguna forma.

Los protocolos se pueden separar en tres categorías: *channel partitioning protocols, random access protocols, taking-turns protocols.*

## 1. Channel Partitioning Protocols

Un protocolo TDM divide el tiempo en ***time frames***, que a su vez son divididos en $n$ ***time slots***, siendo $n$ el número de nodos conectados al canal. Cada uno de los ***time slots*** es asignado a uno de los nodos, por lo que solo puede transmitir información en momentos seleccionados

Un protocolo FDM divide el canal en $n$ rangos de frecuencia, creando efectivamente $n$ canales distintos, uno para cada nodo.

Ambos protocolos son totalmente justos, pero tienen la desventaja de limitar la tasa de transmisión cuando hay un solo nodo enviando datos.

Un tercer protocolo comúnmente utilizado es el de ***code division multiple access (CDMA)***. El protocolo le asigna a cada nodo un código diferente, el cual utilizara para codificar los datos de los bits que enviará. Si estos códigos se seleccionan cuidadosamente, se puede permitir que multiples nodos transmitan simultáneamente sin generar interferencia.

## 2. Random Access Protocols

En este tipo de protocolos, los nodos transmiten datos a tasa completa a través del canal. Si ocurre una colisión, entonces reenviarán el paquete, pero no inmediatamente. Si el tiempo de espera es el mismo, entonces ocurrirá una colisión nuevamente. Es por esto que los nodos esperarán tiempos aleatorios antes de reenviar el paquete.

Existen muchos protocolos de este estilo, en esta sección estudiaremos los más conocidos

### Slotted ALOHA

Las operaciones de cada nodo en el canal son simples:

- Si un nodo tiene un paquete para enviar, esperará hasta el inicio del próximo ***slot*** para transmitir el paquete completo en este ***slot***.
- Si ocurre una colisión, este retransmitirá el paquete con probabilidad $p$ en cada subsecuente ***slot*** disponible, hasta que se transmita sin colisión
- Si no ocurre una colisión, entonces puede prepararse para enviar el próximo paquete, de ser necesario.

Si hay un único nodo transmitiendo, este transmitirá información a la tasa completa, solucionando el problema de los protocolos de particionamiento de canal. Es un protocolo altamente descentralizado.

Consideraremos un ***successful slot*** cuando un solo nodo transmite un mensaje en este ***slot***. La eficiencia del protocolo se define como la fracción a largo plazo de los ***successful slots***. Si suponemos que todos los nodos siempre tienen un paquete para enviar, entonces la probabilidad de envío un successful slot será de $Np(1-p)N-1$. Debemos hallar el $p$ que maximiza la expresión. Para $N$ tendiendo a infinito, la probabilidad de un ***slot exitoso*** será de únicamente $1/e=0.37$. Se está utrilizando correctamente un tercio de la banda ancha total.

### ALOHA

El primer protocolo de ALOHA era desincronizado, por lo que los nodos no esperaban al comienzo de cada ***slot para enviar un paquete***. Si el paquete no es enviado con probabilidad $p$, en lguar de esperar al comienzo del próximo, entonces se espera un tiempo predeterminado de ***frame transmission time***.

Si hacemos un analisis similar, encontramos que la maxima eficiencia será la de $1/2e$, exactamente la mitad de la del protocolo anterior.

### Carrier Sense Multiple Access (CSMA)

El comportamiento de los nodos en ALOHA es independientemente del resto de nodos del canal, el protocolo CSMA tiene dos reglas importantes para mejorar la comunicación:

- ***Listen before Speaking:*** En la jerga de redes, se conoce como ***carrier sensing***. Si un nodo está transmitiendo un paquete, debe esperar a que este finalice antes de enviar su propio paquete. Para esto, se introduce un tiempo de espera entre que finaliza la transmisión de otro nodo hasta que inicia la propia.
- **If someone else begins talking at the same time, stop talking:** En la jerga de redes, se conoce como ***collision detection***. Si se detecta que un nodo está transmitiendo a la vez que el propio nodo, entonces se debe cortar la transmisión y esperar un tiempo aleatorio antes de continuar el ciclo.

La razón por la cual, siguiendo la primera regla, pueden ocurrir colisiones, es debido a la existencia de ***channel propagation delay***. Dos nodos pueden transmitir a la vez por una fracción de tiempo sin darse cuenta.

### CSMA with Collision Detection (CSMA/CD)

La segunda regla permite detectar las colisiones y reducir significativamente el tiempo perdido. Para determinar el tiempo de espera antes de volver a probar de transmitir, se utiliza el algoritmo de ***binary exponential backoff***.

Cuando se retransmite un paquete que ya experimento $n$ colisiones, el nodo toma un valor de $k$ aleatorio entre 0 y 2$n$-1. Cuantas más colisiones ocurran, más tiempo de espera habrá. Para ***ethernet***, el tiempo de espera será de 512$k$ *bit times*. (es decir, el tiempo necesario para enviar 152$k$ bits)

Debido al tiempo de espera creciente por colisiones, este protocolo no sirve para aplicaciones de tiempo real

### CSMA/CD Efficiency

Cuando únicamente hay un nodo enviando información, la tasa de envío será la máxima. Por el otro lado, si transmiten muchos nodos a la vez, la eficiencia será mucho menor.

Denotemos $d_{\text{prop}}$ como el máximo tiempo que le toma a una señal propagarse entre dos adaptadores, y $d_{\text{trans}}$ el tiempo que toma en transmitir un paquete de tamaño máximo. Entonces la eficiencia tendrá una forma aproximada a la siguiente:

$$
\text{Efficiency} = 1 +\frac{d_{\text{prop}}}{d_{\text{trans}}}
$$

Si el tiempo de propagación es muy chico, la eficiencia tenderá a cero. Esto tiene sentido, ya que no habrá nodos transmitiendo a la vez. Si el tiempo de transmisión es muy grande, entonces una vez que un nodo obtiene control del canal, lo usara por mucho tiempo. De esta forma obtendremos un alto porcentaje de canales utilizado exitosamente

## 3. Taking-Turns Protocols

Nuevamente, hay muchos protocolos de este estilo. Discutiremos los dos más importantes. El primero fue el ***polling protocol***. Este protocolo requiere que uno de los nodos del canal sea el ***master node***. Este será el encargado de seleccionar cada uno de los nodos utilizando ***round-robin***. El ***master node*** le indicará a cada uno de los nodos del canal, la maxima cantidad de ***frames*** que puede enviar y en qué momento, de forma cíclica y continua.

Este protocolo permite aprovechar los nodos inactivos, permitiendo una eficiencia mucho mayor, pero con algunas desventajas. La primera es que se debe introducir un **polling delay**, necesario para notificar al próximo nodo que puede enviar información. Una segunda desventaja importante es que si falla el nodo maestro, el canal entero se vuelve inoperante.

Un segundo protocolo conocido como ***token-passing protocol*** consiste en la existencia de un ***frame*** de propósito especial que es intercambiado entre los nodos en un orden fijo y cíclico (cada nodo se lo envía al siguiente).

Los nodos pueden únicamente enviar información si tienen el ***token***, y puede enviar hasta un máximo definido antes de tener que devolver el ***token***. Si un nodo no tiene información a enviar, entonces únicamente reenvía el ***token***.

Algunas desventajas de este protocolo es que si un nodo falla, el canal completo falla. Además, si un nodo accidentalmente no libera el ***token***, se debe invocar algún protocolo de recuperación para que vuelva a circulación.

Esta tecnología sirve para tiempo real, pero no es utilizada de esta forma hoy en dia. Por encima de ethernet, se utiliza el protocolo *Token Bus* para prevenir colisiones.

## 4. DOCSIS: The Link-Layer Protocol for Cable Internet Access

Recordemos que una ***cable access network*** típicamente consiste en miles de *residential cable modems* conectados a un único cable modem termination system (CMTS). DOCSIS utiliza FDM para dividir el ***downstream*** (con el CMTS como único remitente) y el ***upstream***. Debido a que en el ***downstream*** hay un único remitente, no es necesario prevenir colisiones.

Para el caso del ***upstream***, cada canal se divide con TDM en intervalos de tiempo, cada uno conteniendo ***mini-slots*** mediante los cuales los ***modems*** particulares pueden transmitir al CMTS. En el ***downstream*** el CMTC envía mensajes de control conocidos como MAP que especifican que ***modem*** puede transmitir en cada determinado momento.

Para que el CMTC conozca qué modems quieren enviar información, estos envían ***mini-slot-request frames al CMTC*** a través de intervalos especiales dedicados a este propósito. Para compartir estos intervalos especiales, se utiliza un ***random access protocol***. Debido a que no hay confirmación de recibo, los ***requests*** son reenviados si no se recibió una respuesta en el tiempo cercano.

Cuando hay poco tráfico en el *upstream channel*, los ***modems*** pueden transmitir ***data frames*** a través de los ***slots*** asignados para los ***request frames***.
