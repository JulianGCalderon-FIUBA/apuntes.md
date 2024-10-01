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
