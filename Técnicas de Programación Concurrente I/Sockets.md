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

## Sockets en C

### Creación

Utilizamos la función `socket()`, definida como:

```C
int socket (int family, int type, int protocol);
```

Esto crea el *file descriptor* del *socket*, recibe por parámetro:

- `family`: Permite elegir la familia del protocolo a utilizar: IPv4, IPv6, local.
- `type`: Permite elegir el tipo de socket a crear: Stream/Datagram Socket.
- `protocolo`: Normalmente, se deja un valor de 0, ya que existe un único protocolo para cada tipo de *socket*.

Retorna el *file descriptor*, o un -1 en caso de error (y establece la variable externa `errno`).

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

Si estamos utilizando *stream sockets*, utilizamos las funciones `send()` y `recv()`. No hace falta indicar la dirección, ya que es un protocolo con conexión

Si estamos utilizando *datagram sockets*, utilizamos las funciones `sendto()` y`readfrom()`. Debemos indicar la dirección de destino, puesto que estamos utilizando un protocolo sin conexión.

### Conexión Pasiva

Para crear una conexión pasiva (desde un servidor), utilizamos `bind()`.

```c
int bind(int sockfd, struct sockaddr *my_addr, int addrlen);
```

Esta asigna una dirección local al *socket*, para que pueda recibir conexiones de clientes. Retorna 0 en caso de éxito, y -1 en caso de error (y establece la variable externa `errno`).

Luego de esto, debemos utilizar la función `listen()` para convertirlo en un *socket* pasivo.

```c
int listen(int sockfd, int backlog);
```

Recibe por parámetro el `backlog` que es la longitud máxima de la cola de conexiones pendientes que puede tener el servidor. Retorna 0 en caso de éxito, y -1 en caso de error (y establece la variable externa `errno`).

Distintas implementaciones de los distintos sistemas operativos toman el número `backlog` de forma distinta. Algunas implementaciones lo toman como la cantidad total de conexiones ya establecidas, y otras implementaciones como la cantidad total de conexiones (las pendientes y las establecidas).

### Conexiones Entrantes

Para tomar una conexión entrante de un cliente, utilizamos `accept()`.

```C
int accept(int sockfd, 
					 struct sockaddr *cliaddr, 
					 socklen_t *addrlen);
```

Esta función extrae una conexión establecida de la cola de conexiones. Escribe en `cliaddr` la dirección del cliente con el que se conectó. Si todavía no hay ninguna conexión, entonces el proceso se bloquea hasta que llegue una conexión.

Retorna el *file descriptor* del cliente en caso de éxito, el cual se utilizará para comunicarse con él. En caso de error, retorna -1 (y establece la variable externa `errno`).

### Dirección de Socket

La dirección de un *socket* se define de forma genérica con la estructura `sockaddr`.

```C
struct sockaddr {
	unsigned short sa_familty;
	char sa_data[14];
}
```

En `sa_family` se guarda la familia del protocolo. En `sa_data` se guarda tanto la dirección como el puerto

Por otro lado, tendremos `sockaddr_in` para cuando utilizamos IP.

```C
struct sockaddr_in {
	short int sin_family;
	unsigned short int sin_port;
	struct in_addr sin_addr;
	unsigned char sin_zero[8];
}
```

Finalmente, guardamos la dirección en

```C
typedef uint32_t in_addr_t;
struct in_addr {
	in_addr_t s_addr;
}
```

## Sockets en Rust

El módulo de `std::net` nos ofrece estructuras para el manejo de la red.

### Conexión Pasiva

Para asociar un socket a una dirección, utilizamos la función `BIND` que crea un nuevo `TcpListener` y lo asocia a una dirección.

```Rust
pub fn bind<A: ToSocketAddrs>(addr: A) -> Result<TcpListener>
```

El *listener* retornado está listo para aceptar conexiones.

### Conexiones Entrantes

El método `incoming` retorna un iterador que devuelva una secuencia de conexiones de tipo `TcpStream`. La iteración es sobre *intentos* de conexiones (puede devolver error).

```Rust
pub fn incoming(&self) -> Incoming<'_>
```

Cada *stream* representa una conexión abierta entre el cliente y el servidor.

Si se quiere aceptar una única conexión, podemos utilizar el método `accept`, que bloquea el hilo hasta que surja una conexión establecida.

```Rust
pub fn accept(&self) -> Result<(TcpStream, SocketAddr)>
```

### Lectura / Escritura

Un `TcpStream` implementa tanto el *trait* `std::io::Read` como el *trait* `std::io::Write`, por lo que tendremos disponibles los métodos de escritura y lectura de *bytes*.

```Rust
fn read(&mut self, buf: &mut [u8]) -> Result<usize>
fn write(&mut self, buf: &mut [u8]) -> Result<usize>
```
