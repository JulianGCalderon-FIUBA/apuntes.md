Para definir la semántica del lenguaje, debemos definir por cada *statement* del lenguaje *kernel*, como se ejecutará. Utilizaremos una [[Máquina Abstracta]]

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

En el tope del stack, tenemos: `(<x> = proc {$ <y1>... <yn>} <sp> end, E)`.

Tenemos que actualizar el entorno con los nuevos identificadores (los definidos en el procedimiento).

Debemos analizar los identificadores libres del nuevo entorno:

- Parámetros formales: `<z1>,..., <zk>`
- Referencias externas: `<y1,..., <yn>`

Definimos un nuevo entorno de contexto, que contendrá las referencias externas del procedimiento: `CE = E|{<z1>,..., <zk>}`

Luego, se guarda en el *store* el par de procedimiento y contexto: `<x> = (proc {$ <y1>,..., <yn>} <sp> end, CE)`

> [!note] Scoping Dinámico
> Como el *Scoping* es dinámico, el contexto se captura en momento de compilación.

## Ejecución de Procedimiento

En el tope del stack, tenemos: `({<x> <y1>... <yn>}, E)`.

La llamada a un procedimiento es una declaración suspendible. Esto puede ocurrir cuando no está definido `E(<x>)` aún. Si está definido, debe tener la misma aridad (en otro caso, lanza error).

Se apila al stack la declaración del procedimiento: `(<sp>, Ep)`, definiendo el nuevo entorno como `Ep = CE + {<z1> -> E(<y1>),..., <zn> -> E(<yn>)}`.

## Condicional

En el tope del stack, tenemos: `(if <x> then <s1> else <s2> end, E)`

También es suspendible, ya que debe estar determinado `E(<x>)`. Si está determinado, debe ser un booleano (en otro caso, lanza error).

Si `E(<x>)` tiene valor `true`, entonces apila `(<s1>, E)` la pila. Si tiene valor `false`, apila `(<s2>, E)` a la pila.

## Pattern Matching

En el tope del stack, tenemos: `(case <x> of <l>(<f1>:<x1>... <fn>:<xn>) then <s1> else <s2> end, E)`

Es suspendible, se activa si `E(<x>)` está definido. Si se cumpla el patrón, se apila al stack `(local <x1>=<x>.<f1>... <xn>=<x>.<fn> in <s1> end, E)`. Sino, se apila `(<s2>, E)`.

Notemos que se agrega un `local` automáticamente, por lo que no debemos declararlo.

## Excepciones

En el top del stack, tenemos: `(try <s1> catch <x> then <s2> end, E)`

1. Se apila al stack `(catch <x> then <s2> end, E)`
2. Se apila `(<s1>, E)`
