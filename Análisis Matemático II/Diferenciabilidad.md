Sea $f:D\subset\mathbb{R}^n\to\mathbb{R}^m,A\in D^º$, se dice que $f$ es diferenciable en $\vec x_0$ si:

$$
\lim_{\vec x\to\vec x_0}\frac{f(\vec x) - \overbrace{\Big[f(\vec x_0) + \nabla f(\vec x_0)(\vec x-\vec x_0)\Big]}^z}{\|\vec x - \vec x_0\|} = 0
$$

## Teoremas

**Teorema 1:**

Si $f$ es diferenciable en $A$, entonces es continua en $A$

**Teorema 2:**

Si $f$ es diferenciable en $A$, entonces es derivable en toda direccion en $A$

**Teorema 3:**

Si $f:D\subset R^2 \to R$ es diferenciable en $\vec A$, entonces: $f'(\vec A,\vec v) = f'_x(\vec A)\cdot\vec v_x + f'_y(\vec A) \cdot \vec v_y$

**Teorema 4:**

Si $f$ tiene derivadas parciales continuas en $A$, entonces es diferenciable

$$
f \in C^1(A),\quad f\text{ es }C1 \text{ en }A
$$

**Definicion:**

Si $f:D\subset R^2 \to R$ es diferenciable en $x_0, y_0$ solo si:

$$
\lim_{(x,y)\to(x_0, y_0)}\frac{f(x,y) - \overbrace{\Big[f(x_0, y_0)+f_x'(x_0,y_0)(x-x_0) + f_y'(x_0,y_0)(y-y_0)\Big]}^z}{\sqrt{(x-x_0)^2 + (y-y_0)^2}}
$$

Ver tabla de diferencabilidad en: [[Diferenciabilidad 1.pdf]]

## Plano tangente

Sea $f: D\subset\mathbb{R}^2 \to\mathbb{R}$ diferenciable en $A = (x_0, y_0)$, se llama plano tangente a la grafica de $f$ en el punto $(x_0,y_0,f(x_0,y_0))$ al plano de ecuacion:

$$
z = f(x_0, y_0)+f_x'(x_0,y_0)(x-x_0) + f_y'(x_0,y_0)(y-y_0)
$$

## Campos Vectoriales

$$
\lim_{\vec x\to\vec x_0}\frac{\vec f(\vec x) - \overbrace{\Big[\vec f(\vec x_0) + J_f(\vec x_0)(\vec x-\vec x_0)^t\Big]}^z}{\|\vec x - \vec x_0\|} = 0
$$
