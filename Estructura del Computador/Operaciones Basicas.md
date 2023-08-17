---
title: Operaciones Basicas
---

## Complemento

Complemento de un número en base $b$ índica cuanto le falta al número para llegar a su base. Si $n > b$, entonces su complemento indica cuanto le falta al número para llegar al número de la base seguido de tantos dígitos como $n$. Es decir, su distancia a $b^d$ siendo $d$ los dígitos de $n$

## Sumar en Base $b$

Sumo columna a columna partir del siguiente método. Siendo $n$ el mayor y $m$ el menor.

1. Tomo el número más grande $n$
2. Busco su complemento $c$
3. Si $m-c ≥ 0$, me llevo $1$ a la siguiente columna y lo dejo como resultado
4. Si no, dejo como resultado simplemente a $m + n$.

## Restar en Base $b$

Para usar una resta, puedo aplicar la siguiente equivalencia para evitar restar

$$
\begin{gathered}
A - B = C\\
A + C_{b_B} B = C + r^{d_B}
\end{gathered}
$$

Una vez terminada la suma, desecho el dígito extra

Si el número obtenido no tiene dígito extra, significa que el resultado es negativo. En este caso, el resultado que queremos es el complemento en base $b$ del número obtenido. (luego le agrego el signo)

## Multiplicación por Múltiplo de Base

Si multiplico el número por $b^n,\ \forall n\in\mathbb{Z}$. Entonces desplazo los dígitos del número a izquierda o derecha, dependiendo del signo de $n$. Si $n$ es positivo, desplazo los dígitos hacia la izquierda.

Si se trata de un número en representación, entonces el primer bit se mantiene igual.

## Flags

Los flags se generan siempre luego de una operación, depende de nosotros interpretar los números que se almacenan allí.

- **C - Carry:** Cuando una operación devuelve más bits del que podemos almacenar, el bit extra se almacena en el carry. (por defecto un cero)
- **V - Overflow**: Indica si ocurrió un overflow en el caso de números con signo.
- **Z - Cero:** Indica si el resultado dio cero.
- **N - Negativo:** Indica si el resultado dio negativo. Es una copia del primer bit.
- **P - Paridad:** Indica si el número tiene una cantidad par de unos.
