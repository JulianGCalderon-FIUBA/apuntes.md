---
title: Introducción al Diseño de Software
---

El diseño del software es el proceso mediante el cual definimos la arquitectura, los componentes, las interfaces y otras características de un sistema o componente. El diseño del software, también es el resultado del proceso anterior.

- Es una actividad creativa. No existe una receta, aunque hay lineamientos, estándares, y patrones.
- El diseño es emergente, va tomando forma iterativamente. De igual forma, hay que tomar grandes decisiones antes de comenzar a programar
- No es sinónimo de modelar, pero se construyen modelos.
- El nivel de formalidad del diseño dependerá de múltiples factores, como la complejidad técnica, riesgo, costos, tamaño, experiencia del equipo, etc.

## Modelado

Existen dos caminos posibles:

- **Modelado ágil:** Los modelos son informales y no se mantienen.
- **Ing. de Software Basada en Modelos:** Tiene que ver con desarrollar modelos y evolucionarlos hasta transformarlos en la solución. Esta técnica es relativamente popular en determinados segmentos (no todos).

## De Requisitos al Diseño a la Construcción

Se comienza diseñar durante la etapa de requerimientos, solapando ambas actividades. La construcción también comienza durante la etapa de requerimientos y diseño. Existe una idea y vuelta entre todas las disciplinas.

![[Introduccion al Diseno de Software 1.png|550]]

A partir de los requisitos, debemos definir:

- **Arquitectura:** Organización general y estructura de la solución
- **Componentes:** Algoritmos a utilizar, estructuras de datos internas, clases, métodos, criterio
- **Interfaces:** Interacción con el usuario, diálogo.
- **Datos:** Archivo, base de datos
- **Colaboración:** Componentes que interactúan para implementar el comportamiento identificado.

La transición entre los requisitos y el diseño son difíciles.

## Principios Clásicos del Diseño

A lo largo de la carrera, vimos múltiples principios de clásicos del diseño:

![[Introduccion al Diseno de Software 2.png|500]]

Principios clásicos del desarrollo

Desarrollar grandes productos no es lo mismo que los pequeños proyectos. Los principios son importantes.

![[Introduccion al Diseno de Software 3.png|500]]

Principios importantes para el diseño de objetos

![[Introduccion al Diseno de Software 4.png]]

Principios SOLID

## Arquitectura

Refiere a la estructura de alto nivel de un sistema. Las grandes decisiones respecto a un sistema, aquellas decisiones difíciles de cambiar.

### 4 Vistas + 1

Es un modelo que permite visualizar la importancia de la arquitectura. Se plantea que un producto de software se puede ver con diversas vistas, cada una mostrando aspectos particulares:

- Vista Lógica: Aspectos lógicos, la estructura lógica del sistema en subsistemas, submódulos, etc. Refiere a las clases.
- Vista de Implementación: Como empaquetamos los elementos de la vista lógica en elementos ejecutables
- Vista de Distribución: Similar a la vista de implementación.
- Vista de Procesos: Distintos procesos a nivel del sistema operativo.
- Vista de Escenarios: Junta las cuatro vistas anteriores. El mecanismo para visualizarla es un diagrama de secuencia o de colaboración.

### Asignación De Requisitos

Relación entre los requisitos y la arquitectura

- Los requisitos deben asignarse a los elementos de la arquitectura.
- Hay algunos requisitos que tienen mucho impacto en la arquitectura (requisitos arquitectónicamente significativos)
- A su vez, la arquitectura impacta en los requisitos.

### Influencia de Arquitectura

La arquitectura tiene mucha influencia en:

- Los requisitos
- La organización del equipo de desarrollo
- El proceso de desarrollo
- La flexibilidad para adaptarse a los cambios
- Los objetivos de la organización

### Estilos Arquitectónicos

![[Introduccion al Diseno de Software 5.png|500]]

Busca aislar los cambios en la interfaz, de los cambios de la lógica, de los cambios en los datos. Es un patrón del diseño orientado a objetos

![[Introduccion al Diseno de Software 6.png|500]]

La capa de presentación manejo la lógica del diálogo con el usuario. La capa de negocio maneja la lógica de la aplicación. La capa de persistencia permite el acceso a los datos, que están en la capa de base de datos.

![[Introduccion al Diseno de Software 7.png|500]]

Se publica un evento en una cola de eventos. Del otro lado, tendremos componentes que escuchan de la cola y esperan que aparezcan los eventos, para realizar acciones determinadas.

![[Introduccion al Diseno de Software 8.png|500]]

A través de una **API**, se accede a lógica que está en una capa más abajo.

### Arquitectura Corporativa

Son principios y prácticas para guiar a las organizaciones a través de los cambios en procesos, sistemas, información y tecnología necesarios para implementar su estrategia

Es un método estándar para desarrollar arquitecturas corporativas. Se consideran cuatro áreas de especialización:

- Arquitectura de Negocio: Estrategia, organización, procesos clave
- Arquitectura Aplicativa: Sistemas, interacciones, relaciones con los procesos de negocio
- Arquitectura de Datos: Diseño lógico y físico de datos
- Arquitectura Técnica: Infraestructura de software, hardware y redes.

Un lenguaje abierto para modelar arquitecturas corporativas, el modelado se realiza en capas:

- Negocio (procesos)
- Aplicación (software)
- Tecnología (hardware y comunicaciones)

## Interfaces del Usuario

Es un elemento clave del usuario, es un tema crítico. Si una aplicación es muy buena, pero con mala interfaz, el producto será malo.

## Diseño de Datos

Debemos definir como persistirán los datos. Existen tres niveles de modelado:

- **Conceptual:** Representación de los datos del dominio del problema. Usualmente, es el resultado del análisis. Puede ser un *modelo de dominio*
- **Lógico:** Diseño lógico de la base de datos, tablas, columnas, claves primarias, claves foráneas (referencian claves primarias)
- **Físico:** Implementación de la base de datos, índices, espacios de almacenamiento, seguridad.

## Estrategias de Diseño

Un posible enfoque, podría ser:

1. Realizar un diseño arquitectónico inicial, identificando subsistemas, bases de datos, clases significativas.
2. Realizar el diseño de la base de datos.
3. Realizar el diseño de las colaboraciones necesarias para implementar cada escenario, identificando los elementos participantes.
4. Realizar el diseño de cada uno de los elementos (atributos, métodos, interfaces).
5. Refinar la arquitectura.
6. Trasladar el diseño al código, probar, refinar nuevamente el diseño.
