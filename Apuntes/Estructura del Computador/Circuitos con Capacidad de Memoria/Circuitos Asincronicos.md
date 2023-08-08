# Flip Flop - RS Asincrónico

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 1.png|RS - Asincrónico]]

RS - Asincrónico

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 2.png|RS - Asincrónico]]

RS - Asincrónico

En un circuito simple con capacidad de memoria, transforma pulsos temporales de $S, R$ en pulsos constantes $Q, \overline Q$. 

## Diagrama de Tiempos

Para analizar el comportamiento de la función, debo realizar un diagrama de tiempos. Para eso, pienso las entradas como una función de tiempo (pulsos) y analizo el cambio en las variables de la función. 

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 3.png|Untitled]]

## Tabla de Estados

Otra forma de analizar un circuito con memoria es a partir de un diagrama de estados, es como una tabla de verdad pero depende de las variables de salida.

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 4.png|Untitled]]

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 5.png|Untitled]]

## Ecuación Característica

Es una expresión algebraica que representa la variable de salida en función de los datos de entrada (incluyendo la memoria)

$$
Q^{n+1} = S + \overline R . Q^n
$$

## Diagrama de Estados

Es un diagrama que representa  las transiciones entre los estados de salida de un circuito

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 6.png|Untitled]]

## Flip Flop D

$Q$ vale lo mismo que la entrada $D$. A primera vista no es útil, hace falta una modificación para que la memoria tenga algun efecto en el circuito.

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 7.png|Untitled]]

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 8.png|Untitled]]

## Flip Flop JK

Similar al circuito $RS$, pero resuelve la problemática de $R{=}S{=}1$.

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 9.png|Untitled]]

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 10.png|Untitled]]

Si $J{=}K{=}1$, Entonces $Q$ varia con una frecuencia determinada por las compuertas y el retardo de la retroalimentación. Es difícil determinar el valor de la frecuencia

## Flip Flop T

La letra $T$ viene del termino del ingles “Toggle”. Es una simplificación del flip flop $JK$, Si $T{=}1$, entonces es lo mismo que $J{=}K{=}1$.

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 11.png|Untitled]]

![[Apuntes/Estructura del Computador/Circuitos con Capacidad de Memoria/Attachments/Circuitos Asincronicos 12.png|Untitled]]