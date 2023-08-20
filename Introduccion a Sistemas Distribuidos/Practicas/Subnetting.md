Originalmente, se planteó dividir las redes en clases. Esto se llamó *Classful Subnetting*, o *Classful Addressing*. Existían tres grupos principales:

- **Class A:** Desde $0.0.0.0/8$ hasta $127.255.255.255.255/8$
- **Class B:** Desde $128.0.0.0/16$ hasta $191.255.255.255/16$
- **Class C**: Desde $192.0.0.0/24$ hasta $223.255.255.255/24$

También existían las clases $D$ *(multicast)* y las de clase $E$ (reservadas).

El problema con estas redes, era que había mucho desperdicio. Si no te alcanzaban las redes de clase $C$ (256) debías reservar una red de clase $B$ (25536).

Debido a esto, se optó por un sistema de particionamiento flexible, en el que las máscaras pueden ser de cualquier longitud.

## Método de Subnetting

Partiremos de un espacio de direcciones $S$ con longitud de máscara $M$. Debido a que cada red debe reservar una dirección para la *Network Address* y otra para la *Broadcast Address*, tendremos un total de $T$ redes para entregar:

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
