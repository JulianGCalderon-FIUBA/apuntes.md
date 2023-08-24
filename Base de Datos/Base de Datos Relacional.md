---
title: Base de Datos Relacional
---

## Definición

En una base de datos relacional, la información se organiza en **tablas**.

> [!example] Contraejemplo
> No todas las BDD son relacionales. MongoDB almacena información en documentos JSON

Las bases de datos se gestionan a partir de un [[Gestor de Base de Datos]] de base de datos. Debido a esto, podemos separar la base de datos en sus *datos*, y su *gestor*. Los datos pueden no ser organizados por un gestor (aunque frecuentemente lo son)

> [!definition] Base de Datos
> Una base de datos es un conjunto de datos interrelacionados. Un dato es un hecho que puede ser representado y almacenado de alguna forma, y que tiene un sentido implícito.

## Predicados

Los datos no se almacenan como oraciones, sino con relaciones. Separamos los datos en **sujetos** relacionados y agregamos información sobre dicha relación.

Una tabla, luego, es una representación de hechos. Cada fila de la tabla nos dice algo.

La **normalización** de una tabla es tratar de reducir la cantidad de columnas que tiene. Luego debemos ampliar esta información al recuperarla.

Las bases de datos tradicionales almacenan datos de texto o numéricos, que pueden enunciarse a través de proposiciones. Un conjunto de proposiciones con la misma estructura puede tipificarse a través de un predicado.

> [!example]
> Dada la proposición: *"Rogerer Federer ganó el Abierto de Australia en 2018"*. Podemos abstraer un predicado: *"[jugador] ganó el [torneo] en [año]"*. Luego, podemos generar una tabla en la base de datos con esas tres columnas.

El predicado puede ser pensado como una función que recibe las variables del mismo, y nos devuelve un resultado. El resultado será verdadero o falso y nos va a indicar si dicha fila se encuentra en la tabla.

## Abstracción de Datos

Los desarrolladores esconden la complejidad de los usuarios a través de distintos niveles de abstracción:

- **Nivel Físico:** Es el nivel más bajo de abstracción. Describe *cómo* los datos se almacenan, describe estructuras de bajo nivel.
- **Nivel Lógico:** Describe *qué* información se almacena en la base de datos, y que relaciones existen en ella. No nos interesa como se almacena la información, a esto se le llama **independencia de la información física**.
- **Nivel de Vista:** El nivel más alto de abstracción, provee vistas específicas para cada usuario, ya que no todos los usuarios necesitan conocer toda la información de la base de datos.

## Instancias y Esquemas

El conjunto de información almacenada en una base de datos en un particular momento se conoce como una **instancia** de la base de datos. El diseño general de la misma se conoce como el **esquema** de la base de datos.

Las bases de datos tienen distintos esquemas, separados según el nivel de abstracción:

- El esquema **fisico** describe el diseño de la base de datos a un nivel fisio
- El esquema **logico** describe el diseño de la base de datos a un nivel lógico.
- En ocasiones, una base de datos tiene multiples esquemas a nivel de **vista**, llamados **su**
