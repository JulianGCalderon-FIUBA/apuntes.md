# Tipos de funciones

- *Campo escalar:* es una función que asigna un número real $z$ a cada vector $(x_1, x_2, ..., x_n)$
    
    $$
    f(x_1, x_2, \dotsm,x_n) = z
    $$
    
- *Campo vectorial:* es una función que asigna, de manera univoca, un vector $(y_1, y_2, \dotsm, y_m)$ a cada punto $(x_1, x_2, ..., x_n)$

$$
f(x_1, x_2, \dotsm, x_n) = (y_1, y_2, \dotsm, y_m)
$$

- *Función vectorial:* es una función que asigna un vector $(y_1, y_2, \dotsm, y_m)$ a cada numero real $t$

$$
f(t) = (y_1, y_2, \dotsm, y_m)
$$

# Representación de campos escalares

Dado un campo escalar de $n$ variables $f(x_1, x_2, \dotsm, x_n)$, se le llama grafica al siguiente subconjunto de $\mathbb{R}^{n+1}$

$$
Gr(f) = \big\lbrace\vec x\in\mathbb{R}^{n+1} /x_{n+1} =(x_1,x_2,\dotsm,x_n)
,\,(x_1,x_2,\dotsm,x_n) \in D\big\rbrace
$$

Para $n≥3$, no hay representación grafica posible

## Conjuntos de nivel

Para cada valor real $k \in Im(f)$, se denomina *conjunto de nivel* $k$ de un campo escalar $f$ con dominio $D \subset\mathbb{R}^n$ al siguiente subconjunto del dominio de $f$

$$
L_k = \big\lbrace(x_1, x_2, \dotsm, x_n) \in D / f(x_1, x_2, \dotsm, x_n) = k\big\rbrace
$$

Para *campos escalares* de dos variables los conjuntos de nivel son, en general, curvas en el plano.

$$
L_k = \big\lbrace(x,y) \in D/f(x,y) = k\big\rbrace
$$

![[Funciones de varias variables 1.png|Funciones%20de%20varias%20variables%20638fe43ddf1c410c85b7a1b7727a3ce2/Untitled.png]]

# Representación de campos vectoriales

Para *campos vectoriales* de $R^2$ en $R^2$ y $R^3$ en $R^3$, se suele graficar con origen en cada punto del dominio, un vector flecha que represente el valor vectorial del campo en ese punto

![[Funciones de varias variables 2.png|Funciones%20de%20varias%20variables%20638fe43ddf1c410c85b7a1b7727a3ce2/Untitled%201.png]]

# Representación de funciones vectoriales

Las funciones vectoriales, con dominio en $R$ e imagen en $R^n$, admiten una representación para los casos en que $n=2$ y $y=3$. En estos casos se acostumbra representar el recorrido o imagen de la función, en el plano o en el espacio, según corresponda

$$
\vec f(t) = (t,t^2)
$$

![[Funciones de varias variables 3.png|Funciones%20de%20varias%20variables%20638fe43ddf1c410c85b7a1b7727a3ce2/Untitled%202.png]]