---
title: Base de Datos
---

Las bases de datos se gestionan a partir de un [[Gestor de Base de Datos]] de base de datos. Debido a esto, podemos separar la base de datos en sus *datos*, y su *gestor*. Los datos pueden no ser organizados por un gestor (aunque frecuentemente lo son)

> [!definition] Base de Datos
> Una base de datos es un conjunto de datos interrelacionados. Un dato es un hecho que puede ser representado y almacenado de alguna forma, y que tiene un sentido implícito.

Por debajo, una base de datos utiliza un [[Modelo de Datos]] para organizar la información, accederla y modificarla.

## Predicados

Los datos no se almacenan como oraciones, sino con relaciones. Separamos los datos en **sujetos** relacionados y agregamos información sobre dicha relación.

Una tabla, luego, es una representación de hechos. Cada fila de la tabla nos dice algo.

La **normalización** de una tabla es tratar de reducir la cantidad de columnas que tiene. Luego debemos ampliar esta información al recuperarla.

Las bases de datos tradicionales almacenan datos de texto o numéricos, que pueden enunciarse a través de proposiciones. Un conjunto de proposiciones con la misma estructura puede tipificarse a través de un predicado.

> [!example]
> Dada la proposición: *"Rogerer Federer ganó el Abierto de Australia en 2018"*. Podemos abstraer un predicado: *"[jugador] ganó el [torneo] en [año]"*.

El predicado puede ser pensado como una función que recibe las variables del mismo, y nos devuelve un resultado. El resultado será verdadero o falso y nos va a indicar si dicha fila se encuentra en la tabla.

Las bases de datos modernas aprovechan estas repeticiones en la estructura de datos para poder almacenar información de forma eficiente.

## Abstracción de Datos

Los desarrolladores esconden la complejidad de los usuarios a través de distintos niveles de abstracción:

- **Nivel Físico:** Es el nivel más bajo de abstracción. Describe *cómo* los datos se almacenan, describe estructuras de bajo nivel.
- **Nivel Lógico:** Describe *qué* información se almacena en la base de datos, y que relaciones existen en ella. No nos interesa como se almacena la información, a esto se le llama **independencia de la información física**.
- **Nivel de Vista:** El nivel más alto de abstracción, provee vistas específicas para cada usuario, ya que no todos los usuarios necesitan conocer toda la información de la base de datos.

## Instancias y Esquemas

El conjunto de información almacenada en una base de datos en un particular momento se conoce como una **instancia** de la base de datos. El diseño general de la misma se conoce como el **esquema** de la base de datos.

Las bases de datos tienen distintos esquemas, separados según el nivel de abstracción:

- El esquema **físico** describe el diseño de la base de datos a un nivel fisio
- El esquema **lógico** describe el diseño de la base de datos a un nivel lógico.
- En ocasiones, una base de datos tiene múltiples esquemas a nivel de **vista**, llamados **subesquemas**.

## Diseño de Base de Datos

Un modelo de datos de alto nivel le provee al diseñador un *framework* conceptual bajo el cual especificar sus requerimientos de datos. La fase inicial del diseño es la de caracterizar completamente los requerimientos de datos de nuestros usuarios. Se debe interactuar extensamente con los expertos del dominio.

Luego, debemos seleccionar un modelo de datos que satisfaga nuestros requerimientos, y traducir los requerimientos en un esquema conceptual de la base de datos.

La parte final del diseño consiste en mover de un esquema abstracto a la implementación de la base de datos. Consiste en dos fases:

1. En la fase del diseño **lógico**, el diseñador traduce el esquema conceptual en un modelo de datos que utilizara el sistema
2. En la fase del diseño **físico**, se especifican características físicas de la base de datos, como la organización de archivos y la estructura interna del almacenamiento.
