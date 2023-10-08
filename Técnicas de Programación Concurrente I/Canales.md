Los canales conectan un proceso emisor con un proceso receptor, y tienen un nombre y un tipo de dato.

- Son sincrónicos
- Son unidireccionales

Podremos implementar el problema del productor consumidor fácilmente. Al tener un canal `ch`, podemos enviar mensajes:

```C
loop
	Produce(I);
	ch <- I
```

Desde el otro extremo, podemos recibirlos:

```C
loop
	ch -> I
	Consume(I)
```

## Selective Input

Es una sintaxis permitida por los lenguajes que soportan canales, y permite escuchar en varios canales de forma bloqueante y desbloquearse con el primero que recibe un mensaje

```
either
	ch1 => var1
or
	ch2 => var2
or
	ch3 => var3
```

## Remote Procedure Calls

También conocido como RPC, es una forma primitiva de invocar una función en otro servidor. Hoy en dia no se realiza de esta forma.

Se requiere la implementación de *stubs* en ambos extremos. Estos conforman interfaces remotas utilizadas para comunicar el cliente y el servidor.

El *parameter marshaling* es la forma en la que se convierten los argumentos de la función para ser enviados al otro servidor.

## Canales en UNIX

UNIX provee canales a partir de *pipes*, y *FIFOs*, para conectar dos procesos independientes. Son orientados a bytes y unidireccionales.

Los FIFOs tienen una representación en el sistema de archivos. Son pensados como archivos. Los pipes se comparten entre procesos a partir de realizar `fork()`.

UNIX también provee colas de mensajes *(message queues)* orientados a mensajes como unidades independientes. De esta forma, no se lee una determinada cantidad de bytes, sino que se lee de a unidades independientes.

También existen los *flags* de prioridad. Se pueden recibir mensajes con determinada prioridad para ignorar mensajes que no nos interesan.

## Canales en Rust

Los canales tienen dos extremos: un emisor y un receptor.

- Desde el extremo emisor se pueden enviar mensajes (objetos independientes). Se debe transferir el *ownership* del objeto enviado. Este extremo se puede clonar.
- Desde el extremo receptor se pueden recibir mensajes. No se puede clonar, por lo que es único.

Los canales son asimétricos y unidireccionales. Hay un solo consumidor, y muchos productores.
