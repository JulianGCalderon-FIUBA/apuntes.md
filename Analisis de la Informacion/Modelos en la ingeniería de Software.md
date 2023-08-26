Un modelo es una simplificación de la realidad, construimos modelos para entender mejor el sistema que estamos desarrollando. Estos permiten

- Visualizar un sistema
- Especificar la estructura o el comportamiento de un sistema
- Proveer un guía para la construcción de un sistema
- Documentar las decisiones tomadas

## Influencia del Lenguaje de Programación

Idealmente, los modelos empleados en el análisis deberían reflejar el dominio del problema. Los modelos empleados en el diseño deberían reflejar las abstracciones naturales del lenguaje de programación.

En consecuencia, la transición entre el análisis y el diseño no siempre es fácil. La orientación a objetos provee una transición más natural debido a su similitud con la realidad.

## UML

Surge de mezclar las notaciones más populares de la época. Es un lenguaje gráfico que se utiliza para modelar sistemas basados en software. Ofrece diversos tipos de diagramas

- **Diagrama de Clases:** Muestra la estructura interna y estática del sistema. Describe las clases, interfaces y las colaboraciones o relaciones entre las mismas.
- **Diagrama de Casos de Uso:** Muestra la funcionalidad provista por el sistema y su interacción con los usuarios a alto nivel. Describe los actores, casos de uso y las relaciones entre sí. Es un diagrama de muy alto nivel
- **Diagrama de Secuencia:** Muestra la interacción entre una secuencia de clases para completar una acción. Describe las clases y los mensajes con los que interactúan entre sí.
- **Diagrama de Estados:** Muestra el ciclo de vida de una clase o colaboración. Describe los estados de una clase y las transiciones entre los mismos a través de elementos y actividades.
- **Diagrama de Actividad:** Muestra el flujo de actividades al o largo de un ciclo de trabajo. Describe las actividades, los objetos, las transiciones y las decisiones tomadas.

> [!note]
> El BPMN *(Business Process Modeling and Notation)* es similar al UML, pero busca representar un proceso de negocio.

## C4

Tiene como propósito representar la arquitectura del software. Propone una estructura de diagramas en niveles.

1. **Diagrama de Contexto:** Muestra el medio ambiente en el cual funcionará el sistema.
2. **Diagrama de Contenedores:** Busca separar el sistema en distintas aplicaciones, cada una con funcionalidad específica.
3. **Diagrama de Componentes:** Muestra cada contenedor en particular, describe la implementación del componente
4. **Diagrama de Código:** Si es necesario, busca representar el código que forma parte un componente.

Este enfoque combina una notación muy sencilla de la arquitectura, en conjunción con UML para los detalles de implementación, es un enfoque más simple que permite representar la abstracción completa del sistema.
