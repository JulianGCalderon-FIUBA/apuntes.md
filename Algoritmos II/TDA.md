# Tipo de Dato

Un tipo de dato define dos cosas importantes:

1. El conjunto de todos los valores posibles que una variable de ese tipo puede tomar
2. Las operaciones que las variables de ese tipo de dato pueden utilizar

Los lenguajes de programación tienen tipos de datos ***primitivos*** los cuales son predefinidos por el lenguaje de programación.

![[TDA 1.png|Untitled]]

# Abstracción

Proviene del latín *abstracto*, y significa: **separar aisladamente en la mente las características de un objeto o un hecho, dejando de prestar atención al mundo sensible para enfocarse solo en el pensamiento.**

Separamos lo que nos **importa**, y nos olvidamos de lo **innecesario**

![[TDA 2.png|Demostración de Picasso, del concepto de abstracción.]]

Demostración de Picasso, del concepto de abstracción.

# Tipo de Dato Abstracto

Un tipo de dato abstracto (TDA), es una clase de objetos abstractos, los cuales están caracterizados por las operaciones que definimos sobre esos objetos. Cuando un programador utiliza un **TDA**, esta únicamente interesado en en el comportamiento del objeto (¿Que?), y no de como se implementa. La vision de aquel que utiliza un **TDA** es exclusivamente de **Caja Negra**.

## El Qué y el Cómo

Las visiones de caja negra y caja blanca hacen una gran diferencia:

- El **Qué:** Este se refiere a la funcionalidad del TDA, relacionado a ¿Qué hace esto? **CAJA NEGRA**
- El **Cómo:** Este se refiere a como se implemente el TDA, relacionado a ¿Cómo hace esto? **CAJA BLANCA**

En el estudio e implementación de los TDAs es fundamental poder separar correctamente el **qué** y el **cómo**.

**Un Qué y Mil Cómos:**

Este concepto hace referencia a que, para cada problema a resolver, hay infinitas maneras de hacerlo.

## El Contrato

El contrato es el medio de comunicación entre el cliente y el programador, aca se define exactamente lo que tiene que realizar el TDA.  Una vez definido el contrato, es momento de diseñar e implementar.

## Ventajas

La utilización de TDA tiene muchas ventajas a la hora de realizar programas de gran tamaño:

- **Manejan la Abstracción:** Esto permite simplificar la realidad mediante la simplificación, despojando la complejidad que no es importante para el problema.
- **Encapsulamiento:** La información que no debe usar el usuario están ocultas, el solo tiene acceso a las funciones que el mismo entiende y necesita.
- **Localización del Cambio:** Cuando existe un error en el programa, es mas fácil arreglarlo si el código se encuentra modularizado, ya que podemos probar cada parte del programa por separado.

# Proceso de Desarrollo de Software

**El software no se fabrica, el software se desarrolla**. El desarrollo de software no es una única tarea, sino que incluye a un conjunto de etapas:

- **Análisis:** En esta etapa, debemos comprender el problema. Determinar aquellas cosas que se requiere para la resolución del mismo. ¿Que hay que hacer?
- **Diseño:** Consiste en crear una solución, teniendo en cuenta los multiples aspectos del software y del hardware. ¿Como hay que hacer?
- **Implementación:** Es la etapa mas conocida, en la que se desarrolla software en si
- **Pruebas:** Para verificar que el software que desarrollamos funciona correctamente, entonces debemos probarlo.
- **Instalación:** Esta etapa se basa en hacer que el software esté andando
- **Mantenimiento:** El software es un producto susceptible al cambio, a mejoras, a la reparación. Esta etapa se ocupa de esto.