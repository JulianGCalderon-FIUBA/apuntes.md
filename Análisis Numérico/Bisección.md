---
title: Bisección
---

La bisección es un método que permite encontrar las raíces de cualquier función continua, si conocemos un intervalo $[a,b]$ tal que $f(a), f(b)$ tengan signos opuestos.

Para esto, utilizamos el teorema de Bolzano

## Teorema

Sea $f \in \mathscr C[a,b]$ y $f(a)f(b) < 0$, Entonces el método de la bisección genera una sucesión $\{p_n\}_{n≥1}$ que aproxima a la raíz de $f$.

$$
\|p_n - p\| \leq \frac{b-a}{2^n} \quad\text{ con } n\geq1
$$

### Algoritmo

1. A partir de $a_1, b_1$, busco el punto medio $p_1$
2. Busco si el cambio de signo está en el intervalo $[a_1, p_1]$ o $[p_1, b_1]$
	1. Si $f(p_1) = 0$, encontré el punto.
	2. Si $f(a_1)f(p_1) < 0$, defino $a_2:= a_1, b_2:= p_1$
	3. Caso contrario, defino $a_2:= p_1, b_2:= b_1$
3. Repito el algoritmo a partir de $a_2, b_2$
4. Freno el algoritmo una vez hallada la precisión buscada (criterio de paro)

### Criterios de Paro

Se define la tolerancia $\varepsilon$ a partir de la cantidad de precisión que busco. Si quiero un error menor a $10^{-2}$, entonces debo usar una tolerancia de $\varepsilon = 10^{-2}$.

El mejor criterio de paro es el que involucra un error relativo $(2)$

$$
\|p_n - p_{n-1}\| < \varepsilon
$$

$$
\frac{\|p_n - p_{n-1}\|}{\|p_n\|} < \varepsilon
$$

$$
\|f(p_n)\| < \varepsilon
$$

### Iteraciones Necesarias

Podemos encontrar la cantidad de iteraciones necesarias para asegurarnos de alcanzar tolerancia específica.

Sabemos que el problema siempre divide el intervalo a la mitad, por lo que la cota de error máxima siempre se divide en dos a cada iteración. De esta forma, podemos plantear:

$$
\|P_n - P\| \leq \frac{b-a}{2^n} < \varepsilon
$$

$$
n > \frac{\log(b-a) - \log(\varepsilon)}{\log(2)}
$$

Ya que el número de iteraciones debe ser un número natural. Redondeo para arriba para encontrar el próximo natural.

La sucesión $p_n$ converge a $p$ con un radio de convergencia $O(1/2^n)$. Esto quiere decir, que

$$
p_n = p + O(1/2^n)
$$
