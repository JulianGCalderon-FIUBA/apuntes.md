Para representar números con valores decimales, la computadora los guarda en memoria con una terna de tres valores $(s, c, q)$ en base binaria

$$

\begin{align*}
\mathscr M = &\Big\{m:m = (-1)^s\cdot c \cdot 2^q\Big\}\\
&s \in \{0, 1\}\\
&c = 1.b_1b_2b_3\dots b_p\\
&q:E_{min} \leq q \leq E_{max}
\end{align*}
$$

$s:$ Signo, Indica si es positivo o negativo.

$c:$ Mantisa, le da significado al numero.

$q:$ Exponente, le da magnitud al numero.

![[Punto Flotante 1.png]]

Formatos típicos de los números de maquina.

## Propiedades

- Los números de maquina son un subconjunto finito de los números racionales.
- Son mas densos cerca del $0$ y se separan a medida que se alejan de el.
- La cota de error relativo para cualquier numero distinto de $0$ es constante.
- Si intentamos almacenar un numero mas grande que la cota maxima obtendremos una excepción llamada **overflow**.
- Si intentamos almacenar un numero mas chico que la cota minima obtendremos un a excepción llamada **underflow**.
- Cuando queremos almacenar un numero cualquiera, la computadora lo redondea al numero de maquina mas cercano.
