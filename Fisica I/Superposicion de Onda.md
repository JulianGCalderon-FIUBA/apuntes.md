---
title: Superposición de Onda
---

Las ondas son soluciones de ecuaciones diferenciales lineales, por lo que la suma algebraica de dos ondas sigue siendo una onda.

## Ondas Estacionarias

Las ondas estacionarias se generan cuando se superponen dos ondas de igual velocidad y frecuencia. Pero distinto sentido

$$
\begin{gathered}
\xi_1 = A\cdot\sin(kx-\omega t)\\
\xi_2 = A\cdot\sin(kx+\omega t)
\end{gathered}
$$

$$
\xi_{\text{tot}} = 2A\cdot\sin(kx)\cdot\cos(\omega t)
$$

El **nodo** es el punto donde la perturbación es nula. El **vientre** es el punto donde la perturbación puede ser máxima.

El modo de la onda $n$ determina la cantidad de vientres que tiene la onda. El primer modo se denomina onda estacionaria fundamental. Mientras que el segundo se denomina primer armónico.

### Cuerdas

#### Ambos Extremos Fijos

Si los extremos de la cuerda de longitud $L$ son fijos, entonces las ondas estacionarias solo se dan en ciertas frecuencias.

Como ambos extremos están fijos, entonces la perturbación en los extremos es nula.

$$
f_n = n\frac v{2L}
$$

$$
\lambda_n = \frac{2L}n
$$

$n=1,2,3,...$

#### Un Extremo Fijo

Si solo uno de los extremos está fijo, entonces ese extremo es un nodo, y el otro extremo es un vientre.

$$
f_n = (2n-1)\frac v{4L}
$$

$n=1,2,3,...$

### Tubos

#### Ambos Extremos Abiertos

En este caso, en los extremos la presión coincide con la presión atmosférica, por lo que son vientres. Debido a esto, el planteo es idéntico a la cuerda con extremos fijos.

Si se resuelve con ondas de desplazamiento, entonces en los extremos se encuentran los vientres. Para facilitar el cálculo, se usa $[\cos]$

$$
\xi_{\text{tot}} = 2A\cdot\cos(kx)\cdot\sin(\omega t)
$$

El planteo coincide con el de la cuerda con extremos fijos.

$$
f_n = n\frac v{2L}
$$

$$
\lambda_n = \frac{2L}n
$$

$n=1,2,3,...$

#### Un Extremo Abierto

Si cierro un extremo, entonces uno de los extremos es un nodo, y el otro es un vientre. Se resuelve como una cuerda con un extremo fijo.

Si planteo las ondas de desplazamiento, entonces en el primer extremo se encuentra un vientre, y en el otro un nodo. Para facilitar el cálculo, se usa $[\cos]$

El planteo coincide con el de la cuerda con un extremo fijo.

$$
f_n = (2n-1)\frac v{4L}
$$

$n=1,2,3,...$

### Resonancia

Si la frecuencia de la onda es la misma que la frecuencia natural de la caja de resonancia, entonces la amplitud del sonido aumenta considerablemente

## Batidos

Los batidos ocurren cuando dos ondas armónicas de igual amplitud, pero de frecuencias diferentes, se propagan en el mismo medio

$$
\begin{gathered}
\xi_1 = A\cdot\sin(kx-\omega_1 t+\varphi_1)\\
\xi_2 = A\cdot\sin(kx+\omega_2 t+\varphi_2)
\end{gathered}
$$

---

$$
\begin{align*}
\xi_{\text{tot}} = 2A
&\cdot\overbrace{
\cos\bigg(\frac{\Delta k}2x -\frac{\Delta\omega}2t+\frac{\Delta\varphi}2\bigg)}^\text{Amplitud Modulada}
\\
&\cdot
\cos\bigg(k_px-w_pt+\varphi_p\bigg)
\end{align*}
$$

---

$$
\omega_\text{Onda Moduladora} = \frac{w_2-w_1}2
$$

$$
f_\text{Onda Moduladora}  = \frac{f_2-f_1}2
$$

$$
f_\text{Pulso} = \big|f_2-f_1\big| 
$$
