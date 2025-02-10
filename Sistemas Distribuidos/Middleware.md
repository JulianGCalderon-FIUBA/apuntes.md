Hay muchas definiciones:

> Es un software de conectividad que ofrece un conjunto de servicios que hacen posible el funcionamiento de aplicaciones distribuidas sobre plataformas heterogéneas.

> Módulo intermedio que actúa como conductor entre sistemas, permitiendo a cualquier usuario de sistemas de información comunicarse con varias fuentes de información que se encuentran conectadas por una red

> Capa de software que se encuentra o sitúa entre el sistema operativo y las aplicaciones del sistema

> Software que permite conectar componentes, softwares o aplicaciones. El mismo consiste en un conjunto de servicios que permiten que múltiples procesos corriendo en una o varias máquinas interactúen de un lado a otro de la red

Para definir un middleware, hablaremos de sus objetivos.

## Objetivos

Un middleware tiene distintos objetivos:

- Da **transparencia** para ocultar la distribución del sistema, y responde como si fuera una única computadora. Esto es respecto a: Ubicacion, Acceso, Migracion, Replicacion, Concurrencia, Fallos, Persistencia.
- Dar **tolerancia a fallos** para que el sistema se comporte de manera predecible, incluso frente a la aparición de eventos catastróficos. La idea es que siga funcionando, aunque de forma degradada. Esto abarca: Availability, Reliability, Safety, Maintainability.
- Permite el **acceso a recursos compartidos** de forma eficiente, transparente y controlada.
- Dar **estándares claros sobre sintaxis y semántica** de los servicios ofrecidos. Dar interoperabilidad y portabilidad.
- Permitir **comunicación de grupo** (_broadcast_, _multicast_). Facilitar la relocalización de elementos y coordinación de tareas.

## Vista Lógica

El middleware es una capa entre el sistema operativo y las aplicaciones que ofrece una vista única al sistema.

![[Middleware 1739231921.png]]

## Centralizado o Descentralizado

El middleware puede ser centralizado, en forma de un nodo intermedio con el cual se comunican los clientes. Un ejemplo es RabbitMQ.

Por otro lado, el middleware puede descentralizado, en forma de bibliotecas presentes en cada nodo que abstraigan este detalle. Un ejemplo es ZeroMQ.

Un middleware centralizado es más fácil de monitorear, ya que hay un único punto donde obtener la información del sistema (por ejemplo: encontrar congestión).

Un middleware distribuido puede llegar a ser más performante y tiene mejor tolerancia a fallas.

## Clasificación

Hay distintos tipos de middleware:

- **Transaccionales**: Permiten garantizar la transaccionalidad de las operaciones respecto a los datos. Permiten un acceso transparente al grupo.
- **Orientados a procedimientos**: El middleware trabaja como un servidor de funciones que se pueden invocar. Se pueden explorar y ejecutar, pero no presentan estado para futuras invocaciones. Un ejemplo es [[Remote Procedure Control]].
- **Orientados a objetos**: Los objetos viven dentro del middleware, y se puede operar con ellos desde los clientes. A este concepto se lo conoce como [[Objetos Distribuidos]].
- **Orientados a mensajes**: Funciona como un sistema de mensajería entre aquellas aplicaciones que utilizan el middleware. Este tipo se conoce como [[Message Oriented Middleware]].
