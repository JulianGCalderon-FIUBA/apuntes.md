## El Rol de la Abstracción

Las descripciones científicas del mundo están basadas en abstracciones, son necesarias para entender el mundo. En la ciencia de la computación, los ingenieros informáticos trabajan con tres tipos de abstracciones principales:

- **Bibliotecas y Sistemas Operativos:** Usualmente conocidos como *Application Program Interfaces (API)*, definen recursos computacionales disponibles al programador.
- **Lenguajes de Programación:** Nos permite utilizar el poder computacional de la computadora, abstrayéndonos de las arquitecturas principales
- **Conjuntos de Instrucciones:** Nos permiten construir compiladores para distintas arquitecturas, abstrayéndonos de la implementación particular de cada una.

Dos de las herramientas más importantes para la abstracción del software son encapsulamiento y concurrencia.

- **Encapsulamiento** obtiene abstracción al dividir un módulo de software en su especificación pública y su implementación oculta. Al cambiar la implementación, no cambiamos la interfaz pública.
- **Concurrencia** es una abstracción diseñada para hacer posible razonar sobre el comportamiento dinámico de un programa.

## Ejecución Concurrente

La **ejecución del programa concurrente** resulta al ejecutar una secuencia de instrucciones atómicas que se obtiene de intercalar de forma arbitraria las instrucciones atómicas de los procesos que lo componen. A cada posible secuencia de ejecución se le suele llamar **computación**, o *escenarios*.

Esta ejecución está definida por **estados** y las transiciones entre estos estados. En cada punto de la ejecución, el programa debe estar en algún estado particular. Definido por el valor de las variables y el *program counter* de cada proceso. Un escenario, luego, es una secuencia de estados.

## Justificación de la Abstracción

Es conveniente pensar la ejecución de un programa concurrente como una entidad global que, a cada paso del camino, elige cuál hilo va a ejecutar su próxima instrucción. Esta elección es arbitraria.

En un sistema **multitasking**, con un solo procesador, una sola ejecución se ejecuta a la vez. El sistema operativo se encargará de intercalar los distintos procesos (o programas). Es un requerimiento que cualquier escenario posible sea aceptable.

En una computadora **multiprocesador**, se pueden ejecutar, de forma paralela, dos hilos de ejecución. Mientras no accedan a memoria compartida, no habrá ningún problema. En cuanto se acceda a memoria compartida, el hardware se encargará (para algunos tamaños de celdas de memoria) de que estos accesos sean exclusivos. En otros casos, se deben sincronizar dichos accesos.

En un sistema **distribuido** está compuesto por computadores sin recursos globales, que se comunican a través de canales. En estos sistemas no existe la abstracción de intercalado, debido a que es imposible coordinar dos sistemas geográficamente distribuidos.

Estos sistemas se consideran distintos a los sistemas distribuidos, debemos tener en cuenta la topología o la conexión del sistema. Una topología *fully connected* es extremadamente eficiente, pero extremadamente costosa. Una topología de anillo tiene costo mínimo, pero es altamente ineficiente.

## Intercalado Arbitrario

Vamos a asumir que luego de cualquier instrucción, la próxima instrucción puede venir de cualquier proceso. Esto nos permite analizar el sistema de forma correcto y asegurar que el programa concurrente sea correcto. No vamos a tener en cuenta el tiempo entre instrucciones, sino únicamente su secuencia.

Vamos a asumir que los escenarios son **débilmente justos**. Todo proceso que está continuamente habilitado, eventualmente aparecerá en el escenario.

Una segunda razón para esta abstracción es que nos permite construir sistemas robustos ante la modificación del hardware o el software. Si nuestro algoritmo depende del tiempo de ejecución, entonces eventualmente este tiempo de ejecución cambiara en cuanto mejore la tecnología.

La tercera razón es que es simplemente imposible (o muy difícil) de repetir la ejecución de un programa concurrente.

## Declaraciones Atómicas

Una instrucción atómica es aquella que su ejecución completa sin interrupciones es garantizada. La suposición de que todas las instrucciones son atómicas no es para nada realista, ya que las instrucciones del lenguaje de programación se descomponen en múltiples instrucciones en lenguaje de máquina.

## Instrucciones de Código de Máquina

Los registros son independientes para cada proceso, y, por lo tanto, no interfieren en la concurrencia. A su vez, cada proceso tiene su propio *stack*, por lo que esta memoria tampoco interfiere en la concurrencia.

Se dice que la ocurrencia de una variable $v$ es *crítica* si fue asignada por un proceso, y tiene ocurrencia en otro proceso. Un programa satisface la restricción *limited-critical-reference (LCR)* si cada declaración contiene a lo sumo una referencia crítica. El uso de variables locales temporales ayudará a satisfacer esta restricción.
