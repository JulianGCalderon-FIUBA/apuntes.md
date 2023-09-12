Para definir la semántica del lenguaje, debemos definir por cada *statement*, como se ejecutará. Utilizaremos una [[Máquina Abstracta]]

## Skip

La instrucción `skip` se utiliza para no hacer nada dentro de un bloque.

![[Semántica de Oz 1694377235.png|500]]

En nuestro stack tendremos la instrucción `skip`, y el resto del stack. Luego de la ejecución, tendremos el resto del stack, y nuestro estado no cambió.

## Composición Secuencial

Cuando en el tope de la pila tenemos dos declaraciones para el mismo entorno, entonces se apila cada declaración por separado, con el mismo entorno.

![[Semántica de Oz 1694377293.png|500]]

## Declaración de Variable

Cuando en el tope tenemos el siguiente *semantic statement* `(local <x> in <s> end, E)`, entonces:

1. Se crea la variable `x` en el *store*.
2. Se crea un ambiente `E' = E + {<x> -> x}`. Es decir, al ambiente anterior, pero con el identificador `<x>` asignado a la variable recién creada
3. Se apila `(<s>, E')` al stack
4. Se continúa con la próxima ejecución

![[Semántica de Oz 1694377588.png|500]]

## Igualdad: Variable - Variable

Se realiza un *bind* de ambas variables en el *store*.

![[Semántica de Oz 1694377692.png|500]]

## Igualdad: Variable - Valor

Se crea el valor y se liga a la variable `<x>` en el *store*.

![[Semántica de Oz 1694377710.png|500]]

## Igualdad: Variable - Procedimiento

Tenemos que actualizar el entorno con los nuevos identificadores (los definidos en el procedimiento).

Debemos analizar los identificadores libres del nuevo entorno:

1. Parámetros formales
2. Referencias externas

Definimos un nuevo entorno, que será $CE = E|_{\{<z1>,\cdots,<zk>\}}$. Siendo estas referencias externas del entorno interior.

## Ejecución de Procedimiento

La llamada a un procedimiento es una declaración suspendible. Esto puede ocurrir cuando no está definido el procedimiento aún.

Si el procedimiento está definido, debe tener la misma aridad (en otro caso, lanza error).

![[Semántica de Oz 1694536020.png|500]]

Se apila al stack la declaración del procedimiento, con un nuevo entorno que será definido por el entorno del procedimiento, ligando las variables a sus respetivos valores: `Ep = CE + {<z1> -> E(<y1>),..., <zn> -> E(<yn>)}`


