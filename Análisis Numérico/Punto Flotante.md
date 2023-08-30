Para representar números con valores decimales, la computadora los guarda en memoria con una terna de tres valores $(s, c, q)$ en base binaria

$$

\begin{align*}
\mathscr M = &\Big\{m:m = (-1)^s\cdot c \cdot 2^q\Big\}\\
&s \in \{0, 1\}\\
&c = 1.b_1b_2b_3\dots b_p\\
&q:E_{min} \leq q \leq E_{max}
\end{align*}
$$

Definiendo:

- $s:$ Signo, Indica si es positivo o negativo.
- $c:$ Mantisa, le da significado al número.
- $q:$ Exponente, le da magnitud al número.

Podemos observar en la siguiente imagen, los formatos típicos de los números de máquinas

![[Punto Flotante 1693351678.png|475]]

## Propiedades

- Los números de máquina son un subconjunto finito de los números racionales.
- Son más densos cerca del $0$ y se separan a medida que se alejan de él.
- La cota de error relativo para cualquier número distinto de $0$ es constante.
- Si intentamos almacenar un número más grande que la cota máxima obtendremos una excepción llamada **overflow**.
- Si intentamos almacenar un número más chico que la cota mínima obtendremos una excepción llamada **underflow**.
- Cuando queremos almacenar un número cualquiera, la computadora lo redondea al número de máquina más cercano.
