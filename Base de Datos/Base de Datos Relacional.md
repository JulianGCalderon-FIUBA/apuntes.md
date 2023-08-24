---
title: Base de Datos Relacional
---

## Definición

En una base de datos relacional, la información se organiza en **tablas**.

> [!example] Contraejemplo
> No todas las BDD son relacionales. MongoDB almacena información en documentos JSON

Las bases de datos se gestionan a partir de un **gestor** de base de datos. Debido a esto, podemos separar la base de datos en sus *datos*, y su *gestor*. Los datos pueden no ser organizados por un gestor (aunque frecuentemente lo son)

> [!definition] Base de Datos
> Una base de datos es un conjunto de datos interrelacionados. Un dato es un hecho que puede ser representado y almacenado de alguna forma, y que tiene un sentido implícito.

Los datos no se almacenan como oraciones, sino con relaciones. Separamos los datos en **sujetos** relacionados y agregamos información sobre dicha relación.

Una tabla, luego, es una representación de hechos. Cada fila de la tabla nos dice algo.

La **normalización** de una tabla es tratar de reducir la cantidad de columnas que tiene. Luego debemos ampliar esta información al recuperarla.

Las bases de datos tradicionales almacenan datos de texto o numéricos, que pueden enunciarse a través de proposiciones. Un conjunto de proposiciones con la misma estructura puede tipificarse a través de un predicado.

> [!example]
> Dada la proposición: *"Rogerer Federer ganó el Abierto de Australia en 2018"*. Podemos abstraer un predicado: *"[jugador] ganó el [torneo] en [año]"*. Luego, podemos generar una tabla en la base de datos con esas tres columnas.

El predicado puede ser pensado como una función que recibe las variables del mismo, y nos devuelve un resultado. El resultado será verdadero o falso y nos va a indicar si dicha fila se encuentra en la tabla.

## Gestor de Base de Datos

Permiten trabajar con una base de datos de forma cómoda y segura.

### Funciones Principales

Los gestores de bases de datos permiten operaciones atómicas, llamadas transacciones, que nos aseguran que las operaciones no pueden ser interrumpidas. Esto nos asegura que no tendremos problemas de corrupción en la base de datos. Ademas, nos permite acceder a la base de datos de forma concurrente, por muchos usuarios.

Ofrecen seguridad para prevenir accesos no autorizados, y herramientas para la recuperación ante fallas.

Tiene un lenguaje de consultas (SQL) que nos permite realizar todo tipo de consultas.

Asegura la integridad de datos a través de restricciones, como por ejemplo, errores de tipeo al nombrar categorías.

Tiene herramientas para acceder a la tabla de forma eficiente. No se requiere iterar toda la base de datos para hallar la fila que necesitamos. Se utiliza indexación.

### Usuarios

Existen distintos tipos de usuarios, cada uno con capacidades y roles distintos:

- El *admin* o administrador es el usuario que puede realizar cualquier acción.
- El diseñador de una base de datos se encarga de diseñar su arquitectura (tablas, columnas)
- Existen usuarios de solo lectura, o de acceso a ciertas tablas particulares.

### Historia

En los años 50, se reemplazaron los ficheros de información (físicos) por cintas magnéticas. Los datos frecuentemente se ingresaban con tarjetas perforadas. Estas cintas solo permitían acceso secuencial.

En los años 60 surgen los discos magnéticos, y con la posibilidad de acceso directo a los datos. Aquí surgen los primeros gestores de bases de datos:

- El IMS *(Information Management System)* de IBM utilizaba un modelo de datos jerárquico
- El IDS *(Integrated Data Store)* de General Electric utilizaba un modelo de datos en red.

En estos modelos, los datos estaban relacionados con modelos. Finalmente, en el año 72 se propuso el primer modelo relacional (teóricamente). No fue hasta los años 80 que surgieron las primeras implementaciones. Oracle fue el primero, y luego apareció PostgreSQL

En las bases de datos relacionales, los datos no se relacionan con punteros, sino con claves foráneas (no necesita iterar la información, sino indexarla). Con los punteros, el programador debía seguir los punteros (este trabajo luego fue asumido por los gestores).

> [!definition] Gestor de Base de Datos
> Es un conjunto de programas que gestiona y controla la creación, manipulación y acceso a la base de datos.

Esto permite abstraer el programa de los datos, permitiendo cambiar los datos sin romper los programas ya existentes.

## Arquitectura de 3 Capas: ANSI/SPARC

- La primera capa es la organización física de los datos
- La segunda capa es el modelo interno de los datos
- La tercera capa es el modelo conceptual de los datos
- El nivel externo contiene la vistas de la base de datos, una descripción de que ve cada usuario.
