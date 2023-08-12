## Definiciones Básicas

Un conjunto finito no vacío de elementos se denomina **alfabeto**, es designado con $\Sigma$.

Un elemento $a \in \Sigma$ se denomina **letra**.

Una sucesión de letras es una **palabra**. Por ejemplo, $x = abaac$. Llamamos **longitud** a la cantidad de letras de una palabra, designada $|x| = 5$.

Existe una única palabra de longitud cero denominada **palabra nula**, denotada con $\lambda, |\lambda| = 0$

Las palabras pueden ser **concatenadas** a partir del operador **producto**. Sea $x = aab, y = abbc$. Entonces $z= xy = aababbc$. Definiremos la longitud como $|z| = |xy| = |x| + |y|$. Se puede concatenar con la palabra nula. $a\lambda = \lambda a = a$

## Lenguaje

Sea $\Sigma$ un alfabeto, denominaremos $\Sigma^q$ simplemente como el producto de $\Sigma$, $q$ veces. También puede ser pensado como el conjunto de palabras formadas por $\Sigma$ con longitud $q$. Definiremos inicialmente $\Sigma^0 = \{\lambda\},\ \Sigma^1 = \Sigma$

La clausura del alfabeto es el conjunto de palabras que se puede formar utilizando ese alfabeto. Se define como $\Sigma^* = \Sigma^0 + \Sigma^1 + \cdots$.

## Lenguajes Regulares

Un lenguaje es regular si sus palabras se expresan con expresiones regulares. Las expresiones regulares se expresan a partir palabras, letras, y los operadores $+, \cdot, *$. Una expresión regular debe cumplir los 5 axiomas de las expresiones regulares, pero escapan del alcance de la materia.

$$
x = ab^*b = \{ab, abb, abbb, \cdots\}
$$

$$
a+b = \{a,b\}
$$

$$
(a+b)^* = \{a, b, aa, ab, ba, \cdots\}
$$

## Autómatas

Se designa $M=(\Sigma, Q, q_0, \Upsilon, F)$ el **autómata finito determinístico (DFA)** donde:

- $\Sigma$ es un alfabeto
- $Q$ es un conjunto de estados
- $Q_0 \in Q$ es un estado inicial. Puede haber múltiples, pero todo autómata de múltiples estados iniciales puede reducirse a uno de un solo estado.
- $\Upsilon: Q\times \Sigma \to Q$ es la función de transición
- $F \subset Q$ es el conjunto de aceptación

Podremos representar la función de transición a partir de una tabla, o a partir de un grafo dirigido. El estado inicial suele indicarse con una flecha $\stackrel{\text{in}}{\to}$ y en rojo. Los estados que pertenecen al conjunto de aceptación se muestran en un doble circulo y en verde

Se puede crear una función de transición generalizada que toma cualquier palabra:

$$
\Upsilon^*: Q \times E^* \to Q
$$

Definimos $L(M)$ como el elnguaje reconocido por el automata

$$
L(M) \stackrel{\text{def}}{=} \Big\{ x \in \Sigma^*: \Upsilon(q_0, x) \in F\Big\}
$$

> [!note]
> Siempre existe un ***DFA*** para un lenguaje regular, y los ***DFA*** solo dan lenguajes regulares

> [!note]
> Existen infinitos autómatas para un mismo lenguaje, pero solo hay uno minino (con menor cantidad de estados)

### Minimización de Autómatas

Sea $M$ un autómata y $k \in \mathbb{N}_0$, se define que un estado $q$ es $R_k{-}\text{equivalente}$ al estado $r$ si y solo si:

$$
\forall x \in \Sigma^*: |x| \leq k \to \Big(\Upsilon^*(q, x),\Upsilon^*(r,x) \subset F\Big) \lor \Big(\Upsilon^*(q, x),\Upsilon^*(r,x) \subset F'\Big)
$$

Podemos probar que si dos estados están en relación $R_k$, también estarán en relación $R_{k-1}$ (si se cumple para toda palabra con longitud menor a $k$, también se cumplirá para toda palabra con longitud menor a $k-1$.

$$
\forall x,y \in Q, xR_ky \to xR_{k-1}y
$$

El autómata cociente se construye con las clases $R_*{-}\text{equivalentes}$. Sin embargo, el proceso de partición de clases no puede seguir indefinidamente, ya que finaliza cuando ya no puedo subdividir más las clases

El mínimo se alcanza tras $|Q|$ pasos (en este caso el autómata ya era mínimo) o tras llegar a $R_k = R_{k+1}$

El autómata mínimo se puede escribir como $\overline M = (\Sigma, Q/R_*, [q_o], \overline\Upsilon, \overline F)$. Cómo se cumple que $L(\overline M) = L(M)$, muchas veces para hallar el lenguaje conviene buscar el autómata mínimo.
