Una historia de usuario es una descripción de la funcionalidad esperada de un sistema, expresada desde el punto de vista del usuario:

> [!note]
> El formato más aceptado es el denominado quién-qué-porque: Como <actor>, quiero poder <función> de modo que/para asi <razón>


No son requisitos en el sentido tradicional, sino que constituyen un recordatorio de que se debe mantener una conversación respecto al tema en cuestión.

Esto da origen al concepto de las tres ‘C’s

# Card, Conversation, Confirmation

Se separa en tres elementos

- **Card**: Descripción de la intención del usuario al utilizar el sistema, registrada en una ficha
- **Conversation**: Se debe mantener una conversación respecto a la historia para descubrir los detalles
- ***Confirmation:*** Se deben definir criterios de aceptación para garantizar que se han cubierto  todos los aspectos de la historia.

> [!note]
> El formato para los criterios de aceptación puede ser: Dato que soy <actor>, Cuando <acción> entonces <resultado>


## Epopeya

Para resolver el problema del manejo de numerosas historias de usuario, aparece el concepto de é*pica* o de epopeya***.*** Consiste en agrupar historias en relatos de mayor nivel, llamados épicas.

![[Apuntes/Análisis de la Información/Attachments/Historias de Usuario 1.png|Podemos dar nombres a las historias para identificarlas fácilmente]]

Podemos dar nombres a las historias para identificarlas fácilmente

# Calidad de las historias de usuario

## Regla INVEST

Criterio para determinar si la historia de usuario es correcta:

- **I:** independiente (de otras historias)
- **N:** negociable (una declaración flexible, no un contrato)
- **V:** valiosa (aporta valor al cliente o al usuario)
- **E**: estimable (se puede estimar)
- ***S:*** pequeña ( se puede desarrollar dentro de una iteración)
- ***T: v***erificable (se entiende lo suficiente como para poder ser probada.

## QUS Framework

Marco de referencia que propone 13 atributos de calidad:

- Calidad sintáctica:
    - **Bien formada:** Debe incluir al menos un rol y una acción
    - **Atómica:** Debe expresar una únicamente funcionalidad
    - **Mínima**: Solo contiene un rol, acción, y fin.
- Calidad semántica:
    - **Conceptualmente acertada:** La acción expresa una funcionalidad y el fin una razón
    - **Orientada al problema:** No debe especificar la solución
    - **No ambigua:** Debe evitar múltiples interpretaciones
    - **Libre de conflictos:** Debe ser consistente con otras historias de usuario
- Calidad pragmática
    - **Oración completa:** Debe ser una oración bien formada
    - **Estimable:** Debe poder ser estimada y planificada
    - **Única:** No debe haber duplicados
    - **Uniforme:** Todas las historias de usuario emplean el mismo formato
    - **Independiente:** No debe depender de otras historias, debe ser autocontenido
    - **Completa:** No faltan pasos

Este criterio considera opcional el *¿porqué?*, aunque nosotros lo consideramos necesario.

# ¿Como encontrarlas?

Primero debemos entender cuales son los límites del sistema que estamos analizando y quienes lo utilizan. Luego para cada usuario,debemos identificar sus objetivos y la funcionalidad esperada del sistema. Los objetivos pueden incluir una jerarquía de los objetivos. Al final de la jerarquía, podemos encontrar historias de usuario para cada sub objetivo.

## User Story Mapping

Es un posible enfoque para descubrir historias de usuario, describe las actividades que realizan a lo largo del tiempo los usuario de una aplicación y su descomposición en subactividades y tareas. A partir de las tareas podemos identificar historias de usuario. Cada subactividad tenrdra al menos una tarea asociada.

![[Apuntes/Análisis de la Información/Attachments/Historias de Usuario 2.png|Untitled]]

## Impact Mapping

Técnica de planificación que tiene como propósito alinear los equipos de trabajo con los objetivos de la organización

![[Apuntes/Análisis de la Información/Attachments/Historias de Usuario 3.png|Untitled]]

## Proceso de Desarrollo

En el proceso de desarrollo, asignaremos historias de usuario a las distintos ***releases*** del proyecto

![[Apuntes/Análisis de la Información/Attachments/Historias de Usuario 4.png|Untitled]]

## Product & Sprint Backlogs

En ***SCRUM***, las historias de usuario se almacenan en el ***product backlog*** y son seleccionadas para determinados ***sprints***. Cada historia se estima utilizando una técnica llamada ***user story points,*** que nos permite analizar la complejidad de las historias de usuario. A partir de las historias seleccionadas se determinan las tareas a realizar, en el ***sprint backlog***.

![[Apuntes/Análisis de la Información/Attachments/Historias de Usuario 5.png|Untitled]]

## Kanbag

Es un sistema de planificación y organización del trabajo. Su objetivo es ayudar a darle visibilidad al trabajo y limitar el trabajo en simultaneo, mejorando el flujo de trabajo. 

Tendremos una tarjeta por cada historia de usuario y por cada defecto encontrado en el ***software***. Las historias de usuario se moverán por el tablero para indicar el estado de las mismas.

![[Apuntes/Análisis de la Información/Attachments/Historias de Usuario 6.png|Untitled]]

# Niveles de Objetivos

Propuestos por Alistar Cockurn. Separan los objetivos en cuatro niveles:

- **Cloud level:** High summary level. Objetivos de negocio, son aquellos que llevan el negocio a la dirección requerida
- **Kite level:** Sumary level. Objetivos alcanzados por procesos de punta a punta dentro de los sistemas. Pueden tomar icho tiempo en ser alcanzados
- **Sea level:** User goal level. Pueden ser realizados por una sola persona, contribuyen a la entrega de un objetivo completo
- **Fish level:** Sub goal level. No son objetivos en si, si no que se utilizan para completar los objetivos y separarlos.

# Criterios de Aceptación

Una forma de definir un criterio, es define el escenario, un contexto específico, el evento, y el resultado esperado

![[Apuntes/Análisis de la Información/Attachments/Historias de Usuario 7.png|Untitled]]