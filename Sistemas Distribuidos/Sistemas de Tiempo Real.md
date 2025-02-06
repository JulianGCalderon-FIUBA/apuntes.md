Un sistema de tiempo real, o *real time* Es un sistema cuya evolución se especifica en términos de requerimientos temporales requeridos por el entorno. La correctitud del sistema depende de que entregue respuestas correctas y en tiempo correcto.

Algunos ejemplos son:

- Electrodomésticos digitales
- Medidores de señales (presión, pulsaciones)
- Mediciones por sensores
- Control de automóviles
- Control de aeronaves
- Marcapasos

Un sistema es de tiempo real si tiene al menos un servicio de tiempo real.

## Tipos de Real Time

Hay dos tipos principales de servicios en real time:

- **Hard RT**: Se debe evitar todo fallo relacionado con el tiempo de delivery. Perder un deadline o plazo de respuesta es un fallo total. Por ejemplo: Control de aeronaves.
- **Soft RT**: Los fallos relacionados con el tiempo de delivery pueden ser admitidos ocasionalmente. La utilidad de un resultado disminuye tras el deadline. Por ejemplo: Servicio de streaming.

## Previsibilidad

El concepto de real time implica previsibilidad, no performance. Un sistema veloz, pero sin previsibilidad no es de tiempo real, mientras que un sistema previsible con tiempos característicos lentos lo son.

Se trata de hacer un correcto *scheduling* para que se cumplan los plazos previstos por diseño.
