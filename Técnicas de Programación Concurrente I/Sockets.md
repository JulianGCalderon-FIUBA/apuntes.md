Son una herramienta del sistema operativo que permiten hacer comunicación entre dos procesos que estén, o bien en la misma computadora, o bien en computadoras distintas. Se utilizan para implementar un modelo de cliente-servidor:

## Servicios

Los protocolos de red pueden proveer distintos servicios:

- **Sin conexión:** Los datos se envían al receptor y no hay control de flujo ni de errores. Por ejemplo: UDP, IP.
- **Sin conexión con ACK:** Por cada dato recibido, el receptor envía un acuse de recibo conocido como ACK.
- **Con conexión:** Tiene tres fases: Un establecimiento de la conexión, intercambio de datos, y cierre de la conexión. Hay control de flujo y de errores. Por ejemplo: TCP.

## Tipos de Sockets

Existen distintos tipos de sockets, según los servicios que proveen:

- **Stream Sockets:** Proveen un servicio con conexión, utilizan el protocolo TCP.
- **Datagram Sockets:** Proveen un servicio sin conexión, utilizan el protocolo UDP.
- **Raw sockets:** Permiten a las aplicaciones enviar paquetes IP. Este también es un servicio sin conexión.
- **Sequenced Packet Sockets:** Similares a los *stream sockets*, pero preservan los delimitadores de registro. Utilizan el protocolo SSP *(Sequenced Packet Protocol)*. Hoy en día, no se utilizan.

## Sockets en UNIX

### Creación

Utilizamos la función `socket()`, definida como:

```C
int socket (int family, int type, int protocol);
```

Esto crea el *file descriptor* del *socket*, recibe por parámetro:

- `family`: Permite elegir la familia del protocolo a utilizar: IPv4, IPv6, local.
- `type`: Permite elegir el tipo de socket a crear: Stream/Datagram Socket.
- `protocolo`: Normalmente, se deja un valor de 0, ya que existe un único protocolo para cada tipo de *socket*.

Retorna el *file descriptor*, o un -1 en caso de error (y estavlece la variable externa `errno`).

### Conexión

Para conectarnos, utilizamos la función `connect()`, definida como:

```C
int connect(int sockfd, struct sockaddr *serv_addr, int addrlen);
```

Inicia una conexión con el servidor, recibe por parámetro:

- `sockfd`: Es el *file descriptor* del *socket*.
- `serv_addr`: Puntero a estructura que contiene dirección y puerto de destino.
- `addrlen`: tamaño del `serv_addr`.

Retorna 0 en caso de éxito, o -1 en caso de error (y establece la variable externa `errno`).

Para cerrar la conexión (y el *socket*), utilizamos la función `close()`.

### Lectura / Escritura

De forma genérica, utilizamos:

- La función `read()` lee bytes del *socket*
- La función `write()` escribe bytes en el *socket*

Si estamos utilizando *stream sockets*, utilizamos las funciones:

- `send()`
- `recv()`.

Si estamos utilizando *datagram sockets*, utilizamos las funciones:

- `sendto()`: Debemos indicar la dirección de destino, ya que estamos utilizando un protocolo sin conexión.
- `readfrom()`: Debemos indicar la dirección de destino, ya que estamos utilizando un protocolo sin conexión.
