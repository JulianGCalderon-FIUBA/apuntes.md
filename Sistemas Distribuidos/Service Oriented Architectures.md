## Monolíticas

Esta fue la arquitectura más usada en la historia del internet. A medida que crece el sistema, crece el *web server*.

- **Reverse Proxy**: Resuelve consultas más simples, como la de archivos estáticos.
- **Web Server**: Resuelve consultas más complejas, relacionadas con la lógica de negocio.
- **Database Server**: Base de datos que almacena el estado del sistema.

![[Service Oriented Architectures 1737415456.png]]

Si los servidores pueden ser replicado, entonces estas arquitecturas son escalables:

![[Service Oriented Architectures 1737415688.png]]

Esto nos da la posibilidad de rutear consutlas según distintos criterios, como ubicación, o afinidad de los datos.
