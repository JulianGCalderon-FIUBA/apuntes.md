Software de conectividad que ofrece un conjunto de servicios que hacen posible el funcionamiento de aplicaciones distribuidas sobre plataformas heterogéneas.

El middleware puede ser un nodo centralizado, o estar descentralizado en forma de bibliotecas que se usan entre los procesos.

## Objetivos

Da transparencia para ocultar la distribución del sistema, y responde como si fuera una única computadora.

Dar tolerancia a fallos para que el sistema se comporte de manera predecible incluso frente a la aparición de eventos catastróficos.

Permite el acceso a recursos compartidos de forma eficiente, transparente y controlada.

Dar estándares claros sobre sintaxis y semántica de los servicios ofrecidos. Dar interoperabilidad y portabilidad.

Permitir comunicación de grupo (*broadcast*, *multicast*). Facilitar la relocalización de elementos y coordinación de tareas.

## Clasificación

Hay distintos tipos de middleware:

- **Transaccionales**: Permiten garantizar la transaccionalidad de las operaciones respecto a los datos. Permiten un acceso transparente al grupo.
- **Orientados a objetos**: Los objetos viven dentro del middleware, y se puede operar con ellos desde los clientes.
- **Orientados a procedimientos**: El middleware trabaja como un servidor de funciones que se pueden invocar. Se pueden explorar y ejecutar, pero no presentan estado para futuras invocaciones.
- **Orientados a mensajes**: Funciona como un sistema de mensajería entre aquellas aplicaciones que utilizan el middleware.

## MOMs (Message Oriented Middlewares)

### Modos

Tiene dos modos de operación:

- **Bus de información**: Pueden enviarse mensajes bajo ciertos tópicos, para que aquellos interesados lo reciban. Los mensajes se pierden si nadie los toma.
- **Cola de mensajes**: Pueden enviarse mensajes con un destinatario definido. Se quedan esperando hasta que este lo reciba.

### Sincrónico

Se modela una conexión punto a punto. Permite obtener respuestas instantáneas.

### Asincrónico

Se implementa utilizando colas. La arquitectura soporta periodos de discontinuidad del transporte.

Se deben configurar alertas para cuando se llenan las colas. Tienen un tamaño límite, no existe la cola infinita.

Si se quiere recibir respuesta a los pedidos, es necesario tener dos colas (una por cada cliente de la comunicación)

### Operaciones

Algunas operaciones comunes son:

- `Put`: Publicar un mensaje.
- `Get`: Esperar hasta que un mensaje sea detectado, luego eliminarlo y retornarlo.
- `Poll`: Revisa mensajes pendientes, sin bloquear.
- `Notify`: Asocia un *callback* utilizado por el middleware para ser ejecutado frente a publicación de ciertos mensajes.

### Broker

Proveen transparencia de localización entre emisor y receptor.

Pueden soportar lógica en el middleware para filtrado y modificación de mensajes.

Brindan un punto de control y monitoreo.

##