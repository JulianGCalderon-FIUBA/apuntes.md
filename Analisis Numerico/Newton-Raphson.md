---
title: Newton-Raphson
---

Este método es una de las técnicas numéricas más poderosas de la búsqueda de raíces. Sin embargo, este método requiere de una buena raíz, ya que no converge para todo valor inicial.

Para este método, se realiza una aproximación lineal de la función a analizar y se busca la raíz de dicha aproximación. Si el punto inicial es suficientemente cercano a la raíz, entonces el método converge.

Para encontrar el método, partimos de la aproximación de Taylor de orden dos, ignorando/despreciando el término del error. Luego remplazamos $f(p) = 0$ para obtener la sucesión.

$$
f(x)=f(\overline x)+(x-\overline x)f'(\overline x) + \frac{(x-\overline x)^2}{2}f''(\overline x)
$$

Sea $f \in \mathscr C^2[a,b]$ y $\overline x \in [a.b]$ una aproximación de $p$ tal que $f'(x) \neq 0$ y $\|p-\overline x\|$ suficientemente pequeño. Entonces la sucesión $p_n$ converge a la raíz.

$$
p_n = p_{n-1} - \frac{f(p_{n-1})}{f'(p_{n-1})} \quad \forall n \geq 1
$$

## Teorema

Sea $f \in \mathscr C^2[a,b]$. Si $p \in [a,b]$ tal que $f(p) = 0$ y $f’(p) \neq 0$ entonces $\exists\delta > 0$ tal que el método de Newton genera una sucesión $\{p_n\}_{n\geq 1}$ que converge a $p$ para cualquier aproximación inicial $p_0 \in [p-\delta, p+\delta]$

Este método converge y diverge rápidamente, por lo que es fácil darse cuenta si elegimos una mala semilla.

## Método de la Secante

Si queremos evitar evaluar la derivada en el método de Newton, podemos hallar una equivalencia a partir de

$$
f'(p) = \lim\limits_{x \to p} \frac{f(x) - f(p)}{x - p}
$$

Podemos aproximar la derivada de la siguiente forma

$$
f'(p_{n-1}) \approx \frac{f(p_{n-2}) - f(p_{n-1})}{p_{n-2} - p_{n-1}}
$$

$$
p_n = p_{n-1} - \frac{f(p_{n-1})(p_{n-1}-p_{n-2})}{f(p_{n-1})-f(p_{n-2})}
$$

El método de la ventaja permite que no debamos calcular la derivada, y tiene mejores rendimientos que los métodos lineales. Sin embargo, se necesitan dos semillas y se pierde la convergencia cuadrática.

## Raíces Múltiples

Una solución $p$ de $f(x) = 0$ es un cero de multiplicidad $m$ de $f$ si para todo $x \neq p$, se cumple que

$$
f(x) = (x-p)^m q(x)\quad/\quad \lim_{x\to p}q(x) \neq 0
$$

**Teorema:** La función $f$ tiene un cero simple en $p$ si $f(p) = 0$ y $f’(p) \neq 0$

**Teorema:** La función $f$ tiene un cero de multiplicidad $m$ en $p$ si $0 =f(p) = f'(p) = \cdots = f^{(m-1)}(p)$ y $f^{(m)}(p) \neq 0$

### Modificación del Método para Raíces Múltiples

Si $f(x)$ tiene raíces múltiples, entonces para encontrar esas raíces manteniendo la convergencia cuadrática, planteo la función iterativa como

$$
g(x) = x - \frac{u(x)}{u'(x)} \iff u(x) = \frac{f(x)}{f’(x)}
$$

De esta forma, nos aseguramos que la función $u$ no tenga raíces múltiples, pero que $p$ sea un cero de $u$.

Definimos la sucesión de Newton-Raphson modificado como

$$

\boxed{p_{n+1}=p_n-\frac{f(p_n)f'(p_n)}{[f'(p_n)]^2-f(p_n)f''(p_n)}}
$$
