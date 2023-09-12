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
{Browse Var} % 23
```

En un modelo declarativo, las variables pueden ser pensadas como atajos a los valores. Son inmutables y de única asignación.

```Oz
declare A
A = 4
A = 7 % No está permitido
```

Debido a esta limitación, la mayoría de los problemas se resuelven utilizando recursividad y entornos.

No importa de qué lado se encuentra la variable en una asignación.

```Oz
declare A B Var
4 = A
A + 1 = B
A*B + 3 = Var
{Browse Var} % 23
```

El orden de la ejecución, tampoco es importante. Todas las instrucciones son **declaraciones** independientes.

```oz
declare A B Var
A + 1 = B
A*B + 3 = Var
4 = A
{Browse Var} % 23
```

Para declarar números negativos, utilizamos el símbolo `~`.

```Oz
declare A
A = ~3
{Browse A} % ~3
```
