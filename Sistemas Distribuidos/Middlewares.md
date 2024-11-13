## Definiciones

Hay muchas definiciones:

> Es un software de conectividad que ofrece un conjunto de servicios que hacen posible el funcionamiento de aplicaciones distribuidas sobre plataformas heterogéneas.

> Módulo intermedio que actúa como conductor entre sistemas, permitiendo a cualquier usuario de sistemas de información comunicarse con varias fuentes de información que se encuentran conectadas por una red

> Capa de software que se encuentra o sitúa entre el sistema operativo y las aplicaciones del sistema

> Software que permite conectar componentes, softwares o aplicaciones. El mismo consiste en un conjunto de servicios que permiten que múltiples procesos corriendo en una o varias máquinas interactúen de un lado a otro de la red

Para definir un middleware, hablaremos de sus objetivos.

## Objetivos

Un middleware tiene distintos objetivos:

- Da transparencia para ocultar la distribución del sistema, y responde como si fuera una única computadora.
- Dar tolerancia a fallos para que el sistema se comporte de manera predecible, incluso frente a la aparición de eventos catastróficos.
- Permite el acceso a recursos compartidos de forma eficiente, transparente y controlada.
- Dar estándares claros sobre sintaxis y semántica de los servicios ofrecidos. Dar interoperabilidad y portabilidad.
- Permitir comunicación de grupo (_broadcast_, _multicast_). Facilitar la relocalización de elementos y coordinación de tareas.

El middleware puede ser un nodo centralizado, o estar descentralizado en forma de bibliotecas que se usan entre los procesos.

## Clasificación

Hay distintos tipos de middleware:

- **Transaccionales**: Permiten garantizar la transaccionalidad de las operaciones respecto a los datos. Permiten un acceso transparente al grupo.
- **Orientados a objetos**: Los objetos viven dentro del middleware, y se puede operar con ellos desde los clientes.
- **Orientados a procedimientos**: El middleware trabaja como un servidor de funciones que se pueden invocar. Se pueden explorar y ejecutar, pero no presentan estado para futuras invocaciones.
- **Orientados a mensajes**: Funciona como un sistema de mensajería entre aquellas aplicaciones que utilizan el middleware.
