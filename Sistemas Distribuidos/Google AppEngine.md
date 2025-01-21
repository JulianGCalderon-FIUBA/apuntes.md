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

Una instancia (app servers o backend servers) es una unidad de procesamiento, que uede ser dinámica o residente:

- Instancias dinámicas:
	- Se crean dinámicamente, aunque hacerlo toma un poco de tiempo.
	- Procesan consultas pequeñas.
	- Fuerzan respuestas rápidas y sin manejo de estado.
	- Pueden aceptar consultas externas o internas.
- Instancias residentes:
	- Son creadas de forma manual mediante configuración. A veces es preferible tener instancias precalentadas (*warmed up*) para evitar el costo de inicio ante una consulta.
	- No existen límites para su empleo y se pueden elegir su capacidad de cómputo
	- Procesas consultas largas, especialmente en baches (con o sin estado)

## Arquitectura

Hay *front servers* que reciben peticiones, responden las que ya tiene cacheadas. Las consultas que no pueden ser resueltas son reenviadas a la aplicación.

![[Google AppEngine 1737426237.png]]

Las consultas llegan a una cola de tipo *push*. En lugar de esperar a que otro proceso tome el mensaje, la cola es un elemento activo que puede crear instancias de forma dinámica. Además, puede actuar como balanceo de carga.

![[Google AppEngine 1737427429.png]]

Las consultas largas van a otras colas de tipo *pull* para ser resueltas de forma asincrónica, por un proceso residente.

Las instancias acceden a un almacenamiento compartido.

## Tipos de Colas

Hay dos tipos principales de colas:

- Colas de push:
	- Envían consultas a instancias activas.
	- La URL define la instancia, servicio, y versión a atender el mensaje
	- El payload está dado por los argumentos en la URL y los headers
