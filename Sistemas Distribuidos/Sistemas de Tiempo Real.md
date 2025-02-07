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

El scheduling es importante, y debe ser apropiativo (non-preemptive), y de acuerdo a un esquema de prioridades para poder cumplir deadlines.

## Comunicaciones

Un sistema real time requiere comunicación fiable y sincrónica (con deadlines bien definidos):

- La comunicación TCP/IP no permite asegurar estos atributos. No se asegura un deadline sobre el tiempo.
- La comunicación serial permite controlar estos atributos. Ya hay productos comerciales que proveen garantías: Profibus.
- Ethernet puede ser utilizado, pero con un protocolo adecuado.
	- Se requiere evitar el no determinismo en el protocolo. Esto solo puede ocurrir en caso de colisiones en la transmisión.
	- Existen protocolos que ya cumplen con esto, por ejemplo: Profinet.

Se busca evitar algoritmos de backoff, ya que aumentan la imprevisibilidad del sistema.

## Tolerancia a Fallos

Los sistemas de **real time** deben además ser tolerantes a fallos de tiempo.

Hay distintas estrategias para tratar con fallos temporales:

- **Hard RT**: Son sistemas de misión crítica, y suelen ser sistemas de control. Frente a errores, se asume un fallo catastrófico y se debe reiniciar el sistema. En estos casos es importante que el sistema sea mantenible, para que se pueda recuperar de forma barata, rápida y consistente.
- **Soft RT**: Si la restricción no se cumple, entonces se degrada el servicio, pero no es catastrófico. Un ejemplo son los sistemas web de gran escala. Una posible restricción es: el 90% de los requests deben responderse en 2 segundos, mientras que el 10% restante debe responderse en a lo sumo 10 segundos.

## Paradigmas de Trabajo

Hay dos paradigmas de trabajo. En los sistemas **event-triggered**, hay un actor que hace consultas, y otro que responde (denotado como servidor, pero puede ser cualquier cosa, como un sensor).

El cliente solo puede controlar sus propios tiempos, y se deben proveer garantías sobre los deadlines en la comunicación, o en el procesamiento por parte del servidor.

![[Sistemas de Tiempo Real 1738887182.png]]

En los sistemas **time-triggered**, se definen *time slots*, y dentro de cada uno se emiten eventos. Estos eventos pueden demandar respuesta, y las garantías sobre estas respuestas están definidas en base a los *time slots* (por ejemplo, la respuesta debe llegar en el propio *time slot*, o el siguiente).
