Es un modelo propuesto por Krutchen, que consiste en generar 5 diagramas distintos (vistas).

## Vista Lógica

Apoya principalmente los requisitos funcionales. Lo que el sistema debe brindar en términos de servicios a sus usuarios.

Aquí se aplican los principios de abstracción, encapsulamiento y herencia. Esta descomposición no solo se hace para potenciar el análisis funcional, sino también sirve para identificar mecanismos y elementos de diseño comunes a diversas partes del sistema.

Se suele utilizar un diagrama de lógica o estados.

## Vista de Procesos

La vista de procesos toma en cuenta algunos requisitos no funcionales tales como el rendimiento y la disponibilidad.

Se enfoca en asuntos de concurrencia y distribución, integridad del sistema, de tolerancia a fallas.

Un proceso es una agrupación de tareas que forman una unidad ejecutable. Los procesos representan el nivel al que la arquitectura de procesos puede ser controlada tácticamente. Además, los procesos pueden replicarse para aumentar la distribución de la carga de procesamiento, para mejorar la disponibilidad.

Se suele utilizar un diagrama de clases.

## Vista de Componentes

La vista de componentes (o de desarrollo) se centra en la organización real de los módulos de software en el ambiente de desarrollo de software.

El software se empaqueta en partes pequeñas - bibliotecas de programas o subsistemas - que pueden ser desarrollados por uno o un grupo pequeño de desarrolladores.

La vista de desarrollo tiene en cuenta los requisitos internos relativos a la facilidad de desarrollo, administración del software, reutilización y elementos comunes, y restricciones impuestas por las herramientas o el lenguaje de programación que use.

Se suele utilizar un diagrama de componentes (similar a un diagrama de clases).

## Vista Física

La vista física (o de despliegue) toma en cuenta primeramente los requisitos no funcionales del sistema como la disponibilidad, confiabilidad, rendimiento, y escalabilidad.

El software se ejecuta sobre una red de computadores o nodos de procesamiento. Los variados elementos identificados - redes, procesos, tareas y objetos - requieren ser mapeados sobre los nodos.

Esperamos que diferentes configuraciones puedan usarse: algunas para desarrollo y pruebas, otras para mostrar el sistema en varios sitios para distintos usuarios. Por lo tanto, la relación del software en los nodos debe ser altamente flexible y tener un impacto mínimo sobre el código fuente.

## Vista de Escenarios

Los elementos de las cuatro vistas trabajan conjuntamente en forma natural mediante el uso de un conjunto pequeño de escenarios relevantes.

Los escenarios son de alguna manera una abstracción de los requisitos más importantes. Sirve para dos propósitos principales:

- Como un guía para descubrir elementos arquitectónicos durante el diseño de arquitectura.
- Como un rol de validación e ilustración después de completar el diseño de arquitectura, en el papel y como un punto de partido de las pruebas de un prototipo de la arquitectura.
