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

A su vez, los servicios tienen su capa de caché, su capa de datastore, y un servicio de colas. Hoy en día, estos servicios se ofrecen por separado.

![[Google AppEngine 1737425829.png]]

Un servicio (módulo), que permite mantenerr unidad entre las operaciones soportadas. Pueden desplegarse distintas versiones a la vez, y para cada versión pueden existir una o más instancias.

Una instancia (app servers o backend servers) es una unidad de procesamiento. Puede ser dinámica o residente. Las dinámicas se crean automáticamente al recibir consultas, mientras que las residentes se escalan de forma manual.

Crear una instancia puede tomar cierto tiempo, por lo que a veces es preferible definir instancias residentes.

## Arquitectura

Hay data centers

![[Google AppEngine 1737426237.png]]
