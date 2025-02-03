El problema de los generales bizantinos es un experimento que se utiliza para ilustrar la dificultad de los algoritmos de consenso, en situaciones donde las entidades que participan pueden tener fines maliciosos.

- Hay $m$ **generales** bizantinos que están asediando una ciudad desde distintos frentes.
- El ataque solo es exitoso si se realiza en todos los frentes a la vez.
- Uno de los generales es el **comandante**, y es el que da la orden de atacar/retirarse. Esta orden se realiza enviando un mensajero a cada uno de los otros generales.
- Los generales pueden ser **traidores**, en cuyo caso pueden ofrecer información errónea.

Se debe encontrar una forma de que los generales se pongan de acuerdo, evitando perder la guerra.

## Requerimientos

Los requerimientos generales de [[Algoritmos de Consenso#Requerimientos|algoritmos de consenso]] también son aplicables aca:

- **Agreement**: Todos los procesos deben acordar lo mismo: atacar o retirarse.
- **Integrity**: Todos los procesos deben acordar lo que diga el comandante.
- **Termination**: El consenso deberá eventualmente terminar.
