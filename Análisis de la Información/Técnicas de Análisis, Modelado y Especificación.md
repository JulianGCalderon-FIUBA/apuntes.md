Esta ingeniería parte de una base de necesidades del usuario para generar requisitos. Los requisitos pueden ser descritos desde distintos puntos de vista:

- **Requisitos de Negocio:** Desde el punto de vista de la organización que solicita el software. Utilizaremos artefactos como el documento de visión, concepto de operación, especificación de requisitos de negocio (BRD)
- ***Requisitos de Usuario:*** Desde el punto de vista del usuario final. Utilizaremos estrategias de caja negra, describiremos únicamente la interacción de los actores con el sistema, sin detalles internos. Podremos utilizar casos de uso, historias de usuario, Especificación de requisitos de usuario (URD).
- ***Requisitos de Software:*** Desde el punto de vista de los desarrolladores. A veces hay una capa mayor, denominada requisitos del sistema. No es un documento de diseño, sino una descripción abstracta de lo que deberá hacer, independientemente de la implementación. Se utiliza el documento SRS (especificación de requisitos de software).

Para cada uno de estos puntos de vista, usualmente se producen distintos documentos llamados especificaciones de requisitos. Los nombres de los documentos variarán de la audiencia y el alcance, pero el propósito colectivo es invariable: acordar entre las partes los requisitos del software a desarrollar.

## Representación

Existen diversas formas de representación para los requisitos:

- Lenguaje natural: Debemos tener cuidado con la ambigüedad
- Modelos visuales: Explicar cambios, flujos de datos, funcionalidades
- Especificaciones formales: Se utiliza lenguaje matemático muy preciso.

La mayoría de las veces utilizamos una combinación de las primeras dos opciones.

## Tipos de Documentos

### Visión (y Alcance)

- Es desarrollado en las primera fases/iteraciones. Define el sistema a desarrollar desde el punto de vista de las partes interesadas.
- Es la base para especificaciones mas detalladas que se desarrollarán posteriormente. A veces, también sirve de base para la elaboración de un contrato.
- Puede incluir una definición del problema a resolver o de la oportunidad de negocio a aprovechar, una descripción de los usuarios e interesados, una descripción de las prestaciones del producto/sistema a desarrollar (a muy alto nivel), riesgos, valor para el negocio, supuestos, restricciones, etc.

### Especificación de Requisitos de Software

Usualmente representado en lenguaje natural, complementado con gráficos de, por ejemplo, casos de uso y reglas de negocio. Suele estar relacionado a ciclos de desarrollo clasicos (secuenciales), o proyectos donde hay contratos de por medio.

### Desarrollo Ágil

En entornos ágiles, es difícil encontrarse con documentos como los vistos anteriormente. Se utilizan historias de usuario, como recordatorios de conversaciones con los especialistas o usuarios.

### Modelos

Los modelos reflejan las abstracciones del dominio del problema, describen el sistema en términos tecnológicamente neutros. Pueden ser formales o informales.

## Atributos de Buena Especificación

- Correcta: Reflejar las verdaderas necesidades de los usuarios. No debe tener ambigüedades, debe haber una única interpretación posible para cada requisito.
- Completa: Todo lo que se supone que el software debe hacer debe estar incluido en la verificación, todas las respuestas a todas las entradas posibles están incluidas, todas las páginas del documento están numeradas y referenciadas correctamente.
- Verificable: Hay criterios para determinar si el software una vez desarrollado satisface los requisitos
- Consistente: No hay requisitos en la especificación que estén en conflicto entre si o con otros documentos o artefactos
- Entendible: Debe ser entendida por terceros. Se escribirán una sola vez, pero leídos muchas veces.
- Modificable: la estructura debe permitir modificaciones simples ante un cambio en algún requisito
- Independiente del diseño: Describe el comportamiento del sistema, no los detalles de implementación.
- Concisa: No debe ser innecesariamente extensa
- Organizada: Los requisitos deben ser faciles de localizar
- Trazable: Se debe poder encontrar el origen de cada requisito
- Priorizada: Los requisitos tendrá una prioridad asignada.

## Técnicas

### Organización de Requisitos

Nos permite establecer categorías para identificar y ubicar más rápidamente a los requisitos

- Funcional / No Funcional
- Funcionalidad, Usabilidad, Confiabilidad, Desempeño, Facilidad de soporte, etc (FURPS+)
- Por rol de usuario
- Por área o proceso de negocio
- Por evento, casos de uso o escenario.

Debemos definir como reflejamos los cambios en el repositorio y en los demás mecanismos que utilizaremos para registrar requisitos. Debemos entender la relación de cada requisitos con el resto de artefactos del proyecto. Cada requisito debería tener una identificación única, y más atributos asociados. Debemos definirlos independientemente del tipo de herramienta que utilicemos.

### Priorización

Nos permite asegurar que el esfuerzo del equipo esté dirigido hacia el análisis y la implementación de los requisitos más críticos para todos los interesados, son varios los criterios que se pueden utilizar para establecer la prioridad:

- Valor para el negocio
- Riesgos técnicos o de negocio
- Dificultad de implementación
- Regulaciones / politicas.

Existen varias técnicas que se utilizan para este tarea:

- MoSCoW (Must/Should/Could/Won't): Se colocan los requisitos en categorías
- Votación:
- Timeboxing: Se decide la prioridad en función del tiempo de desarrollo disponible.
- Análisis de Riesgo
- Análisis de Decisiones

### Escenarios

Se conoce con este nombre a una familia de técnicas que están orientadas a contar historias acerca de loa que hace la técnica con los sistemas. Nuestro cerebro está socialmente adaptado para contar historias, por lo que es un grupo de técnicas muy familiar.

- **Casos de Uso**: Es una secuencia de acciones realizadas por un sistema que generan un resultado observable de valor para un actor en particular. A cada acción de un actor le corresponde una respuesta del sistema. Usualmente son cajas negras. No dicen como se elabora la respuesta, sino describe la respuesta en si.
- **Historias de Usuario**: Una descripción de la funcionalidad esperada, desde el punto vista de un usuario. No son requisitos en el sentido estricto, sino simplemente un recordatorio. (tienen poca granularidad). Si incluyen criterios de aceptación, entonces constituyen una descripción completa de lo que se espera del comportamiento del sistema.
- **Storyboards (Guiones)**: Son pequeños relatos, en prosa o en forma gráfica, que nos muestran como utilizar el sistema en determinadas circunstancias.

Todas comparten una característica esencial, para identificar los escenarios se propone partir de los objetivos que las distintas categorías tienen con respecto a la utilización del sistema, luego se identifican subobjetivos, estos se satisfacerán a partir de un único escenario.

## Técnicas de Modelado

Presentaremos algunos de los modelos de análisis más populares

### C4

Utilizado para describir la estructura del software. Si bien no está muy relacionado con el análisis los requisitos. Nos permite entender el proyecto y su relación con el contexto. Muestra otros sistemas con los cuales interactuar.

### Modelos de Casos de Uso

Busca representar los casos de uso del sistema y los actores primarios y secundarios con los que el sistema interactúa. Cuando se usa en conjunto con las especificaciones de casos de uso, forman parte del modelo de casos de uso

### Modelos de Dominio

Es una representación visual de los objetos o clases conceptuales del dominio del problema y las asociaciones entre sí.

- Cosas manipuladas en la organización
- Objetos y conceptos del mundo real
- Personas, roles, organizaciones

Sirven para entender y analizar el contexto del sistema a analizar. Se utiliza en combinación con otras técnicas como casos de uso e historias de usuarios.Para utilizarlo, emplearemos un diagrama de clases con la notación ***uml***. No representan objetos del lenguaje de programación, sino objetos de negocio. Es un modelo de análisis, no de diseño

### Árbol de Funcionalidades (Feature Tree)

Se representa con un diagrama similar al de causa y efecto. Tiene como objetivo mostrar las prestaciones y funcionalidades del sistema, y como desglosan en prestaciones más pequeñas.

### Diagrama de Estados

Permite representar los diferentes estados por los que puede pasar un objeto de dominio o sistema. Representarlos usando lenguaje natural puede ser bastante problemático por lo que esta herramienta es muy útil. Para aplicaciones en tiempo real, es fundamental desarrollar este tipo de diagramas

### Diagrama de Actividades

Permite especificar las actividades o pasos dentro un flujo de trabajo, de un proceso, o de un caso de uso.

### Flujo de Actividades en Un Proceso de Negocio (BPMN)

Es un estándar para el modelado de procesos de negocio, ayuda a identificar casos de uso / historias de usuario. Es similar al diagrama de actividades mencionado anteriormente. Sirve para genera un proceso que pueda ser ejecutados.

### Prototipado

No sólo para descubrir requisitos, también es útil para analizarlos. No se deben discutir aspectos de diseño. Se suelen integrar con casos de uso, historias de usuario.

Pueden ser evolutivos o descartables, y hechos con papel y lápiz.

### EARS (Easy Approach to Requirements Syntax)

Es un lineamiento para minimizar los problemas derivados de la ambigüedad cuando utilizamos lenguaje natural. *EARS* propone formatos muy específicos para describir requisitos:

- **Ubicuos:** Algo que el sistema debe hacer incondicionalmente. Son generales y aplican a todo el sistema.
- **Basado en Eventos:** Algo que el sistema debe hacer en respuesta a un evento disparador
- **Basado en Estados:** Algo que se activa mientras se permanece en un estado determinado
- **Opcional:** Algo que necesario solo bajo determinadas circunstancias
- **Comportamiento indeseado:** Una respuesta del sistema a eventos no deseados

### Criterios de Aceptación

Es una estrategia útil para completar la especificación. El simple acto de pensar las condiciones que satisfacen los requisitos ayuda a encontrar problemas en la especificación mucho antes de comenzar el desarrollo del producto.

Agregarle estos criterios a un requisito de usuario lo acerca a la definición clásica de requisitos de software. Ayudan a clarificar su alcance.

### Reglas de Negocio

Son políticas, regulaciones, leyes, y estándares. Puede seguir la siguiente estructura: "Cuando ***<condicion>*** entonces ***<imposición>.*** En caso contrario ***<consecuencias>***". Pueden describir cálculos completos, restricciones, inferencias, o hechos.

### User Story Mapping

Es un modelo que describe las actividades que realizan a lo largo del tiempo los usuario de la aplicación, y como se descomponen en subactividades y tareas.

### Impact Mapping

Tiene como propósito alinear los equipos de trabajo con los objetivos de la organización. Se identifican los objetivos que se buscan satisfacer, luego los actores que serán impactados con la solución, lo que se deberá hacer para producir los impactos.

## Recomendaciones

Algunas recomendaciones **generales**:

- Es importante definir los límites del sistema, de no hacerlo podemos profundizar temas innecesarios
- Debemos prepararnos para gestionar los inevitables conflictos que surgirán
- Clasificar y priorizar los requisitos para destinar los recursos correctamente
- Debemos mantener la trazabilidad de los requisitos (tanto vertical como horizontal). De donde vienen y con que otros requisitos se relacionan.
- Debemos evaluar riesgos para poder priorizar aquellos que impliquen un nivel de riesgo por encima de determinado umbral.
- En todo caso, debemos evitar la parálisis del análisis. Debemos eventualmente concluir el análisis para continuar el proyecto.

En cuanto al **modelado**:

- Definir que modelos pueden aportar al análisis, no todos son útiles en todas las situaciones. Los modelos deben mantener consistencia entre sí.
- Debemos decidir que modelos deben ser formalizados, algunos modelos merecerán tener una versión electrónica que podamos compartir.
- Debemos considerar diversos aspectos del sistema a modelar
- El prototipado es una técnica muy adecuada para explorar requisitos poco claros o riesgosos.

En cuanto a la **especificación**:

- Debemos determinar el nivel de formalidad de las especificaciones, dependerá del tamaño de equipo y de la dispersión geográfica. A veces bastará con historias de usuario, pero a veces necesitamos documentos más formales.
- Definir estándares para especificar requisitos
- Siempre es importante ser claros, independientemente de la formalidad.
- De ser posible, debemos expresar requisitos de forma cuantitativa
- Podemos definir un glosario para entender fácilmente el vocabulario de negocio
