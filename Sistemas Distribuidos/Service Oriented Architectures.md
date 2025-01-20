## Evolución de Arquitecturas

### Monolíticas

Esta fue la arquitectura más usada en la historia del internet. A medida que crece el sistema, crece el *web server*.

- **Reverse Proxy**: Resuelve consultas más simples, como la de archivos estáticos.
- **Web Server**: Resuelve consultas más complejas, relacionadas con la lógica de negocio.
- **Database Server**: Base de datos que almacena el estado del sistema.

![[Service Oriented Architectures 1737415456.png]]

Si los servidores pueden ser replicados, entonces estas arquitecturas son escalables:

![[Service Oriented Architectures 1737415688.png]]

Esto nos da la posibilidad de routear consultas según distintos criterios, como ubicación, o afinidad de los datos.

El *reverse proxy* es un único punto de falla, por lo que debemos ser cuidadosos con las responsabilidades que le asignamos.

### Service Oriented Architecture

Si tenemos distintas necesidades en las aplicaciones, y queremos asignar recursos según la aplicación en lugar de todas por igual, surge la necesidad de utilizar una *service oriented architecture* (SOA).

![[Service Oriented Architectures 1737416013.png]]

En estos sistemas, los clientes acceden al registro de servicios para encontrar los procesos orquestadores. Estos a su vez utilizarán uno o varios servicios, que accederán a una a varias bases de datos. Estos elementos se agregarán para lograr algo más complejo.

Si los servicios se comunican entre sí, necesitaremos definir un *service bus*.

SOA no es únicamente la definición de arquitecturas, sino un paradigma orientado al ámbito corporativo. Se complementa con el concepto de BPM (*Business Process Management*):

> "... discipline involving any combination of modeling, automation, execution, control, measurement and optimization of business activity flows, in support of enterprise goals, spanning systems, employees, customers and partners within and beyond the enterprise boundaries" Palmer, Nathaniel.

La tecnología para desarrollar estas arquitecturas fue:

- *Web services*, con SOAP + HTTP
- *Enterprise Service Buses*, utilizados para emitir y receptar eventos.
- *Service repository and discovery*, para encontrar los servicios

## Microservicios

Los encapsulan un concepto, y estan compuestos por un servidor web y una base de datos.

A diferencia de SOA, , y una base de datos. Es un enfoque con mayor granularidad.

Internamente, los servicios se comunicarán entre sí. Los clientes se comunicarán con aplicaciones y un gateway que conocerá la ubicación de los servicios.

![[Service Oriented Architectures 1737417009.png]]

## Transición de Arquitecturas

Hay muchos sistemas que trataron/tratan de migrar de una aplicación monolítica, a una arquitectura de microservicios. Esta es una migración difícil de lograr, ya que son enfoques muy distintos.

![[Service Oriented Architectures 1737417286.png]]
