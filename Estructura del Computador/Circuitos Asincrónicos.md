## Flip Flop - RS Asincrónico

En un circuito simple con capacidad de memoria, transforma pulsos temporales de $S, R$ en pulsos constantes $Q, \overline Q$.

![[Circuitos Asincrónicos 1693351681.png|300]] ![[Circuitos Asincrónicos 1693351681-1.png|300]]

### Diagrama de Tiempos

Para analizar el comportamiento de la función, debo realizar un diagrama de tiempos. Para eso, pienso las entradas como una función de tiempo (pulsos) y analizo el cambio en las variables de la función.

![[Circuitos Asincrónicos 1693351681-2.png|475]]

### Tabla de Estados

Otra forma de analizar un circuito con memoria es a partir de un diagrama de estados, es como una tabla de verdad, pero depende de las variables de salida.

![[Circuitos Asincrónicos 1693351681-3.png|197]] ![[Circuitos Asincrónicos 1693351681-4.png]]

### Ecuación Característica

Es una expresión algebraica que representa la variable de salida en función de los datos de entrada (incluyendo la memoria)

$$
Q^{n+1} = S + \overline R . Q^n
$$

### Diagrama de Estados

Es un diagrama que representa las transiciones entre los estados de salida de un circuito

![[Circuitos Asincrónicos 1693351681-5.png|475]]

### Flip Flop D

$Q$ vale lo mismo que la entrada $D$. A primera vista no es útil, hace falta una modificación para que la memoria tenga algún efecto en el circuito.

![[Circuitos Asincrónicos 1693351681-6.png|325]] ![[Circuitos Asincrónicos 1693351681-7.png]]

### Flip Flop JK

Similar al circuito $RS$, pero resuelve la problemática de $R{=}S{=}1$.

![[Circuitos Asincrónicos 1693351681-8.png|275]] ![[Circuitos Asincrónicos 1693351681-9.png|207]]

Si $J{=}K{=}1$, Entonces $Q$ varía con una frecuencia determinada por las compuertas y el retardo de la retroalimentación. Es difícil determinar el valor de la frecuencia

### Flip Flop T

La letra $T$ viene del término del inglés *"Toggle".* Es una simplificación del Flip Flop $JK$, Si $T{=}1$, entonces es lo mismo que $J{=}K{=}1$.

![[Circuitos Asincrónicos 1693351681-10.png|183]] ![[Circuitos Asincrónicos 1693351681-11.png|196]]
