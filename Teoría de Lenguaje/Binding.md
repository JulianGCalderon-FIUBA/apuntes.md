Existen dos formas de asignarles valores a una variable.

El **binding** consiste en asignarle un valor literal a una variable. Es el más simple

```Oz
declare X
X = 5
{Browse X} % 5
```

El **variable binding** consiste en ligar el valor de una variable a partir de otra. No es necesario que la otra variable este definida, es simplemente una declaración.

```Oz
```
declare X
X = 5
{Browse X} % 5

El **partial value** se da cuando una característica registro tiene una variable asignada a una característica.

Cuando realizamos un *variable binding* entre registros con valores parciales, el programa hará su mayor esfuerzo para igualarlos. Si no puede, fallará.

```Oz
declare X Y A B in
X = rec(10 B)
Y = rec(A 40)
X = Y
{Browse A} % 10
{Browse B} % 40
```

Si tratamos de ligar dos estructuras con distintas características, el programa falla.
