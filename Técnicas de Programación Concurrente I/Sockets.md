Son una herramienta del sistema operativo que permiten hacer comunicación entre dos procesos que estén, o bien en la misma computadora, o bien en computadoras distintas. Se utilizan para implementar un modelo de cliente-servidor:

## Modelo de Capas

Los protocolos de internet suelen ser ordenados en capas. Las capas le ofrecen servicios a sus capas superiores, y utilizan los servicios de las capas inferiores. Las capas de igual número en distintas computadoras se comunican virtualmente a partir del protocolo.

![[Sockets 1697723178.png|447]]

Este modelo se conoce como protocolo de capa $N$.

## Servicios

Los protocolos de capa de transporte pueden proveer distintos servicios:

- **Sin conexión:** Los datos se envían al receptor y no hay control de flujo ni de errores. Por ejemplo: UDP.
- **Sin conexión con ACK:** Por cada dato recibido, el receptor envía un acuse de recibo conocido como ACK.
- **Con conexión:** Tiene tres fases: Un establecimiento de la conexión, intercambio de datos, y cierre de la conexión. Hay control de flujo y de errores. Por ejemplo: TCP.
