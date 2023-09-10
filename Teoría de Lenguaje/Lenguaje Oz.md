El sistema **Mozart** es una implementación del lenguaje de programación **Oz**, un lenguaje de programación multi-paradigma, con orientación en concurrencia. El lenguaje utiliza el modelo **declarativo**. Las instrucciones son declaraciones.

## Browse

Para imprimir en el navegador, utilizamos el procedimiento `Browse`.

```Oz
{Browse '¡Hola Mundo!'}
```

Este procedimiento es ejecutado en un hilo distinto.

## Variables

La asignación de variables es simple, con tipado dinámico. Es necesario que las variables comiencen con mayúscula.

```Oz
declare A B Var
A = 4
B = 5
Var = A*B + 3
{Browse Var} %23
```

En un modelo declarativo, las variables pueden ser pensadas como atajos a los valores. Son inmutables y de única asignación.

```Oz
declare A
A = 4
A = 7 % No está permitido
```

Debido a esta limitación, la mayoría de los problemas se resuelven utilizando recursividad y entornos.

Podemos limitar el ambiente de variables a un entorno particular.

```Oz
local A B Var in
	A = 4
	B = 5
	Var = A*B + 3
	{Browse Var} %23
end
```

En un entorno global, las variables pueden ser accedidas en todo el programa, lo cual puede traer problemas.

Las variables pueden ser reasignadas al definir un nuevo entorno.

```Oz
local A in
	A = 4
	local A in
		A = 7
		{Browse A} %7
	end
end
```

Si se referencia a una variable que no pertenece al entorno, se buscara en un entorno superior.

No importa de qué lado se encuentra la variable en una asignación.

```Oz
declare A B Var
4 = A
A + 1 = B
A*B + 3 = Var
{Browse Var} %23
```

El orden de la ejecución, tampoco es importante. Todas las instrucciones son **declaraciones** independientes.

```oz
declare A B Var
A + 1 = B
A*B + 3 = Var
4 = A
{Browse Var} %23
```

## Funciones

Podemos definir funciones, estas deben tener un nombre y una lista de parámetros. Deben ser declaradas como variables.

```Oz
declare Mayor A B M
fun {Mayor X Y}
	if (X > Y) then X else Y end
end

A = 30
B = 20
M = {Mayor A B}
{Browse M} %30
```

Los lenguajes se dividen en expresiones y declaraciones. Los valores solos son expresiones. Las funciones devuelven las expresiones sueltas, sin necesidad de agregar un `return`. Solo puede haber una expresión suelta en una función.

Una función es una expresión, debe estar asignada a algo. Para definir una función sin valor de retorno, utilizamos procedimientos.

```Oz
declare Imprimir
proc {Imprimir Msg}
	{Browse Msg}
end
```

## Procedimientos

Los procedimientos son conceptos aún más básicos que las funciones. Se utilizan variables no ligadas como parámetros.

Los procedimientos no devuelven un valor. El procedimiento puede ligar un valor a esa variable, y ser utilizado luego de la llamada al procedimiento.

```Oz
declare Suma A B Z in
proc {Suma A B Z}
	Z = A + B
end
A = 10
B = 5
{Suma A B Z}
{Browse Z} % 15
```

## Records

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

## Binding

El **binding** consiste en asignarle un valor literal a una variable.

El **variable binding** consiste en ligar el valor de una variable a partir de otra

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

## Pattern Matching

Es una manera de acceder a los campos de una estructura de datos y obtener los valores

Un patrón *matchea* sobre un registro cuando coincide en su largo, etiqueta, y características.

```Oz
declare EsVacio L

proc {EsVacio L}
	case L of H|T then
		{Browse 'No'}
	else
		{Browse 'Si'}
	end
end

L = nil
{EsVacio L} % Si
```

El *pattern matching* trata de asignar la variable al patrón. Si es posible hacerlo, entonces el patrón coincide.

```Oz
declare L H T
L = [10 20 30] % 10|20|30|nil
L = H|T
{Browse H} % 10
{Browse T} % [20, 30]
```

Esto puede ser utilizado para, por ejemplo, calcular el largo de una lista

```Oz
declare Largo L Res
fun {Largo L}
	case L of H|T then
		{Largo T} + 1
	else
		0
	end
end

L = [10 20 30]
Res = {Largo L}
{Browse Res} % 3
```

También pueden utilizarse múltiples patrones

```Oz
declare EsVacio L1 L2 L3
fun {EsVacio L}
	case L of H|T then
		{Browse 'No'}
	[] nil then
		{Browse 'Si'}
	else
		{Browse 'No es una lista'}
	end
end

L1=[10]
L2=nil
L3=10

{EsVacio L1} % No
{EsVacio L2} % Si
{EsVacio L3} % No es una lista
```
