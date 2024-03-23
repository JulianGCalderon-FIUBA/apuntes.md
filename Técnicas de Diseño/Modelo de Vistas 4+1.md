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

La vista de desarrollo se centra en la organización real de los módulos de software en el ambiente de desarrollo de software.

El software se empaqueta en partes pequeñas - bibliotecas de programas o subsistemas - que pueden ser desarrollados por uno o un grupo pequeño de desarrolladores.

La vista de desarrollo tiene en cuenta los requisitos internos relativos a la facilidad de desarrollo, administración del software, reutilización y elementos comunes, y restricciones impuestas por las herramientas o el lenguaje de programación que use.

Se suele utilizar un diagrama de componentes (similar a un diagrama de clases).

## Vista Física


