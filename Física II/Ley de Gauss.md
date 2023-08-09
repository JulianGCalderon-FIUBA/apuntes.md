$$
\underbrace{\oint_S \vec F\cdot d\vec S = \int_V \nabla\cdot\vec F \cdot d\vec V}_\text{Teorema de Gauss}
$$

El teorema de Gauss solo nos permite calcular módulos, no podemos encontrar la dirección del campo. Esa la tenemos que razonar por nuestra cuenta

## Enunciado

La ley de Gauss tiene dos formas, la forma integral y la forma diferencial. Ambas relacionan el campo eléctrico con la carga encerrada, o con la densidad de carga

$$
\text{Forma Integral}:\phi = {\subset\!\supset} \llap{\iint} \vec Ed\vec s = \frac{Q_\text{enc}}{\varepsilon_0}
$$

$$
\text{Forma Diferencial}:\nabla\cdot\vec E = \frac{\rho}{\varepsilon_0}
$$

### Carga Puntual

Si analizamos el flujo a través de una superficie cerrada de una carga puntual en su interior, llegamos a la siguiente expresión:

$$
\phi = {\subset\!\supset} \llap{\iint}_S \vec E\cdot d\vec s = {\subset\!\supset} \llap{\iint} \frac{kq}{r^2}\cdot\hat r \cdot r^2\sin\theta\cdot d\theta d\phi\cdot \hat r
$$

$$
\phi = kq{\subset\!\supset} \llap{\iint}_S ds = kq\cdot 4\pi \implies \varphi =\frac{Q}{\varepsilon_0}
$$

> [!note]
> Podemos demostrar a través del teorema de gauss que el flujo es independiente de la superficie.

### Multiples Cargas

Para el caso de multiples cargas, el flujo es proporcional a la suma de las cargas individuales dentro de la superficie. Esto se debe a que las operaciones que se aplican son lineales. Se pueden distribuir

$$
\phi = {\subset\!\supset} \llap{\iint}_S \vec E\cdot d\vec s = {\subset\!\supset} \llap{\iint}_S \sum_i\vec E_i\cdot d\vec s = \sum_i{\subset\!\supset} \llap{\iint}_S \vec E_i\cdot d\vec s
$$

$$
\phi = \frac{\sum Q}{\varepsilon_0}
$$

> [!note]
> Para el calculo del flujo, solo se tienen en cuenta las cargas dentro de la superficie cerrada. En cambio, el campo eléctrico en un punto depende de **todas** las cargas

### Distribución Continua

El teorema de gauss para distribución distribución continua de cargas permite analizar el flujo de ciertos casos de forma mucha mas practica

#### ¿Como calcular el campo eléctrico?

- Buscamos la dirección y sentido de $\vec E$
- Analizamos la dependencia de $\vec E$
- Elegimos una superficie cerrada $S$ acorde
- Calculamos $\iint ds$, $Q_\text{enc}$

De esta forma podemos despejar el modulo del campo eléctrico, y agregamos la dirección manualmente
