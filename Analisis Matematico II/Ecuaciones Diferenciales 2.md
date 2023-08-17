## Diferencial Exacto

Si la EDO no es de variables separables, entonces puedo tratar de escribir la ecuación de la forma

$$
f_1(x,y)dx +f_2(x,y)dy = 0
$$

Si encuentro una función $\varphi(x,y)$ cuyas derivadas parciales sean las funciones $f,g$. Entonces puedo igualar $0$ al diferencial de $\varphi$. Siendo esta una función constante

$$
d\varphi = \varphi'_xdx + \varphi'_ydy = 0
$$

la solución de la ecuación diferencial son los puntos $(x,y)$ que verifican la igualdad $\varphi = k$

Para verificar si existe la función $\varphi$, basta con verificar que el campo $f$ sea conservativo

$$
f(x,y) = \Big(f_1,\,f_2\Big) = \Big(\varphi'_x,\,\varphi'_y\Big)
$$

> [!note]
> Un campo es conservativo si las derivadas segundas cruzadas de su función potencial son iguales, y el dominio es un conjunto simplemente conexo. $f'_{1y} = f'_{2x}\to\varphi''_{xy} = \varphi''_{yx}$

### Factor Integrante

Cuando la función potencial $\varphi$ no existe. Podemos multiplicar la ecuación por un factor integrante para convertirla en un diferencial exacto.

$$
\underbrace{f_1 \cdot \mu}_{F_1}\cdot dx + \underbrace{f_2 \cdot \mu}_{F_2}\cdot dy = 0
$$

Para encontrar $\mu$, buscamos las diferencias entre las derivadas cruzadas y las dividimos por $f_1$ o $f_2$. Si alguno de estos dos cocientes da una función $g$ dependiente de una sola variable, entonces el método puede funcionar. La función $\mu$ depende únicamente de la misma variable que $g$

$$
\frac{f'_{1y} - f'_{2x}}{f_1} = g
$$

$$
\frac{f'_{1y} - f'_{2x}}{f_2} = g
$$

Si se cumple esta condición, entonces buscamos un $\mu$ que fuerce la ecuación diferencial a ser un diferencial exacto.

Igualamos las derivadas cruzadas de la nueva función $F$ y resolvemos para el factor integrante $\mu$

$$
F_{1y} = F_{2x}
$$

Ahora que tenemos $\mu$, resolvemos la nueva ecuación diferencial con el método del diferencial exacto, buscando la función potencial $\varphi$

$$
\big(\varphi'_x,\,\varphi'_y\big) = \big(F_1,\,F_2\big)
$$
