---
title: Bugs de Concurrencia
---

Hay dos tipos de ***bugs*** principales relacionados con la concurrencia:

## Non-Deadlock Bugs

Engloban la mayoría de bugs relacionados con la concurrencia, y son los más fáciles de arreglar. La mayoría de estos ***bugs*** entran en alguna de las siguientes dos categorías:

Los primeros son conocidos como ***atomicity violation bugs***. Ocurren cuando se viola la atomicidad de una operación, introduciendo condiciones de carrera a nuestro programa. Para solucionar estos bugs, es necesario utilizar ***locks***. Se producen cuando dos porciones del código pueden acceder a un mismo recurso al mismo tiempo.

La definición más formal, de acuerdo con '*Tu et al'* es: *"The desired serializability among multiple memory accesses is violated"*

También existe otro tipo de bugs muy comunes llamados ***order violation bugs***. Ocurren cuando algunas operaciones dependen del comportamiento de otros ***threads***, pero no se pueden asegurar el orden de la ejecución. Para solucionar estos bugs, es necesario utilizar ***condition variables***. Estas variables permiten asegurarnos de que algunas partes del código se ejecutan después de otras.

La dirección más formal de un ***order violation*** es: "The desired order between two (groups of) memory accesses is flipped".

## Deadlock Bugs

Un clásico problema que surge cuando introducimos concurrencia compleja. Los ***deadlocks*** ocurren cuando dos ***threads*** se bloquean mutuamente, cada uno esperando un recurso que el otro tiene.

Una de las razones principales por las cuales surgen estos bugs, es debido a que cuando tenemos gran cantidad de código, pueden surgir dependencias complejas entre componentes.

Otra razón es debido a la naturaleza de la encapsulación. Los desarrolladores son enseñados a encapsular implementaciones para que el código sea fácil de modificar, pero esto no se mezcla bien con la concurrencia.

Tienen que ocurrir cuatro condiciones para que un ***dead lock*** ocurrea:

- ***Mutual Exclusion:*** Hilos reclaman control exclusivo de un recurso que requieren
- ***Hold-and-wait:*** Cuando un hilo quiere un recurso, espera de forma indefinida hasta que este recurso se libera
- **No preemption:** Los recursos no pueden ser removidos de forma forzada de los ***threads que los contienen.***
- ***Circular wait:*** Existe una cadena circular de ***threads***, donde cada uno tiene un ***recurso*** que otro contiene.

## Prevención

### Circular Wait

La forma mas practica de prevenir un ***deadlock*** consiste en escribir código de forma que nunca se genere un ***circular wait***. La forma más sencilla es proveer un ***total ordering*** en la adquisición de ***locks***. En sistemas más complejos es difícil obtener esto, por lo que muchas veces se recurre a ***partial ordering***.

Una forma de solucionarlo es adquirir los ***locks*** en un orden basado en la dirección de memoria de este ***lock***. Tanto orden parcial como orden total requieren de un cuidadoso diseño de las estrategias de ***lockeo***.

### Hold and Wait

Otra forma de prevenir esto es nunca tener esto es obtener todos los *lock al mismo tiempo, de forma atómica. Una forma de hacerlo es tener un lock* de prevención que permite acceder otros ***locks*** de forma atómica. Esta solución es problemática por varias razones. Necesitamos saber de antemano todos los ***locks*** que necesitaremos, además de ser más lento (reduce concurrencia ya que los ***locks*** se adquieren al principio y no cuando realmente se necesitan).

### No Preemption

Muchas thread libraries permiten interfaces flexibles para adquirir ***locks***. Con rutinas que no bloquean un proceso, sino que continúan la ejecución si no se pudo acceder al ***lock***.

Esta solución puede causar algo conocido como ***live lock***. Dos threads repiten constantemente la misma secuencia de código sin producir ningún avance. Para este problema también existen soluciones, como añadir un ***delay*** aleatorio entre ciclos.

Esta solución trae problemas de encapsulamiento, ya que un ***lock*** puede esta enterrado dentro de una rutina, y necesitaríamos saber de antemano esta información. Por otro lado, si fallamos en adquirir un ***lock***, debemos saber que ***locks*** fueron previamente accedidos por funciones anteriores, para poder liberarlos.

### Mutual Exclusion

Por último, podemos evitar la exclusión mutua totalmente. Para realizar esto, dependemos de poderosas instrucciones atómicas del hardware. Para poder tener estructuras concurrentes sin necesidad de ***locks***.

### Scheduling

En lugar de prevenir ***deadlocks***, podemos tratar de evitarlos. Para hacer esto, se necesita conocimiento global de los ***locks*** que cada ***thread*** puede adquirir. El planificador puede planificar los hilos de forma que se garantice que no haya ***deadlocks***.

### Detect and Recover

Por último, una última estrategia para prevenir ***deadlocks*** consiste en tomar cierta acción en caso de que se detecte un ***deadlock***. Muchas bases de datos emplean esta táctica para reiniciar el sistema en caso de que se detecte una falla.
