Los registros son estructuras de datos para agrupar referencias. Se componen de una etiqueta *(label)* y múltiples características *(features)*. Cada característica puede tener valores asociados

```Oz
declare Arbol ArbolDer
Arbol = arbol(valor:4 izq:nil der:ArbolDer)
ArbolDer = arbol(valor:5 izq:nil der:nil)
{Browse Arbol}
```

Las etiquetas, así como las características, se escriben en minúscula. Se denominan **literales**. El valor *nil* también es un literal.

Hay distintas funciones disponibles para los registros:

- `Label` nos devuelve su etiqueta
- `Arity` nos devuelve sus características
- `Width` nos devuelve la cantidad de características

## Tuplas

Una tupla es un registro en el cual sus características son enteros, empezando por el 1.

```Oz
declare Numeros
Numeros = numeros(3 5 2 5)
{Browse Numeros.1} % 3
```

## Listas

Una lista es una tupla con dos elementos. Uno es el primer elemento, y el segundo es el resto de la lista. La lista se construye con `[]`, `|`, o `'|'()`

```Oz
declare L1 L2 L3
L1 = [10 20 30]
L2 = 10|20|30|nil
L3 = '|'(10 '|'(20 '|'(30 nil)))

{Browse L1.1}
{Browse L1.2.1}
{Browse L1.2.2.1}
```

La lista se recorre de forma recursiva. A esto se debe la naturaleza de su estructura
