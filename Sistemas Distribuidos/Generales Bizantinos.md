El problema de los generales bizantinos es un experimento que se utiliza para ilustrar la dificultad de los algoritmos de consenso, en situaciones donde las entidades que participan pueden tener fines maliciosos, o están funcionando de forma defectuosa.

- Hay $m$ **generales** bizantinos que están asediando una ciudad desde distintos frentes.
- El ataque solo es exitoso si se realiza en la mayoría de los frentes a la vez.
- Uno de los generales es además el **comandante**, y es el que da la orden de atacar/retirarse. Esta orden se realiza enviando un mensajero a cada uno de los otros generales.
- Los generales/comandante pueden ser **traidores**, en cuyo caso pueden ofrecer información errónea.

Se debe encontrar una forma de que los generales se pongan de acuerdo, evitando perder la guerra.

Una falla **bizantina** es un tipo de falla que se produce en un sistema informático cuando los participantes de una red distribuida no están coordinados.

## Requerimientos

Los requerimientos generales de [[Algoritmos de Consenso#Requerimientos|algoritmos de consenso]] también son aplicables acá:

- **Agreement**: Todos los procesos deben acordar lo mismo: atacar o retirarse.
- **Integrity**: Todos los procesos deben acordar lo que diga el comandante.
- **Termination**: El consenso deberá eventualmente terminar.

Se denota como $f$ como la cantidad de nodos que pueden tener una falla bizantina, y $N$ con la cantidad de nodos del sistema.

## Imposibilidad de `N <= 3f`

En el siguiente caso, vemos que el nodo $2$ recibe valores distintos de $1$ y $2$, pero no puede determinar donde se está produciendo la falla.

![[Generales Bizantinos 1738624253.png]]

## Solución con `N >= 3f + 1`

Vemos que los nodos siempre reciben

![[Generales Bizantinos 1738624468.png]]
