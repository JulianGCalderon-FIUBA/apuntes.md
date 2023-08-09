## Flip Flop - RS Asincrónico

RS - Asincrónico ![[Circuitos Asincronicos 1.png]]

RS - Asincrónico ![[Circuitos Asincronicos 2.png]]

En un circuito simple con capacidad de memoria, transforma pulsos temporales de $S, R$ en pulsos constantes $Q, \overline Q$.

### Diagrama de Tiempos

Para analizar el comportamiento de la función, debo realizar un diagrama de tiempos. Para eso, pienso las entradas como una función de tiempo (pulsos) y analizo el cambio en las variables de la función.

![[Circuitos Asincronicos 3.png]]

### Tabla de Estados

Otra forma de analizar un circuito con memoria es a partir de un diagrama de estados, es como una tabla de verdad pero depende de las variables de salida.

![[Circuitos Asincronicos 4.png]]

![[Circuitos Asincronicos 5.png]]

### Ecuación Característica

Es una expresión algebraica que representa la variable de salida en función de los datos de entrada (incluyendo la memoria)

$$
Q^{n+1} = S + \overline R . Q^n
$$

### Diagrama de Estados

Es un diagrama que representa las transiciones entre los estados de salida de un circuito

![[Circuitos Asincronicos 6.png]]

### Flip Flop D

$Q$ vale lo mismo que la entrada $D$. A primera vista no es útil, hace falta una modificación para que la memoria tenga algun efecto en el circuito.

![[Circuitos Asincronicos 7.png]]

![[Circuitos Asincronicos 8.png]]

### Flip Flop JK

Similar al circuito $RS$, pero resuelve la problemática de $R{=}S{=}1$.

![[Circuitos Asincronicos 9.png]]

![[Circuitos Asincronicos 10.png]]

Si $J{=}K{=}1$, Entonces $Q$ varia con una frecuencia determinada por las compuertas y el retardo de la retroalimentación. Es difícil determinar el valor de la frecuencia

### Flip Flop T

La letra $T$ viene del termino del ingles "Toggle". Es una simplificación del flip flop $JK$, Si $T{=}1$, entonces es lo mismo que $J{=}K{=}1$.

![[Circuitos Asincronicos 11.png]]

![[Circuitos Asincronicos 12.png]]
