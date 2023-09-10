Para definir la semántica del lenguaje, debemos definir por cada *statement*, como se ejecutará.

## Skip

La instrucción `skip` se utiliza para no hacer nada dentro de un bloque.

![[Máquina de Oz 1694377235.png|500]]

En nuestro stack tendremos la instrucción `skip`, y el resto del stack. Luego de la ejecución, tendremos el resto del stack, y nuestro estado no cambió.

## Composición Secuencial

Cuando en el tope de la pila tenemos dos declaraciones para el mismo entorno, entonces se apila cada statement po

![[Máquina de Oz 1694377293.png|500]]
