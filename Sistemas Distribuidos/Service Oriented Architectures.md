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

Si tenemos distintas necesidades en las aplicaciones, y queremos asignar recursos según la aplicación en lugar de todas por igual, surge la necesidad de realizar aplicaciones orientadas a servicios.

![[Service Oriented Architectures 1737416013.png]]

En estos sistemas, los clientes acceden al registro de servicios
