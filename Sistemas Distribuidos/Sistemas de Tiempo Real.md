Un sistema de tiempo real, o *real time* Es un sistema cuya evolución se especifica en términos de requerimientos temporales requeridos por el entorno. La correctitud del sistema depende de que entregue respuestas correctas y en tiempo correcto.

Algunos ejemplos son:

- Electrodomésticos digitales
- Medidores de señales (presión, pulsaciones)
- Mediciones por sensores
- Control de automóviles
- Control de aeronaves
- Marcapasos

Un sistema es realtime si tiene al menos un servicio real time.

## Tipos de Real Time

Hay dos tipos principales de servicios en real time:

- **Hard RT**: Se debe evitar todo fallo relacionado con el tiempo de delivery. Perder un deadline o plazo de respuesta es un fallo total. Por ejemplo: Control de aeronaves.
- **Soft RT**: Los fallos relacionados con el tiempo de delivery pueden ser admitidos ocasionalmente. La utilidad de un resultado disminuye tras el deadline.

## Previsibilidad

El concepto de real time implica previsibilidad, no performance. Un sistema veloz, pero sin previsibilidad no es de tiempo real, mientras que un sistema previsible con tiempos característicos lentos lo son.

Se trata de hacer un correcto *scheduling* para que se cumplan los deadlines previstos por diseño.

## Comunicaciones

Un sistema real time requiere comunicación fiable y sincrónica (con deadlines bien definidos):

- La comunicación TCP/IP no permite asegurar estos atributos. No se asegura un deadline sobre el tiempo.
- La comunicación serial permite controlar estos atributos. Ya hay productos comerciales que proveen garantías: Profibus.
- Ethernet puede ser utilizado, pero con un protocolo adecuado. Ya hay protocolos que lo cumplen: Profinet.
	- Se requiere evitar el no determinismo en el protocolo.
