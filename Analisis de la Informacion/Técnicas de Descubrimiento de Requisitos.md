Utilizamos la palabra descubrimiento debido a que los requisitos no están en la mente de los usuarios listos para ser recolectados, sino que tenemos que descubrirlos a través de un esfuerzo cooperativo entre los interesados y los desarrolladores.

## Dificultades

Las dificultades no son técnicas, sino sociales: los clientes muchas veces no saben lo que quiere, y cuando lo saben, no son capaces de articular sus objetivos. Nuestra falsa de experiencia en el dominio del problema agrega dificultad extra en esta tarea. Finalmente, los factores organizacionales y políticos juegan un papel importante en este proceso, lo convierten en un juego de negociación. Los cambios económicos abruptos también impactan en los requisitos.

## Interesados

El *onion model* es un diagrama que consiste en colocar los interesados con el problema según su cercanía al servicio que provee el producto. Sirve para modelar la relación entre los interesados:

- En la capa más cercana, encontraremos los usuarios finales que interactuarán con el sistema, esta capa junto al producto se denomina el sistema.
- En la siguiente capa nos encontraremos con los beneficiarios económicos o funcionales, los responsables de mantener en funcionamiento la solución y otros sistemas que interactuarán como interfaces con la última capa.
- La última capa es la del medio ambiente. Aquí encontraremos a los beneficiarios funcionales, los entes reguladores, auspiciadores económicos, etc. Por otro lado, aquí estarán los interesados negativos, aquellos que atacan la idea del nuevo sistema por diversas razones.

## Entrevistas

Son reuniones en las que se dialoga con uno o más interesados con el propósito de obtener información. Puede ser estructurada (cuando se elaboran listas de preguntas con anticipación) o desestructuradas (o mixtas). Tiene algunas desventajas

Se obtienen limitados puntos de vista, lo que nos deja puntos de vista por resolver. Por otro lado, existe un conocimiento tácito desde el lado de los entrevistados. Es necesario invocar a los representantes adecuados, saber escuchar, saber preguntar, y documentar las respuestas, y prepararlas con anticipación.

## Observación

La observación puede ser pasiva (solo se observa) o activa (hacer el trabajo bajo supervisión). Debemos saber preguntar y saber escuchar, así como documentar las observaciones. Es una técnica fácil que tiene algunas limitaciones. Puede no ser suficiente para alcanzar nuevos requisitos, ya que solo se observa el comportamiento actual, también puede no detectar eventos inusuales

## Talleres

Consiste en reunir un grupo de expertas con el objetivo común de encontrar una solución a un problema compartido. Son actividades intensas y de duración limitada que debe ser correctamente gestionada. Se busca que los *stakeholders* discutan las diferencias y puedan llegar a un acuerdo.

## Encuestas

Tienen como propósito obtener información de mucha gente en un tiempo acotado. Las preguntas pueden ser cerradas o abiertas (requiere más análisis)

## Focus Groups (Grupos de Discusión)

Es una discusión moderada por un moderador (participan de 5 a 10 personas). Tiene como propósito obtener ideas, percepciones y actitudes acerca de un producto. Es muy útil cuando el software apunta al mercado masivo. Es importante tener un buen moderador y activa participación de los integrantes.

## Análisis de Reglas de Negocio

Son directivas específicas y verificables que definen como opera una organización. Son externos al producto en sí. El desafío es poder extraerlas, catalogarlas, y documentarlas. Es una técnica muy útil que requiere de un trabajo prácticamente arqueológico

## Brainstorming

Consiste en reunir a un grupo de personas para resolver un problema y generar una gran cantidad de posibles soluciones, con la característica de que no hay censura. La discusión de la viabilidad queda para una etapa posterior.

## Análisis de Documentos

Tiene como propósito examinar documentación existente con el propósito identificar información relevante. Se pueden revisar planes de negocio, análisis de mercado, contratos, estudios, etc. Puede resultar tedioso, ya que toma mucho tiempo y a veces la documentación encontrada es obsoleta.

## Análisis de Causa Raíz

También conocido como diagrama **espina de pescado**, Tiene como propósito determinar las causas que originan un problema. Estas causas estarán ordenadas en categorías y en **subcausas** que estén relacionadas. Algunas categorías utilizadas son personas, procesos, métricas, etc. Es útil para guiar discusiones, utilizándolo en combinación con otras técnicas.

## Prototipado

El prototipado permite modelar las interfaces del software a desarrollar. Estos ayudan a ser que los requisitos sean más tangibles, facilitan el descubrimiento y la verificación. Es muy simple, se puede hacer con papel y lápiz.

Es importante no discutir aspectos relacionados con el diseño, sino los requisitos. Los prototipos pueden ser evolutivos o descartables

## Open Space (Technology)

Pensada para organizar reuniones con una gran cantidad de asistentes. Se convoca a una reunión en un mismo lugar a los interesados. Se define la agenda de forma colaborativa: aquellos interesados en un tema en particular lo comunican públicamente. Aquellos interesados en los temas planteados se reúnen y dialogan entre sí

## Documentación de los resultados

Se pueden tomar notas a mano, pero lo ideal es complementarlo con herramientas modernas como audio o video.

En el caso de las entrevistas, se estila a documentar lo conversado en una minuta de reunión. Es un documento electrónico que tiene como propósito registrar los temas conversados y registrar que se entendió correctamente. Normalmente, se distribuye luego de la reunión para que sea validada por los participantes. El contenido puede variar, pero en general incluye el objetivo, sus participantes, un resumen de los temas tratados, y los próximos pasos a dar.

## Otras Técnicas

Pueden utilizarse de forma combinada:

- Modelado de metas y objetivos.
- Mapa del ecosistema
- Análisis FODA (fortalezas, oportunidades, debilidades y amenazas)
- Los Cinco Porqués
- Diagrama de afinidad
- Diagrama de impacto *(Impact Maps)*
- Mapas de historias de usuario *(User Story Maps)*

## Recomendaciones

- Debemos tener mucho tacto en aspectos políticos y organizacionales.
- Identificar e involucrar a los interesados (incluso los negativos).
- Registrar las fuentes de los requisitos. Es crucial entender el origen de cada requisito.
- Registrar, cuando corresponda, la fundamentación de los requisitos.
- En términos generales, debemos guiarnos por las inquietudes del negocio. Centrarnos en los problemas a resolver.
- Debemos buscar restricciones en el dominio (leyes, regulaciones, normas, estándares, etc.).
- Es importante considerar múltiples puntos de vista, y llegar a un consenso a través del diálogo
- Prototipar requisitos poco claros o riesgosos (o con puntos de vista divergentes), para facilitar el diálogo y la validación.
- No debemos perder de vista el interés de quienes deberán operar y mantener la solución una vez desarrollada. Esta es una fuente para múltiples requisitos, en su mayoría no funcionales.
- Si tenemos experiencia en el dominio, es válido reutilizar requisitos de otras soluciones similares que ya hemos diseñado.
- Es muy importante entender el dominio del problema y el vocabulario de negocio.
