---
title: Multiplexing and Demultiplexing
---

Recordemos que un proceso puede tener uno o más sockets, debido a esto, la capa de transporte no tiene que enviar información directamente a los procesos, sino a un socket intermediario.

Cada segmento de capa de transporte tiene un conjunto de campos para este propósito. La capa de transporte del receptor debe examinar estos campos para identificar al socket adecuado y enviarle los segmentos. Este trabajo es conocido como **demultiplexing**. El trabajo de juntar *data chunks* en el host de fuente de distintos sockets, encapsularlos con información de cabecera para crear segmentos y enviar estos segmentos a la capa de red se conoce como *multiplexing*.

Estos campos especiales son: *source port number field* y *destination port number field*. Cada puerto es un número de 16 bits, los números del 0 al 1023 son llamados *well-known port numbers* y se reservan para protocolos de aplicación conocidos.

Para implementar el servicio de *demultiplexing*, cada socket en el host puede ser asignado un número de puerto. Cuando un segmento arriba, la capa de transporte examina el número de puerto y redirige el segmento al socket correspondiente.

## Connectionless Multiplexing and Demultiplexing

Cuando un socket UDP es creado, la capa de transporte automáticamente asigna un número de puerto a este socket. Alternativamente, el desarrollador de la aplicación puede asociarlo a un puerto específico (esto es usualmente utilizado en la implementación del *server-side* de una aplicación).

Un socket UDP se identifica por una dupla conteniendo una dirección IP de destino y un número de puerto de destino. Esto implica que si dos segmentos tienen distinta dirección de envío, pero misma dirección de destino, serán direccionados al mismo socket.

## Connection-Oriented Multiplexing and Demultiplexing

Un socket TCP es identificado por una tupla de cuatro valores, conteniendo: dirección IP del remitente, número de puerto del remitente, dirección IP de destino, número de puerto de destino. Cuando un segmento llega a un host, este utiliza estos cuatro valores para direccionar el segmento al socket apropiado.

Un servidor TCP tiene un *welcoming socket* que espera a nuevas conexiones en un número de puerto determinado. Un cliente TCP crea un socket y envía un pedido de establecimiento de conexión al servidor. Cuando el servidor TCP recibe segmento de pedido de establecimiento de la conexión, entonces crea un nuevo socket por el cual se llevará a cabo esta comunicación. Un *server host* puede soportar múltiples sockets de conexión TCP simultáneos (asociados al mismo puerto), cada uno asignado a un proceso. Para determinar esto, se utiliza la dirección y el puerto de envío.

## Port Scanning

Hemos visto que los procesos esperan pacientemente en un puerto abierto a la conexión de un cliente remoto, algunos de estos puertos son conocidos. De esta forma, podemos determinar la aplicación ejecutándose en el servidor basándonos en el número de puerto utilizado. Los atacantes pueden utilizar esta información para atacar servidores.

Determinar que aplicaciones están escuchando en que puertos es una tarea relativamente fácil. Hay múltiples programas de dominio público, llamados *port scanners*, que cumplen esta propiedad.
