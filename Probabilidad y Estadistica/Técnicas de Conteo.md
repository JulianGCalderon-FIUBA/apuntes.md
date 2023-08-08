# Regla del Producto

Dados dos conjuntos $A,B$ con $n_a, n_b$ elementos. La cantidad de pares ordenados que pueden formarse son

$$
\#AB = n_a \cdot n_b
$$

# Permutaciones

Cantidad de formas distintas que puedo ordenar $n$ elementos.

$$
\#AB = n!
$$

## Variaciones

Si solo quiero ordenar $m$ elementos de los $r$ totales, entonces debo usar variaciones

$$
\#A = \frac{n!}{(n- r)!}
$$

En la calculadora, se puede calcular con la combinación de teclas: $n \ \boxed{\texttt{nPr}} \ r$

## Anagramas

En el caso de los anagramas, es un problema de permutaciones con elementos repetidos

$$
\text{Sea } n = n_1, n_2, n_3, \cdots\\\ \\
\#A = \frac{n!}{n_1!n_2!n_3!\cdots}
$$

Esto se debe a que a las permutaciones totales, debo descontar las permutaciones entre las mismas letras.

# Combinaciones

Puedo calcular la cantidad de conjuntos no ordenados de $r$ de los $n$ elementos totales que puedo formar. Como los conjuntos no son ordenados, no importa el orden en el que represento los elementos del conjunto.

$$
\#A = \frac{n!}{(n-r)!\cdot r!} = \binom{n}{r}
$$

En la calculadora, se puede calcular con la combinación de teclas: $n \ \boxed{\texttt{nCr}} \ r$

## Anagramas

Tambien podemos resolver el caso con combinatoria

$$
\text{Sea } n = n_1, n_2, n_3, \cdots \\\ \\
\#A = \binom{n}{n_1}\binom{n - n_1}{n_2}\binom{n-n_1-n_2}{n_3}\cdots
$$

Lo podemos pensar como que de las $n$ posiciones posibles, elijo $n_1$ opciones para colocar la primer letra. Luego repito la misma lógica para el resto de letras.

# Modelo Bose-Einstein

Para resolver un problema del estilo urnas y bolitas indistinguibles, puedo pensar el problema como un anagrama. Separando las bolitas en urnas utilizando ceros y unos.

$$
\underbrace{0010010100}_{7 \text{ bolitas},\ 4 \text{ urnas}}
$$

Luego puedo resolver el problema como si fuera un anagrama.

$$
\#A = \binom{10}{7}\binom{3}{3} = \frac{10!}{7!\cdot 3!}
$$