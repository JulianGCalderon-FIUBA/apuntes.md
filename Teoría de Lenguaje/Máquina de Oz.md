Para definir la semántica del lenguaje, debemos definir por cada *statement*, como se ejecutará.

## Skip

La instrucción `skip` se utiliza para no hacer nada dentro de un bloque.

![[Máquina de Oz 1694377235.png|500]]

En nuestro stack tendremos la instrucción `skip`, y el resto del stack. Luego de la ejecución, tendremos el resto del stack, y nuestro estado no cambió.

## Composición Secuencial

Cuando en el tope de la pila tenemos dos declaraciones para el mismo entorno, entonces se apila cada declaración por separado, con el mismo entorno.

![[Máquina de Oz 1694377293.png|500]]

## Declaración de Variable

Cuando en el tope tenemos el siguiente *semantic statement* `(local <x> in <s> end, E)`, entonces:

1. Se crea la variable `x` en el *store*.
2. Se crea un ambiente `E' = E + {<x> -> x}`. Es decir, al ambiente anterior pero con el identificador `<x>` asignado a la variable recién creada
3. Se apila `(<s>, E')` al stack
4. Se continúa con la proxima ejecución

![[Máquina de Oz 1694377588.png|500]]
