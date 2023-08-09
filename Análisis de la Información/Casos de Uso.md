> [!note]
> Definición Una historia acerca de cómo un actor utiliza un sistema para alcanzar sus objetivos. Más formalmente, una secuencia de acciones realizadas por un sistema que generan un resultado observable de valor para un actor particular

> [!note]
> Actor: Una entidad con algún tipo de comportamiento que interactúa con el sistema: personas, organizaciones, otros sistemas.

Los casos de uso son tecnológicamente neutros (esenciales). No describen la solución ni aspectos de implementación. (ni siquiera aquellos relacionados con la interfaz del usuario).

También se pueden representar visual, en un diagrama de casos de uso de UML.

Los casos de uso están compuestos por escenarios. Normalmente encontraremos un escenario principal (camino feliz), y uno o varios escenarios alternativos o secundarios.

Un caso de uso describe un contrato entre las partes interesadas acerca del comportamiento de un sistema. Este comportamiento describe que responde el sistema a las acciones de una de las partes interesadas, en particular el actor primario. El actor primario inicia una interacción con el sistema para lograr algún objetivo. El sistema responde protegiendo los intereses de todas las partes interesadas. El caso de uso recoge diferentes escenarios que son el resultado de distintas condiciones y acciones de los actores.

Si bien perdieron protagonista hoy en día, tienen su lugar en situaciones particulares.

## Formatos

El formato breve simplemente contiene un título escrito en verbo en voz activa mas un objeto, y una descripción resumida del comportamiento.

![[Casos de Uso 1.png]]

El formato de secuencia de acciones, se describen las acciones del actor y las respuestas una por una, de forma detallada. El sistema se describe como una caja negra, no muestra como se elabora la respuesta.

![[Casos de Uso 2.png]]

El formato de dos columnas o diálogo, se separan las acciones en dos columnas separadas. Una para el actor y otra para el sistema.

![[Casos de Uso 3.png]]

El formato más completo, contiene precondiciones, poscondiciones,m y escenarios alternativos. También es usual agregar una sección para describir los requisitos no funcionales asociados al caso de uso

![[Casos de Uso 4.png]]

## ¿Como Encontrarlos?

1. Es importante establecer / entender los límites del sistema. Que influiremos y que dejaremos afuera.
2. Debemos identificar los actores primarios y sus objetivos.
3. Para cada objetivo, encontraremos un caso de uso.
4. Para cada caso de uso:
	1. analizaremos sus pre y post condiciones
	2. Describiremos sus escenarios principales.
	3. Buscaremos los escenarios alternativos
	4. Refinaremos y ajustaremos los casos. Buscamos relaciones de inclusión, de extensión, y especializaciones

### Relaciones de Inclusión

Si encontramos que mucho comportamiento se repite en varios casos de uso, crearemos un nuevo caso de uso y lo invocaremos los casos de uso que lo necesiten los llamados casos base. La relación se dibuja con una línea punteada desde el caso de uso base al caso de uso incluido.

![[Casos de Uso 5.png]]

### Relaciones de Extensión

Cuando en un caso de uso encontramos comportamiento adicional u opcional, también podemos crear un nuevo caso de uso para ubicar esas acciones. En este caso, pagar con tarjeta de crédito extiende el comportamiento de vender productos.

![[Casos de Uso 6.png]]

### Relaciones de Generalización

También encontraremos situaciones donde es necesario especializar un caso de uso. Debemos indicar que comportamiento se hereda sin cambiar, cual se especializa, y cual es nuevo y propio de la especialización

![[Casos de Uso 7.png]]

## Adicionales

A partir de cada caso de uso, se pueden identificar casos de prueba. Que debe probarse en cada escenario, bajo que condiciones, con que datos, etc.

También vamos a encontrarnos con que en los casos de usa se mencionan objetos de negocio, asociaciones, atributos, propiedades. Todos ellos deben existir en el modelo de dominio.

## CRUD/ABMC

CRUD es un concepto, y un acrónimo de *Create, Read, Update, y Delete*, o en español, *Altas, Bajas, Modificaciones, Consultas.* Consiste en agrupar operaciones bajo estas categorías.

Debe haber casos de uso que permitan custodiar las entidades del modelo de dominio. A veces será mostrar casos de uso independientes para el alta, la baja, la modificación, y la consulta. Otras veces, será mejor unificarlos en un único diagrama de casos de uso.

## Procesos Unificado

Conjunto de disciplinas que en conjunto forman el proceso de software. En el proceso unificado los casos de uso juegan un papel importante ya que en relación a ellas se realizan las actividades.

Para adecuar los distintos aspectos, es necesario incluir más de una vista o perspectiva.

![[Casos de Uso 8.png]]

La vista central se representa mediante casos de uso. Los casos de uso se diagraman en notación UML.

Con esta información se propone desarrollar el modelo de análisis es una descripción de la realización de cada caso de uso. Se describe el comportamiento interno del sistema en términos tecnológicamente neutros, necesarios para elaborar las respuestas a los actores descritos en los casos de uso.

En este modelo el comportamiento se describe con objetos de análisis, abstracciones con propiedades y comportamiento, que colaboran entre sí para elaborar la respuesta que necesitan los actores. Pueden ser entidades, objetos de interacciones, y objetos de control.

A partir del modelo de análisis, se da lugar al modelo de diseño

## Contratos Y Operaciones

*á la Larman* propone un modelo de casos de uso más completo que además de los casos de uso propiamente dichos, contiene contratos y operaciones. Nos encontraremos con diagramas de secuencia y contratos para cada operación

Una operación se dispara como resultado de un evento, como resultado de la operación se pueden producir cambios en los objetos de demonio. Cada operación debe ser definida mediante un contrato. No estamos hablando de la implementación, sino de la esencia del sistema.

El contrato de la operación incluye:

- Nombre de la operación y parámetros
- Responsabilidades
- Precondiciones
- Post condiciones

Con estas descripciones complementamos lo que hace el sistema.

## Casos de Uso 2.0

La novedad más importante es que los casos de uso en esta nueva versión son un conjunto de historias que ayudan a organizar las slices en las que se divide un caso de uso.
