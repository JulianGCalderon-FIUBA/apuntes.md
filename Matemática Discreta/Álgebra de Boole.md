El álgebra de *Boole* es un espacio vectorial de forma axiomática. Se definen los siguientes elementos:

$$
(B, +, \cdot, ', O_B, 1_B)

$$

1. $O_B \neq 1_B \in B$
2. $+: B\times B \to B,\quad x+y$
3. $\cdot: B\times B \to B,\quad xy$
4. $': B \to B,\quad x’$

Estos elementos, deben satisfacer los siguientes axiomas:

1. Conmutatividad: $\forall x,y \in B: x+y = y+x, \quad xy = yx$
2. Distributividad: $\forall x,y,z \in B: x(y+z) = xy+xz, \quad x+yz = (x+y)(x+z)$
3. Neutros: $\forall x \in B: x + 0_B = x, \quad x1_B = x$
4. Complementos: $\forall X \in B: x + x’ = 1_B, \quad xx' = 0_b$

A partir de los axiomas, podemos demostrar el resto de propiedades del algebra de bool:

1. Acotación: $1 + x = 1, 0x = 0$
2. Asociativa: $(x+y)+z = x + (y + z), (xy)z = x(yz)$
3. Involución: $(x')' = x$
4. De Morgan: $(x+y)' = x'y', (xy)' = x' + y'$
5. Idempotencia: $x+x = x, xx=x$
6. Absorción: $x + xy = x, x(x+y)=x$

Decimos que un álgebra de ***Boole*** tiene definido un orden natural cuando $x\leq y \iff xy = x$

## Pruebas de Unicidad

Las pruebas de unicidad se suelen demostrar de la misma forma. Se supone que no hay unicidad y se elaboran las expresiones hasta llegar a que estos dos valores son el mismo.

Cuando demostramos algo en el álgebra de ***Boole***, podemos inmediatamente asumir que su dual es válido también. Esto se debe a que todos los axiomas son duales, si se intercambia $0_B$ por $1_B$ y $\cdot$ por $+$, entonces la expresión sigue siendo completamente válida.

## Pruebas de equivalencia

Se parte de una de las expresiones de la igualdad y, aplicando axiomas y propiedades derivadas de los axiomas, se llega a la segunda expresión. En algunos casos, también podemos utilizar los supuestos planteados para la igualdad (hipótesis).

## Átomos

En el álgebra de ***Boole***, se llama *átomo* a los sucesores inmediatos del $O_B$. En otras palabras, $a \neq 0_B$ es un ***átomo*** si y sólo si

$$
\forall x \in B, \quad ax = b \implies x=a \lor x=0_B
$$

Es decir, si $x \leq b$, entonces $x$ deberá ser el propio elemento o el elemento neutro $0_B$.

El producto de dos átomos distintos es $0_B$

$$
a_1a_2 = 0_B
$$

Todo elemento del álgebra puede anotarse como una combinación de los átomos del conjunto.

$$
\forall x \in B: x = \alpha_1a_1 + \alpha_2a_2 + \cdots + \alpha_na_n
$$

Donde $a_1, \cdots, a_n$ son átomos en $B$ y $\alpha_1, \cdots, \alpha_n \in \{0_B, 1_B\}$

Como todos los elementos del álgebra pueden anotarse como una combinación de los átomos, entonces la cantidad de elementos del álgebra será $|B| = 2^n$, donde $n$ es la cantidad de átomos. Si un conjunto cumple los axiomas del algebra de boole, entonces esta propiedad se cumplirá.

## Cotas

Sea $(A, \leq)$ un *poset* y sea $S \in A, S \ne 0$:

- $m \in A$ es una cota inferior de $S$ sii $\forall x \in S, m \leq x$.
- $M \in A$ es una cota superior de $S$ sii $\forall x \in S, x \leq M$.

Un conjunto que admite cota superior (inferior) se llama superiormente (inferiormente) acotado. Si admite ambas se llama acotado.

- $x \in S$ es minimal (maximal) de $S$ sii $\forall y \in S, \color{}{y \leq x} \ \color{blue}{(y \geq x)}$
- $u \in S$ es mínimo (máximo) de $S$ sii $\forall x \in S: \color{red}{u \leq x}\ \color{blue}{(u \geq x)}$. Se elemento se denota comúnmente como $u = \color{red}{\min S}\ \color{blue}{(\max S)}$
- $u \in A$ es el ínfimo (supremo) de $S$ sii $S$ está inferiormente (superiormente) acotado y además $u$ es la máxima (mínima) cota inferior (superior). Se denota como $u = \color{red}{\inf S}\ \color{blue}{(\sup S)}$

> [!note]
> Si $S$ tiene mínimo, es único. Esta observación también es análoga para el máximo.

> [!note]
> Si $u = \min S$ entonces $u$ la mayor de las cotas inferiores, y además pertenece a $S$. Esta observación también es análoga para el máximo.

## Isomorfismos

Sean $B_1, B_2$ dos álgebras de Boole, se dice que son isomorfas si preservan sus tres leyes a través de $f: B_1 \to B_2$ biyectiva tales que:

1. $\forall x,y \in B_1: f(x +_1 y) = f(x) +_2 f(y)$
2. $\forall x,y \in B_1: f(x \cdot_1 y) = f(x) \cdot_2 f(y)$
3. $\forall x \in B_1: f(x^{'_1}) = f(x)^{'_2}$

Se puede demostrar que si preserva algunas dos de las tres leyes mostradas, entonces preserva las tres.

Si se cumplen estas tres leyes, entonces podemos demostrar que se preservan también los siguientes elementos:

- **Neutro:** $f(0_{B_1}) = 0_{B_2}$
- **Orden:** $\forall x,y \in B_1: x\leq_1 y \to f(x) \leq_2 f(y)$
- ***Átomos:*** Si $a$ es átomo en $B_1$, entonces $f(a)$ es átomo en $B_2$.

Como cualquier elemento del álgebra de Boole se puede escribir como combinación de los átomos, entonces para definir un isomorfismo basta con definir la transformación de sus átomos. De esta forma definimos la cantidad de isomorfismos posibles entre dos algebras como $n!$, siendo $n$ la cantidad de átomos (ambas álgebras tendrán el mismo numero de átomos).
