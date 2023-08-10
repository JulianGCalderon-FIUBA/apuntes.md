> Conjeturo que no hay un buen algoritmo para el problema del viajante ~ Jack Edmonds, 1967

¿Que quiere decir un buen algoritmo? Un algoritmo es bueno si puede resolver un problema en una cantidad de tiempo que consideramos aceptable, luego, ¿Que cantidad de tiempo es aceptable? Necesitaremos entonces una clasificación para los algoritmos.

## Algoritmo Polinomial

Un algoritmo se dice polinomial si su orden de crecimiento está acotado por un polinomio, sin importar el grado del polinomio

## Problema Polinomial

Un problema se dice polinomial, o "fácil", si se conoce un algoritmo polinomial para determinar una solución óptima. Algunos ejemplos de problemas polinomiales son: ordenamiento de un vector, búsqueda de un elemento en un vector, calculo de inversa de matriz.

## Problema Indecidible

Un problema indecidible es aquel que no tiene algoritmos que lo resuelvan. Un ejemplo de estos es el problema de la parada: Dado un programa y un conjunto de datos iniciales, determinar si el programa finalizará en algún momento, o quedará atrapado en un bucle infinito.

## Complejidad Algorítmica

La complejidad se define según la relación entre la cantidad de instrucciones computadas y el tamaño de la instancia. Usualmente, se utiliza la notación ***big-O*** para medirla.

## Clases de Complejidad

Antes de mencionar las clases de complejidad, debemos hablar de la maquina determinística de ***Turing***. Esta se definió como una cinta, de tamaño ilimitado, que podremos pensar como la memoria de la maquina. La maquina tendrá un solo procesador y podrá recorrer la cinta, modificar los valores, y realizar operaciones con ella.

Una maquina no determinística es aquella que contiene una cantidad infinitas de cintas infinitas, luego cualquier problema de ramificación se puede resolver como si existiese una sola rama.

Un problema de decisión es aquel cuya respuesta es de si o no. Los problemas de decisión se pueden pensar como problemas de decisión. ¿La solución óptima, tiene un valor menor a $x$?

### Clase P

La clase de problemas de decisión $P$ constituyen aquellos problemas que tienen un algoritmo para resolverlo en tiempo polinomial. Lógicamente, la verificación de una solución también estará en tiempo polinomial.

### Clase NP

La clase de problemas de decisión $NP$ constituyen aquellos problemas que pueden ser resueltos en tiempo polinomial por una maquina de ***Turing*** no determinística. Esto es, no se pueden resolver en tiempo polinomial, pero si se pueden verificar en tiempo polinomial.

El problema del viajante, se puede reducir a $n!$ posibles soluciones, luego con $n!$ verificaciones encontraremos la solución optima. Este es un problema $NP$.

### Clase NP Completo

***Reducciones:*** Si un problema $A$ puede convertirse en tiempo polinomial en un problema $B$, se dice que $B$ "no es mas fácil" que $A$.

Los problemas $NP{-}\text{Completos}$ son aquellos problemas $NP$ tales que cualquier problema $NP$ puede reducirse en tiempo polinómico a dicho problema.

Esto quiere decir que si existe una solución polinómica para un problema $NP{-}\text{Completo}$, entonces todos los problemas $NP$ pueden ser resueltos en tiempo polinomial

### Clase NP Dificil

Los problemas $NP{-}\text{Dificiles}$ son aquellos problemas casi tan difíciles como los problemas $NP$. Son aquellos problemas tales que todos los problemas $NP$ pueden ser reducidos de forma polinómica a dicho problema. Estos problemas no son necesariamente $NP$.

Al igual que con los $NP{-}\text{Completos}$, si existe una solución polinómica para un problema $NP{-}\text{Dificil}$, entonces todos los problemas $NP$ pueden ser resueltos en tiempo polinomial

Los $NP{-}\text{Completos}$ son la intersección entre los $NP$ y los $NP{-}\text{Dificiles}$.

## P vs NP

El problema del milenio $P$ vs. $NP$. es aquel que busca definir si todo algoritmo $NP$ es también, un algoritmo $P$. Es decir, si todo algoritmo que es verificable en tiempo polinomial, también es resoluble en tiempo polinomial.

![[Complejidad de Problemas 1.png]]

En la imagen, vemos un diagrama de Euler para las clases de dificultad, según el resultado del problema
