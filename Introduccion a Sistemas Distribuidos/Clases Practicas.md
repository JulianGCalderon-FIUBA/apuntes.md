---
title: Clases Prácticas
---

## Latencia

**Latencia:** La latencia es el retardo entre un estímulo y la respuesta. Es un valor conceptual

RTT: El RTT es una medida aproximada de la latencia, es el tiempo que le toma a un paquete ir a un host de destino y volver. Una forma de medirlo es a través del comando ***ping***.

Tiene cuatro componentes principales:

- ***Tiempo de Inserción:*** Es el tiempo que tarda en introducirse el paquete en el canal del enlace. Depende del tamaño del paquete y la capacidad del enlace.
- ***Tiempo de Propagación:*** Es el tiempo que tarda en propagarse el paquete en el canal de enlace. Depende de la velocidad del enlace y de la distancia entre las interfaces.
- ***Tiempo de Procesamiento:*** Es el tiempo que tarda el router en procesar el paquete y decidir a qué puerto de salida enviarlo. Suele ser despreciable.
- ***Tiempo de Encolado:*** Es el tiempo que tarda un paquete desde que es introducido a la cola de salida hasta que es efectivamente transmitido. Depende del nivel de congestión de la red.

La latencia total se calculará como la sumatoria de los tiempos mencionados para cada nodo atravesado, tanto en la idea como en la vuelta.

Si despreciamos el tiempo de encolado y de procesamiento, entonces podremos calcular la latencia de la siguiente forma:

Sea $L$ el tamaño del paquete, $R$ el ancho de banda del enlace, $D$ la distancia entre los nodos (largo del enlace) y $c$ la velocidad de propagación del medio, entonces:

$$
T_{\text{inserción}} = \frac{L}{R}
$$

$$
T_{\text{propagación}} = \frac{D}{c}
$$

Nota: trabajar con las mismas unidades para evitar errores de cálculo

Luego, para cada enlace $i$ en los enlaces atravesados $E$, calculamos su tiempo total $T_i = T_{i,\text{inserción}} +T_{i,\text{propagación}}$, luego calcularemos el tiempo total como:

$$
T = \sum_{i\in\text{E}} T_i
$$

## TCP

El protocolo TCP es un protocolo de capa de transporte que implementa un protocolo de entrega confiable, esto es:

- Asegura entrega de todos los paquetes serán entregados en orden
- Provee detección de errores para la corrupción de paquetes
- Proporciona control de flujo (para evitar enviar más paquetes de los que la aplicación del host puede recibir)
- Proporciona control de congestión (para mejorar el tráfico general de la red)
- Es un protocolo orientado a conexiones, donde se tiene un ***handshake*** y un ***close***.

Por el otro lado, el protocolo UDP es un protocolo minimalista que no ofrece un servicio confiable. Únicamente ofrece detección de errores simple con ***checksum***. Es más rápido, ya que no necesita de un ***handshake*** ni de un ***close***, y tampoco tiene control de congestión.

El protocolo TCP utiliza paquetes ***acks*** para indicarle al otro extremo de la conexión que recibir correctamente los paquetes. El valor del número de secuencia del ***ack*** será el próximo ***byte*** que esperará recibir. Si un servidor recibe un paquete de datos con número de secuencia $x$, entonces el servidor enviara un paquete de ***ack*** con un número de secuencia de $x+1$. Si un host recibe un paquete fuera de orden, entonces enviara un paquete de ***ack*** correspondiente al último paquete recibido en orden.

### Parámetros del Protocolo

El protocolo TCP puede tener los **siguientes parámetros**:

- SIZE: Tamaño del archivo que se debe enviar
- MSS: Es el tamaño máximo de los paquetes. Utilizaremos este valor como unidad para el análisis, debiendo pasar todos los valores a esta unidad.
- ***LW=1:*** Es el valor que toma la ventana de congestión luego de una perdida (al volver a la etapa ***slow start)***
- IW: Es el valor que toma la ventana de congestión al inicio del protocolo
- RTO: El tiempo establecido para los ***timer interrupts*** del ***ack*** de los paquetes.
- **ssthresh:** Es el valor en el que el protocolo pasa a la etapa de ***congestion avoidance***.
- ***cwnd:*** Es el valor de la ventana de congestión. Representa la cantidad de paquetes que puede al o sumo tener en vuelo
- ***rwnd:*** Es el valor de la ventana de recepción del host del otro lado de la conexión. Representa la cantidad de paquetes que puede al o sumo tener en vuelo
- ***Version:*** Tahoe | Reno

### Etapas del Protocolo

El protocolo consta de las **siguientes etapas**:

- ***Slow Start (SS):*** Es la etapa inicial del protocolo. Envía tantos paquetes como lo permitan las ventanas (se toma el mínimo entre la ventana de recepción y la ventana de congestión). El valor de la ventana se actualiza con la siguiente fórmula.

	$$
    \text{cwnd}(n+1) = \text{cwnd}(n) + \text{MSS}\cdot\#\text{ack}
    $$

	Es decir, por cada ***ack*** recibido, aumentamos la ventana de congestión en uno.

	Por simplificación, únicamente aumentaremos el valor de la ventana cuando lleguen los ***acks*** de todos los paquetes enviados.

	En algún momento, se dará que $\text{cwnd} == \text{sstresh}$. En este momento pasamos a la etapa de ***Congestion Avoidance (CA).***

- ***Congestion Avoidance (CA):*** En esta etapa, la ventana de congestión se aumentará linealmente:

	$$
    \text{cwnd}(n+1) = \text{cwnd}(n) + \frac{\#\text{ack}}{\text{cwnd}(n)}
    $$

	Es decir, cuando arriban todos los paquetes que estaban en vuelo (siempre debe ser entero el valor), entonces aumentaremos la ventana de congestión en un MSS.

- ***Fast Retransmit:*** Al entrar en esta fase, se reenvía inmediatamente el paquete que se presume perdido. En cuanto le llega el ***ack*** correspondiente, se avanza según el tipo de protocolo.
	- ***Tahoe:*** Realiza lo mismo que tras un RTO, se establecen los siguientes valores y se vuelve a ***Slow Start (SS):***

		$$
		\text{cwnd}(n+1) = \text{LW}
		$$

		$$
		\text{sstresh}(n+1) = \text{cwnd}(n)/2
		$$

	- ***Reno:*** Se entra en la etapa de ***Fast Recovery***, la cual establecerá los siguientes valores:

		$$
		\text{cwnd}(n+1) = \text{cwnd}(n)/2
		$$
		$$
		\text{sstresh}(n+1) = \text{cwnd}(n)/2
		$$

		Debido a que ahora ***cwnd*** y ***ssthresh*** tienen el mismo valor, se entrará a la etapa de ***Congestion Avoidance (CA)***.

### Perdida de Paquetes

Ante la **perdida de paquetes**, el protocolo responde:

- Si se da una perdida por ***RTO (timer interrupt),*** entonces se establecerán los siguientes valores y se volverá a la etapa de ***Slow Start (SS):***
- Si se da una perdida por triple ***ack*** repetido (cuatro *acks* iguales), entonces pasaremos a la etapa de ***Fast Retransmit (FR)***.

### Three-Way Handshake

Consiste de tres paquetes (de ahí su nombre)

1. El cliente envía un paquete de inicio de conexión, llamado SYN. El número de secuencia será tomado de forma aleatoria, para minimizar la probabilidad de utilizar un número de secuencia de un paquete aún presente en la red.
2. El servidor acepta la conexión y le envía un paquete de ***ack*** llamado SYNACK. Este paquete también tendrá un número de secuencia elegida de forma aleatoria, distinto al del cliente.
3. El cliente envía un último ACK para finalizar el saludo inicial.

A partir de aca, ambos hosts están conectados y pueden intercambiar información.

### Secuencia de Cierre

Consiste de cuatro paquetes:

1. El cliente inicia el cierre de la conexión con un paquete de FIN
2. El servidor confirma la recepción con un paquete de ***ack***
3. El servidor le envía un paquete de cierre de conexión FIN.
4. El cliente confirma la recepción con un paquete de ***ack.***

Tanto el cliente como el servidor pueden iniciar el cierre de la conexión.

## Routing

Existen dos definiciones importantes:

- ***Forwarding:*** Es la acción de mover los paquetes de una interfaz de entrada a una interfaz de salida
- ***Routing:*** Es la acción de decidir a qué interfaz enviar un paquete

### Tablas de Ruteo

En la versión más simple, una tabla de ruteo tiene dos columnas

Cuando se recibe un paquete, se debe comparar con las entradas de la tabla para definir a que puerto de salida debe ir. Por ejemplo, $\text{192.168.0.1/24}$ indica que los primeros $\text{24}$ bits de la dirección de destino del paquete entrante debe coincidir con $\text{192.168.0.1}$.

Generalmente, $/n$ indica que la máscara es un número binario de $\text{32}$ *bits,* donde los primeros $n$ bits tienen valor $\text 1$ mientras que los restantes tienen valor $\text 0$.

Sea $\text{Prefix}$ el prefijo de una entrada de la tabla y $\text{Mask}$ la máscara asociada a ese prefijo, entonces el paquete con dirección de destino $\text{Destination}$ coincide con dicha entrada de la tabla si y solo si:

$$
\text{Destination} \oplus \text{Mask} == \text{Prefix}
$$

El paquete deberá ser enviado a la interfaz indicada por la entrada de la tabla con el prefijo más restrictivo (más largo) que coincide. Esto se debe a que si una **subred** *particular* está incluida en otra, entonces debe enviarle el paquete a la particular.

***Default Gateway:*** El ***default gateway*** es el puerto configurado para cualquier entrada que no coincide con la tabla, se denota con el prefijo/mascara $\text{0.0.0.0/0}$, esto se debe a que, por lo que vimos recién, cualquier dirección IP coincidirá con esta entrada, pero no la preferirá por sobre cualquier otra entrada (ya que es de longitud mínima).

### Optimización de Tablas

Existen dos procedimientos para optimizar tablas:

- ***Agregación de Entradas:*** Se da cuando dos redes vecinas tienen como destino el mismo puerto, por lo que pueden ser simplificadas en una sola entrada. Se debe cumplir que:
	- Las entradas tienen una máscara de igual longitud
	- Las entradas únicamente varían en el último bit mantenido por la máscara
	- Las entradas tienen el mismo puerto de salida

	En ese caso, podremos unificar esas entradas en una sola tabla, disminuyendo en uno la longitud del prefijo. (debemos quedarnos con el prefijo cuyo último bit mantenido es un 0, ya que si no sería una entrada mal configurada).

- ***Contención de Entradas:*** Se da cuando dos entradas tienen la misma dirección de destino, y una entrada está contenida en otra. En estos casos podremos eliminar la entrada más restrictiva (la incluida en la otra).
- ***Entrada Mal Configurada:*** Una entrada mal configurada es aquella que tiene un bit de valor 1 en una posición mayor al tamaño de la máscara. Esto implica que ninguna dirección jamás podrá coincidir con ella. El prefijo es más restrictivo de lo que la máscara permite.

## Subnetting

Originalmente, se planteó dividir las redes en clases. Esto se llamó ***Classful Subnetting***, o ***Classful Addressing***. Existían tres grupos principales:

- ***Class A:*** Desde $0.0.0.0/8$ hasta $127.255.255.255.255/8$
- ***Class B:*** Desde $128.0.0.0/16$ hasta $191.255.255.255/16$
- ***Class C***: Desde $192.0.0.0/24$ hasta $223.255.255.255/24$

Tambien existían las clases $D$ (multicast) y las de clase $E$ (reservadas).

El problema con estas redes, era que había mucho desperdicio. Si no te alcanzaban las redes de clase $C$ (256) debías reservar una red de clase $B$ (25536).

Debido a esto, se optó por un sistema de particionamiento flexible, en el que las máscaras pueden ser de cualquier longitud.

### Método de Subnetting

Partiremos de un espacio de direcciones $S$ con longitud de máscara $M$. Debido a que cada red debe reservar una dirección para la ***Network Address*** y otra para la ***Broadcast Address***, tendremos un total de $T$ redes para entregar:

$$
T = 2^{32-M} - 2
$$

Esto también aplica para las subredes, por lo que si tendremos una subred con $A$ hosts y $R$ routers, entonces necesitaremos un total de $T_a$ redes para entregar:

$$
T_a = A + R + 2
$$

Las conexiones entre los routers también son **subredes**, por lo que una conexión punto a punto entre dos routers necesitaría $2 + 2 = 4$ direcciones, mientras que una entre tres routers necesitaría $3 + 2 = 5$ direcciones.

Debido a como se funcionan las máscaras, solo se pueden entregar cantidades de direcciones que sean potencias de dos, por lo que si una **subred** necesita $5$ direcciones, debemos entregarle por lo menos $2^3=8$. Nos quedaremos con la menor potencia de dos que nos proporcione al menos la cantidad de redes necesarias.

Para evitar tener tablas mal configuradas, debemos entregar subespacios de direcciones de forma creciente en orden de mayor cantidad de redes solicitadas a menor.

## Fragmentación

El MTU (***maximum transmission unit)*** es el máximo tamaño de un paquete de datos que se puede transferir en IP. Si el paquete completo tiene un tamaño mayor al MTU, se deberá fragmentar.

Los paquetes no son reensamblados en el camino, sino en el host de destino. Si se pierde un fragmento, IP descartará el paquete completo.

Los headers de IP tienen tres campos utilizados para la fragmentación:

- ***Identification:*** Es un número de **16** bits que identifica cada paquete, permite definir de qué paquete provienen los fragmentos
- ***Flags:*** Son tres bits, el primero no es utilizado, siempre valdrá cero.
	- El segundo es el bit ***Do Not Fragment***. Si vale uno, el paquete será descartado, si es necesario fragmentarlo
	- El tercer bit es el ***More Fragments***. Vale cero si es el último fragmento de un paquete.
- ***Fragment Offset:*** Número de 13 bits que determina la posición del primer bit del fragmento con relación al paquete completo. Debido a que tenemos **3** bits menos, la posición real se obtiene tras multiplicar el ***offset*** por $2^3=8$. Debido a esto, el tamaño de ***payload*** de los fragmentos debe ser múltiplo de 8.

### Método de Fragmentación

1. Si el tamaño del ***datagrama*** $D$ ***(incluye headers) es mayor al $MTU$, debemos fragmentar.
2. Calculamos el tamaño del ***payload*** $P$ (sin headers) como:

	$$
    P = D -  \underbrace{\text{Header IP}}_\text{20}
    $$

3. Calculamos el máximo tamaño de ***fragment payload*** $FP$ permitido, como:

	$$
    \max FP = MTU - \text{Header IP}
    $$

4. Como nuestro fragmento debe tener un tamaño múltiplo de 8, entonces debemos hallar el máximo valor permitido múltiplo de 8, este será:

	$$
    FP = \bigg\lfloor\frac{\max FP}8\bigg\rfloor\cdot 8
    $$

5. A partir del ***nuestro fragment payload size***, podremos calcular la cantidad de fragmentos que debemos enviar como

	$$
    \#\text{Fragments} = \bigg\lceil\frac{P}{FP}\bigg\rceil
    $$

6. Construiremos un fragmento con ***payload size*** $FP$***, datagram size*** $FP + \text{Header IP}$, y ***fragment offset*** de 0.
7. Repetiremos el procedimiento para el resto de fragmentos que se necesitan enviar. El tamaño de todos los fragmentos enviados será el mismo $(P)$ excepto el último, que tendrá un tamaño menor (o igual). Los ***fragment offset*** incrementarán linealmente a razón de $P/8$ por cada fragmento enviado. El último fragmento tendrá el bit de ***More Fragments*** en 0. Lógicamente, todos los paquetes tendrán el bit de ***Do Not Fragment*** en 0.

## NAT

El NAT o *Network Address Translation* es un mecanismo mediante el cual un router traduce direcciones IP entre dos espacios incompatibles. Suele ser utilizado en redes locales para aprovechar el uso de direcciones IP.

Los hosts dentro de una red local tienen asignada una IP únicamente dentro de esa subred. Cuando tratan de enviar un paquete a una dirección IP externa, el r***outer NAT*** (y ***default gateway de la red)*** modifica la dirección IP del remitente e inyecta su propia IP antes de reenviar el paquete, asignando un puerto específico para esa traducción. También agrega una entrada a su tabla de traducciones en las que asocia el puerto especificado con la dirección IP local del remitente original.

Cuando la respuesta al paquete enviado llega al ***router NAT,*** este utiliza la tabla de traducciones para averiguar el remitente original del paquete (a partir del puerto), y reenvía el paquete a dicho host.

De esta forma, se simula tener más direcciones IP, utilizando los puertos de un router. Desde afuera, los paquetes de toda la subred parecen provenir de un único ***host.***

Una tabla de traducción NAT mínimamente, tendría los siguientes campos:

| Puerto Router | Dirección Host | Puerto Host |
| ------------- | -------------- | ----------- |
| 23412         | 192.168.0.101  | 12412       |
| 11239         | 192.168.0.101  | 61231       |
| 31921         | 192.168.0.53   | 40032       |

El puerto del router será elegido de forma aleatoria, mientras que el puerto del host será, justamente, elegido por el host.

## DNS

El sistema DNS es el sistema mediante el cual se traducen los nombres de dominio (google.com, fiuba.com.ar), a direcciones IP.

$$
\underbrace{\text{www}}_\text{ Subdomain }\underbrace{\text{.fiuba}}_\text{ Domain }\underbrace{\text{.com}}_\text{ Second-level domain }\underbrace{\text{.ar}}_\text{ Top-level Domain }
$$

Para resolverlo, existen DNS ***servers*** ordenados de forma jerárquica que conocen las direcciones IP y los nombres de dominio de otros servidores conectados directamente.

Por encima de la jerarquía, están los servidores ***raíz*** que conocen las direcciones de los *TLD servers (top level domain)*

El servidor autoritario es aquel que conoce la dirección de un dominio completo. Puede haber cualquier número de servidores DNS intermedios, desde el servidor raíz hasta el servidor autoritario.

Por otro lado, también existen los ***local DNS servers.*** Cada ISP contiene uno, que se encarga de realizar las consultas provenientes de los usuarios.

Existen dos tipos de consultas, las consultas iterativas y las consultas recursivas.

- Cuando se realiza una consulta recursiva, si el receptor no conoce la dirección asociada al nombre de dominio dado, entonces se encargará de hallar la dirección a partir de consultas iterativas sucesivas.
- Cuando se realiza una consulta iterativa, si el receptor no conoce la dirección asociada al nombre de dominio dado, devolverá una lista de servidores que conocerán la dirección buscada. Si la conoce, devolverá la dirección buscada (o una lista de ellas)

Usualmente, todas las consultas son iterativas, excepto la consulta al servidor local. Este realizará consultas sucesivas, comenzando por el servidor raíz hasta llegar al servidor autoritario. Una vez obtenida la dirección, finalmente se la devuelve al cliente que inicio la consulta.

Los servidores utilizan ***DNS caching*** para devolver direcciones que ya fueron consultadas frecuentemente y así acelerar el proceso de consultas DNS. Los registros en el caché tienen un tiempo de vida determinado y serán eliminados luego de este.
