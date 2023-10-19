Son una herramienta del sistema operativo que permiten hacer comunicación entre dos procesos que estén, o bien en la misma computadora, o bien en computadoras distintas. Se utilizan para implementar un modelo de cliente-servidor:

## Servicios

Los protocolos de red pueden proveer distintos servicios:

- **Sin conexión:** Los datos se envían al receptor y no hay control de flujo ni de errores. Por ejemplo: UDP, IP.
- **Sin conexión con ACK:** Por cada dato recibido, el receptor envía un acuse de recibo conocido como ACK.
- **Con conexión:** Tiene tres fases: Un establecimiento de la conexión, intercambio de datos, y cierre de la conexión. Hay control de flujo y de errores. Por ejemplo: TCP.

## Tipos de Sockets
