Es un servicio de [[Computación Cloud#Platform as a Service (PaaS)|PaaS]] de Google, iniciado en 2008. Ofrece servicios gratuitos y servicios de pago.

## Objetivos de Diseño

El concepto consiste en una plataforma donde las buenas prácticas son forzadas:

- Los sistemas son granulares.
- El escalamiento es horizontal.
- Las consultas son breves, con posibilidad de encolar consultas largas.
- Independencias del sistema operativo y el hardware.

Además, ofrece los siguientes servicios:

- Cache.
- Colas de mensajes.
- Elasticidad.
- Versionado.
- Herramientas de *logging*, *debugging*, monitoreo, etc.
- Modelos no-relacionales con Datastore y BigTable.

## Microservicios

Se definen aplicaciones que pueden comunicarse entre sí. Cada aplicación tiene servicios, que pueden comunicarse entre sí.
