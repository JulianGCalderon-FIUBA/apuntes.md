## Teorema del Punto Fijo

Una función $G: D \subset \mathbb{R}^n \to \mathbb{R}^n$ tiene un punto fijo en $\overline p \in D$ si $G(\overline p) = \overline p$

1. Sea $G$ continua en $D$, entonces si $G(\overline x) \in D,\quad \forall x \in D$, entonces $G$ tiene punto fijo en $D$
2. Si $\exists 0 < k < 1$ talque $\|\frac{\partial g_i(\overline x)}{\partial x_j}\| \leq \frac Kn, \quad \forall \overline x \in D$, entonces el punto fijo de $G$ es unico en $D$

Entonces la sucesión definida como:

$$
x^{(k)} = G(x^{(k-1)})\quad\forall k \geq 1
$$

Converge al único punto fijo $p \in D$, ademas podemos encontrar el minimo de iteraciones necesarias a partir de:

$$
\|x^{k} - p\|_\infty \geq \frac{K^k}{1-K} \|x^{(1)} - x^{(0)}\|_\infty
$$

> [!note]
> Este metodo converge para cualquier semilla perteneciente a $D$.

## Newton-Raphson

En el caso $n$-dimensional, el metodo Newton Raphson se resuelve a partir de dividir por la matriz Jacobiana

$$
G(x) = x - A^{-1}(x)F(x)
$$

Donde $A(x) = J(x)$, por lo tanto, la sucesión del punto fijo puede ser definida como

$$
x^{(k)} = x^{(k-1)} - J_F^{-1}(x^{(k-1)})F(x^{(k-1)})
$$

Sin embargo, no se calcula la inversa de la Jacobiana en cada iteracion, por lo que se resuelve el sistema de la siguiente forma

$$
J_F(x^{(k-1)}) y^{(k-1)} = -F(x^{(k-1)})
$$

$$
x^{(k)} = \overline x^{(k-1)} + \overline y^{(k-1)}
$$

> [!note]
> Este metodo tiene convergencia cuadratica, al igual que para una sola variable.

## Métodos Cuasi Newton

Consisten en aproximar la matriz Jacobiana con cada iteracion mediante fórmulas de recurrencia.

Podemos definir una sucesión de $A$ a partir de la Jacobiana inicial:

$$
A_k =A_{k-1} + \frac{(y_{k-1} - A_{k-1}s_{k-1})s^T_{k-1}}{s^T_{k-1} s_{k-1}}
$$

Definiendo:

- $y_k = f(x_k) - f(x_{k-1})$
- $s_{k-1} = x_k - x_{k-1}$

De esta forma, los metodos de Cuasi-Newton necesitan el calculo de una sola Jacobiana

## Método del Descenso Más Rápido

Coverge solo linealmente a la función, pero siempre converge. La idea consiste en partir de cualquier semilla, evaluar la función, y movernos en la direccion del maximo descenso, es decir, en la direccion inversa al gradiente.

Primero, definimos $G$ como $G(\vec x) = \sum_i^n f_i(\vec x)^2$

1. Evaluar $g$ en una aproximacion inicial $x^{(0)}$
2. Determinar una direccion en $x^{(0)}$ que origine una disminución del valor de $G$
3. Desplazar una cantidad $\alpha$ apropiada en esa direccion y llamar al nuevo punto $x^{(1)}$
4. Repetir los pasos hasta encontrar una aproximacion deseada.

De esta forma, encontramos una sucesión que converge para toda semilla inicial a la solución del sistema, para alguna constante $\alpha > 0$.

$$
x^{(k)} = x^{(k-1)} - \alpha \nabla_G(x^{(k-1)})
$$

Para hallar nuestra constante, buscamos el valor $\alpha$ que minimice la funcion $F$ en nuestro nuevo punto

Como hallar este minimo es muy costoso, definimos $h(\alpha)$ como un polinomio de grado 2.

Primero definimos los coeficientes

$$
\alpha_1 = 0
$$

$$
\alpha_3 \ /\  h(\alpha_3)< h(\alpha_1)
$$

$$
\alpha_2 = \frac{\alpha_3}{2}
$$

Luego, buscamos un polinomio $h^*(\alpha)$ de grado $2$ que interpole los puntos

$$
\{(\alpha_1, h(\alpha_1)), (\alpha_2, h(\alpha_2)),(\alpha_3, h(\alpha_3))\}
$$

Una vez construido este polinomio, encontramos $\alpha$ que minimice $h(\alpha)$ en el intervalo $(\alpha_1, \alpha_3)$

Para hallar el gradiente, nos conviene usar la forma matricial, vale que:

$$
\nabla_G(\vec x) = 2 J_F^T(\vec x) F(\vec x)
$$
