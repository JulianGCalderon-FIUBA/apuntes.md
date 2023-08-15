## Ecuaciones Diferenciales Ordinarias

La incógnita es una función de una sola variable, las derivadas que aparecen son ordinarias (no parciales)

$$
F(x,y,y',\cdots,y^{(n)}) = 0
$$

El **orden** de una EDO, es el orden de derivación más alto que aparece en la ecuación.

### Diferenciales

Existen dos notaciones utilizadas para los diferenciales:

$$
dy = y'dx,\quad\text{Newton}
$$

$$
\frac{dy}{dx} = y' ,\quad \text{Leibniz}
$$

### Resolver la EDO

Una **solución general** se contiene dos constantes de integración arbitrarias (es una familia de soluciones)

Una **solución particular** se obtiene dando valores a las constantes de integración a partir de las condiciones iniciales

Una **solución singular** es una solución que verifica la ecuación, pero no pertenece a la solución general

> Vamos a estudiar ecuaciones diferenciales de primer orden

## Existencia y Unicidad

$$
\text{PVI }\begin{cases}y' = f(x,y)\\f(x_0) = y_0\end{cases}
$$

$$
(x_0,y_0) \in [a,b]\times[c,d]
$$

Si $f$ y $f'_y$ continua en $(a,b)\times(c,d)$, entonces existe $I \subset (a,b)$ que contiene a $x_0$ / existe una solución $y = y(x)$, y es única en $I$.
