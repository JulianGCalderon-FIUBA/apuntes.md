Las bases de datos se gestionan a partir de un [[Gestor de Base de Datos]] de base de datos. Debido a esto, podemos separar la base de datos en sus *datos*, y su *gestor*. Los datos pueden no ser organizados por un gestor (aunque frecuentemente lo son)

> [!definition] Base de Datos
> Una base de datos es un conjunto de datos interrelacionados. Un dato es un hecho que puede ser representado y almacenado de alguna forma, y que tiene un sentido implícito.

Por debajo, una base de datos utiliza un [[Modelo de Datos]] para organizar la información, accederla y modificarla.

## Abstracción de Datos

Los desarrolladores esconden la complejidad de los usuarios a través de distintos niveles de abstracción:

- **Nivel Físico:** Es el nivel más bajo de abstracción. Describe *cómo* los datos se almacenan, describe estructuras de bajo nivel.
- **Nivel Lógico:** Describe *qué* información se almacena en la base de datos, y que relaciones existen en ella. No nos interesa como se almacena la información, a esto se le llama **independencia de la información física**.
- **Nivel de Vista:** El nivel más alto de abstracción, provee vistas específicas para cada usuario, ya que no todos los usuarios necesitan conocer toda la información de la base de datos.

## Instancias y Esquemas

El conjunto de información almacenada en una base de datos en un particular momento se conoce como una **instancia** de la base de datos. El diseño general de la misma se conoce como el **esquema** de la base de datos.

Las bases de datos tienen distintos esquemas, separados según el nivel de abstracción:

- El esquema **físico** describe el diseño de la base de datos a un nivel físico
- El esquema **lógico** describe el diseño de la base de datos a un nivel lógico.
- En ocasiones, una base de datos tiene múltiples esquemas a nivel de **vista**, llamados **subesquemas**.
