Sean $A, B$ dos conjuntos, entonces definimos como $B^A$ como el conjunto de funciones posibles que van del conjunto $A$ al conjunto $B$

$$
B^A \ \overset{\text{def}}{=}\  \Big\{f: A \to B\Big\}
$$

De igual forma, podemos definir la cantidad de funciones (cardinalidad) como

$$
|B^A| = |B|^{|A|}
$$

Nota: En este documento se utilizará la notación $\subseteq$ para mayor claridad, sin embargo, en la materia el simbolo $\subset$ tambien denotara inclusión o igualdad. Para ser explícitos en que queremos un subconjunto que estrictamente incluido, utilizaremos la siguiente notación: $(A\subset B, A\neq B)$

## Álgebra de Proposiciones

> [!note]
> Si en particular $|B| = 2$, entonces $B^A = 2^{|A|}$

> [!note]
> **Proposición:** Afirmación que sólo puede tomar dos valores

La función proposicional del argumento $x$ escrita como $p(x)$ se convierte en una proposición $p(a)$ cuando al argumento $x$ se le asigna un valor fijo $a$, tomado de un conjunto de referencia $I$.

Sean $A, B$ proposiciones, entonces tendremos 4 funciones $f(p)$ de una variable proposicional. Podremos visualizar estas cuatro funciones en una tabla de verdad.

$$
\begin{array}{|c||c:c:c:c|}
\hline
p & F & p & p' & T\\
\hline
0 & 0 & 0 & 1 & 1\\
1 & 0 & 1 & 0 & 1 \\
\hline
\end{array}
$$

Para el caso de dos variables proposicionales, tendremos 16 funciones proposicionales $f(p,q)$

$$
\begin{array}{|c||c:c:c:c:c:c:c:c|}
\hline
p & F & p & q & p + q & pq & p \to q &q \to p & p\iff q\\
\hline
0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 \\
0 & 1 & 0 & 1 & 1 & 0 & 1 & 0 & 0\\
1 & 0 & 1 & 0 & 1 & 0 & 0 & 1 & 0\\
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1\\
\hline
\end{array}
$$

Están definidas 8 proposiciones, ya que faltan los complementos de todas las proposiciones.

Particularmente, diremos que si tenemos $n$ variables proposicionales, entonces la cantidad de funciones proposicionales que podemos formar con estas son:

$$
|B^A| = 2^{2^n}
$$

$$
|A| = 2^n
$$

Algunos matemáticos dicen que $p → q$ es la proposición más importante de todas. Esta es la proposición $p$ implica $a$. Solo puede ser falsa cuando la proposición $p$ es verdadera, pero su implicación $q$ no lo es. La forma de negar un teorema de este estilo es justamente encontrar algún caso para el cual $p$ se cumple, pero $q$ no.

Podemos definir las implicancias utilizando los elementos del álgebra de boole.

$$
p \to q \overset{\text{def}}{=} p' + q
$$

$$
q \to p \overset{\text{def}}{=} q' + p
$$

Se reserva $p \implies q$ para denotar que la condicional $p \to q$ es verdadera.

$$
p \leftrightarrow q \quad \overset{\text{def}}{=} \quad (p \to q)(q \to p) 
$$

A partir de las definiciones, podemos demostrar rápidamente que:

$$
\begin{align*}
p \to q = q'\to p'
\end{align*}
$$

La función binaria **Sheffer** denominada usualmente **NAND** se simboliza con $\uparrow$ y se define de la siguiente manera

$$
p\uparrow q\overset{\text{def}}{=} (pq)'
$$

La función binaria **Peirce** denominada usualmente **NOR** se simboliza con $\downarrow$ y se define de la siguiente manera

$$
p\downarrow q\overset{\text{def}}{=} (p+q)'
$$

Ambas funciones admiten versiones $n$-arias que aceptan más de dos proposiciones como argumentos. Se definen de la siguiente manera

$$
p_1\uparrow p_2 \uparrow \cdots \uparrow p_3 \overset{\text{def}}{=} (p_1p_2\cdots p_3)'
$$

$$
p_1\downarrow p_2 \downarrow \cdots \downarrow p_3 \overset{\text{def}}{=} (p_1 + Pp_2 + \cdots + p_3)'
$$

Otra función importante es la diferencia, simbolizada $A-B$. Representa aquellos elementos que se encuentren en $A$ pero no en $B$.

$$
A-B \overset{\text{def}}{=} AB'
$$

El **or** exclusivo se simboliza con $A \oplus B$ y representa aquellos elementos que se encuentren en $A$ o en $B$, pero no en ambos. Es el complemento de si solo si.

$$
A \oplus B \overset{\text{def}}{=} A'B + AB'
$$

## Densidad de Verdad de una Proposición

Definiremos la densidad de verdad de una proposición como el porcentaje de elementos del dominio que afirman la proposición. Por ejemplo, sea

$$
f(p,q) = p + p'q
$$

Calcularemos la densidad como

$$
\delta\Big(f(p,q)\Big) = \frac34 = 75\%
$$

## Conjuntos de Veracidad

Sea $I$ un conjunto de referencia y $P$ un subconjunto de $I$, entonces definimos

$$
p(x) = \begin{cases}
1 \gets x \in P \\
0 \gets \text{e.o.c.}
\end{cases}
$$

Diremos que $P$ es el conjunto de veracidad de la función proposicional $p(x)$. Son aquellos valores de $x$ para los cuales el $p(x) = 1$. Podremos definir operaciones entre los conjuntos de veracidad:

> [!note]
> **Disyunción**: Definimos la disyunción $P\cup Q$ como el conjunto de elementos que se encuentran o en $P$, o en $Q$. De forma análoga, considerando las funciones proposicionales correspondientes $p + q$.

> [!note]
> **Conjunción:** Definimos la conjunción $P\cap Q$ como el conjunto de elementos que se encuentran tanto en $P$ como en $Q$. De forma análoga, considerando las funciones proposicionales correspondientes, denotamos $pq$

> [!note]
> **Negación:** Definimos la negación $P'$ como el conjunto de elementos que no pertenecen a $P$. De forma análoga, considerando las funciones proposicionales correspondientes, denotamos $p'$

## Demostraciones de Equivalencia

Para demostrar que dos proposiciones $p, q$ son equivalentes, debemos demostrar la doble inclusión para sus conjuntos de veracidad. Esto es:

1. $P \subseteq Q$
2. $Q \subseteq P$

Otra forma de demostrar la igualdad de dos funciones es que estas toman en el mismo valor para todo elemento del dominio. Aprovechando que las proposiciones únicamente tienen dos valores, basta con demostrar que se cumple que $v(p) = 1$ si y sólo si $q(p) = 1$. Nótese que el análisis análogo con $v(p) = 0$ también es valido.

Para las demostraciones en los conjuntos de veracidad, usualmente será más simple si tratamos de hallar una expresión equivalente igualada al vacío. Para esto, utilizaremos la identidad

$$
A = B \iff A'B + AB' = \emptyset
$$

Cuando nos hallamos con una inclusión, esta podrá ser remplazada con una igualdad.

$$
A \subseteq B \iff AB = A
$$

Es muy importante utilizar las definiciones, los supuestos, y las propiedades en cada paso del desarrollo, para demostrar la equivalencia de forma correcta.

A veces, demostrar una implicancia es complicada, por lo que se puede trabajar con la contrarrecíproca, la cual es equivalente. A su vez, la contraria es equivalente a la reciproca

$$
\text{Original}: p \to q
$$

$$
\text{Contraria}: p' \to q'
$$

$$
\text{Reciproca}: q \to p
$$

$$
\text{Contra-reciproca}: q' \to p'
$$

## Equivalencias Útiles

Muchas veces se utilizan identidades para reescribir una expresión de forma que resulta más conveniente para trabajar. Las siguientes 6 expresiones son equivalentes:

1. $X \subseteq Y$
2. $XY = X$
3. $X + Y = Y$
4. $XY' = \emptyset$
5. $X’ + Y = I$
6. $Y’ \subseteq X’$

Es más simple trabajar con expresiones que están igualadas al vacío (o a la identidad). Debido a esto, trabajaremos con las siguientes 3 expresiones equivalentes.

1. $X = Y$
2. $X'Y + XY' = 0$
3. $(X'+Y)(X + Y') = I$

## Invalidez de la Cancelación

$$
\begin{align*}
\text{En los numeros reales }: \quad& p + q = q \implies p = 0 \\
\text{En logica proposicional}: \quad& p + q = q \implies p = pq \\
\text{En algebra de conjuntos}: \quad& p + q = q \implies p \subset Q
\end{align*}
$$

En álgebra de conjuntos y de proposiciones, la **cancelación** de términos es inválida. Notemos que si bien las soluciones triviales son válidas, estas no son la solución completa.

## Forma Canónica de Proposiciones

Existen dos formas canónicas. La primera se llama forma canónica de suma de productos. Busca representar las regiones de validez a partir de productos sumados

$$
f(p, q, r) = pqr + pq'r + pqr' + p'qr + pq'r'\tag{Ej.}
$$

Otra forma es la de representar las regiones de invalidez a partir de un producto de sumas

$$
f(p, q, r) = (p + q + r)(p + q + r')(p + q' + r)\tag{Ej.}
$$

Nótese que la primer forma tiene 5 términos, mientras que la segunda tiene 3 términos. Sumando a un total de 8 regiones (el cardinal del dominio).

## Identidades del Álgebra de Proposiciones

$$
\begin{align*}

\text{a) Conmutatividad}&:\quad p + q = q + p,\quad pq=qp \\

\text{b) Distributividad}&:\quad p(q+r) = pq + pr,\quad p+qr=(p+q)(p+r) \\

\text{c) Neutros}&:\quad p+F = p,\quad pT = p \\

\text{d) Complementos}&:\quad p + p' = T,\quad pp'=F,\quad T' = F \\

\text{e) Acotacion}&:\quad p + T = T,\quad pF=F \\

\text{f) Asociatividad}&:\quad (p +q)+r = p+(r + q),\quad (pq)r=p(qr) \\

\text{g) Involucion}&:\quad (p')' = p \\

\text{h) De Morgan}&:\quad (p + q)' = p'q',\quad (pq)'=p'+q' \\

\text{i) Idempotencia}&:\quad p + p = p,\quad pp=p \\

\text{j) Absorcion}&:\quad p + pq = p,\quad p(p+q) = p\\

\end{align*}
$$

Nota: en sus respectivos conjuntos de igualdad se cumplen las mismas identidades.

Las leyes de **De Morgan** también se cumplen para las operaciones $\uparrow$ y $\downarrow$

$$
(p\uparrow q)' = p'\downarrow q'
$$

$$
(p\downarrow q)' = p'\uparrow q'
$$

## Soluciones del Algebra de Proposiciones

En el álgebra de proposiciones, encontrar soluciones a ecuaciones no es tan directo como en los reales. Solucionar la $X$ de una ecuación implica encontrar las cotas inferiores y superiores de la misma. La solución usualmente tomará la siguiente forma.

$$
f(X) \subseteq X \subseteq g(X)
$$

## Juegos Completos

> [!note]
> Un juego se llama completo si alcanza para fabricar cualquier elemento del conjunto donde se un juego completo

**Teorema:** El juego $(+,\cdot, ')$ es un juego completo en el espacio de proposiciones. Podemos construir cualquier función proposicional a partir de estos elementos.

Se puede demostrar, a partir de equivalencias, que los siguientes juegos también son completos. Para hacerlo, deberá tratar de expresarse la operación faltante como una combinación de los elementos disponibles.

- $(+,')$
- $(\cdot,')$
- $(\to,')$
- $(\uparrow)$
- $(\downarrow)$
