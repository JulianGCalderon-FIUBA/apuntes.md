El protocolo TCP es un protocolo de capa de transporte que implementa un protocolo de entrega confiable, esto es:

- Asegura entrega de todos los paquetes serán entregados en orden
- Provee detección de errores para la corrupción de paquetes
- Proporciona control de flujo (para evitar enviar más paquetes de los que la aplicación del host puede recibir)
- Proporciona control de congestión (para mejorar el tráfico general de la red)
- Es un protocolo orientado a conexiones, donde se tiene un *handshake* y un *close*.

Por el otro lado, el protocolo UDP es un protocolo minimalista que no ofrece un servicio confiable. Únicamente ofrece detección de errores simple con *checksum*. Es más rápido, ya que no necesita de un *handshake* ni de un *close*, y tampoco tiene control de congestión.

El protocolo TCP utiliza paquetes *acks* para indicarle al otro extremo de la conexión que recibir correctamente los paquetes. El valor del número de secuencia del *ack* será el próximo *byte* que esperará recibir. Si un servidor recibe un paquete de datos con número de secuencia $x$, entonces el servidor enviara un paquete de *ack* con un número de secuencia de $x+1$. Si un host recibe un paquete fuera de orden, entonces enviara un paquete de *ack* correspondiente al último paquete recibido en orden.

## Parámetros del Protocolo

El protocolo TCP puede tener los siguientes parámetros:

- `SIZE`: Tamaño del archivo que se debe enviar.
- `MSS`: Es el tamaño máximo de los paquetes. Utilizaremos este valor como unidad para el análisis, debiendo pasar todos los valores a esta unidad.
- `LW=1`: Es el valor que toma la ventana de congestión luego de una perdida (al volver a la etapa *slow start*).
- `IW`: Es el valor que toma la ventana de congestión al inicio del protocolo.
- `RTO`: El tiempo establecido para los *timer interrupts* del *ack* de los paquetes.
- `ssthresh`: Es el valor en el que el protocolo pasa a la etapa de *congestion avoidance*.
- `cwnd`: Es el valor de la ventana de congestión. Representa la cantidad de paquetes que puede al o sumo tener en vuelo.
- `rwnd`: Es el valor de la ventana de recepción del host del otro lado de la conexión. Representa la cantidad de paquetes que puede al o sumo tener en vuelo.
- `Version`: Puede ser Tahoe o Reno.

## Etapas del Protocolo

El protocolo consta de las siguientes etapas:

### Slow Start (SS):

Es la etapa inicial del protocolo. Envía tantos paquetes como lo permitan las ventanas (se toma el mínimo entre la ventana de recepción y la ventana de congestión). El valor de la ventana se actualiza con la siguiente fórmula.

$$
\text{cwnd}(n+1) = \text{cwnd}(n) + \text{MSS}\cdot\#\text{ack}
$$

Es decir, por cada *ack* recibido, aumentamos la ventana de congestión en uno.

Por simplificación, únicamente aumentaremos el valor de la ventana cuando lleguen los *acks* de todos los paquetes enviados.

En algún momento, se dará que $\text{cwnd} == \text{sstresh}$. En este momento pasamos a la etapa de **Congestion Avoidance** (CA).

### Congestion Avoidance (CA):

En esta etapa, la ventana de congestión se aumentará linealmente:

$$
\text{cwnd}(n+1) = \text{cwnd}(n) + \frac{\#\text{ack}}{\text{cwnd}(n)}
$$

Es decir, cuando arriban todos los paquetes que estaban en vuelo (siempre debe ser entero el valor), entonces aumentaremos la ventana de congestión en un MSS.

### Fast Retransmit:

Al entrar en esta fase, se reenvía inmediatamente el paquete que se presume perdido. En cuanto le llega el *ack* correspondiente, se avanza según el tipo de protocolo.

El comportamiento dependerá del algoritmo utilizado:

#### Tahoe

Realiza lo mismo que tras un RTO, se establecen los siguientes valores y se vuelve a **Slow Start** (SS):

$$
\text{cwnd}(n+1) = \text{LW}
$$

$$
\text{sstresh}(n+1) = \text{cwnd}(n)/2
$$

#### Reno

Se entra en la etapa de **Fast Recovery**, la cual establecerá los siguientes valores:

$$
\text{cwnd}(n+1) = \text{cwnd}(n)/2
$$

$$
\text{sstresh}(n+1) = \text{cwnd}(n)/2
$$

Debido a que ahora `cwnd` y `ssthresh` tienen el mismo valor, se entrará a la etapa de **Congestion Avoidance** (CA).

## Perdida de Paquetes

Ante la **perdida de paquetes**, el protocolo responde:

- Si se da una perdida por RTO *(timer interrupt)*, entonces se establecerán los siguientes valores y se volverá a la etapa de **Slow Start** (SS):

	$$
	\text{cwnd}(n+1) = \text{LW}
	$$

	$$
	\text{sstresh}(n+1) = \text{cwnd}(n)/2
	$$

- Si se da una perdida por triple *ack* repetido (cuatro *acks* iguales), entonces pasaremos a la etapa de **Fast Retransmit** (FR).

## Three-Way Handshake

Consiste de tres paquetes (de ahí su nombre)

1. El cliente envía un paquete de inicio de conexión, llamado SYN. El número de secuencia será tomado de forma aleatoria, para minimizar la probabilidad de utilizar un número de secuencia de un paquete aún presente en la red.
2. El servidor acepta la conexión y le envía un paquete de *ack* llamado SYNACK. Este paquete también tendrá un número de secuencia elegida de forma aleatoria, distinto al del cliente.
3. El cliente envía un último ACK para finalizar el saludo inicial.

A partir de acá, ambos hosts están conectados y pueden intercambiar información.

## Secuencia de Cierre

Consiste de cuatro paquetes:

1. El cliente inicia el cierre de la conexión con un paquete de FIN
2. El servidor confirma la recepción con un paquete de *ack*.
3. El servidor le envía un paquete de cierre de conexión FIN.
4. El cliente confirma la recepción con un paquete de *ack*.

Tanto el cliente como el servidor pueden iniciar el cierre de la conexión.
