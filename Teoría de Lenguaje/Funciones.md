Podemos definir funciones, estas deben tener un nombre y una lista de parámetros. Deben ser declaradas como variables.

```Oz
declare Mayor A B M
fun {Mayor X Y}
	if (X > Y) then X else Y end
end

A = 30
B = 20
M = {Mayor A B}
{Browse M} % 30
```

Los lenguajes se dividen en expresiones y declaraciones. Los valores solos son expresiones. Las funciones devuelven las expresiones sueltas, sin necesidad de agregar un `return`. Solo puede haber una expresión suelta en una función.

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

Para imprimir en el navegador, utilizamos el procedimiento `Browse`.

```Oz
{Browse '¡Hola Mundo!'}
```

Este procedimiento es ejecutado en un hilo distinto.

