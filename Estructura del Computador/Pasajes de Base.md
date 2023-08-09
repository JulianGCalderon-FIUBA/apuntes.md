## Pasaje de Base $B$ a Base 10

La suma de los pesos de un símbolo es el numero en sistema decimal. $d_{1 \to n}$ son los dígitos de $a$ en la base $b$

$$
a_{10} = d_{-2} b^{-2} + d_{-1} b^{-1} + d_0 b^0 + d_2b^2 + d_3b^3
$$

Se utiliza el subíndice para representar la base del numero

$$
a \text{ en base } n: a_n
$$

## Pasaje de Base 10 a Base $B$

1. Divido $n$ entre $B$ $\frac nB = C\cdot B + R$
2. Divido $C$ entre $B$
3. Repito con el nuevo cociente hasta que $C$ = 0

Los dígitos del numero en base $B$ son los restos de las divisiones desde el principio al final.

Si $n$ tiene números decimales:

1. Tomo los números decimales y los divido por la base.
2. Extraigo la porción entera del numero y la anoto como decimal
3. Repito hasta llegar a la cantidad de dígitos deseada.

## Pasaje entre Bases en Potencia

Si quiero pasar entre dos bases que son potencias entre si, entonces busco $n$ tal que $b_1^n = b_2$. Por lo que necesito $n$ dígitos en base $b_1$ para representar un digito en base $b2$.

Para pasarlo, tomo el numero de a $n$ dígitos y los convierte individualmente. Si me faltan números, entonces agrego ceros.

$$
101101,10011_2 \to \text{Base } 16
$$

$$
\underbrace{\color{gray}{00}10}_{2}\underbrace{1101}_{D},\underbrace{1001}_{9}\underbrace{1\color{gray}{000}}_{8} = 2D,98_{16}
$$

Si quiero pasar hacia una base mas grande, cada digito de la base mayor la convierto en $n$ dígitos en la base menor

$$
2D,98_{16} \to \text{Base } 2
$$

$$
\underbrace{2}_{0010}\underbrace{D}_{1101},\underbrace{9}_{1001}\underbrace{8}_{1000} = 00101101,10011000
$$
