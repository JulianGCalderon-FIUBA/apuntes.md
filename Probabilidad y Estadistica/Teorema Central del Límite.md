Las sumas de algunas variables aleatorias independientes e idénticamente distribuidas, tienen distribuciones conocidas

1. Si $X_1, \cdots, X_n \stackrel{iid}{\sim} \text{Ber}(p) \implies \sum^n X_i \sim B(n, p)$
2. Si $X_1, \cdots, X_n \stackrel{iid}{\sim} \text{G}(p) \implies \sum^n X_i \sim \text{Pas}(n, p)$
3. Si $X_1, \cdots, X_n \stackrel{iid}{\sim} \mathcal E(\lambda) \implies \sum^n X_i \sim \Gamma(n, \lambda)$

Pero si las graficamos, encontramos que los gráficos se parecen a la gráfica de una distribución normal.

Además, si estandarizamos la función como si fuese una normal estándar, encontramos que el gráfico de distribución se parece mucho más a la de una campana de Gauss.

## Definición del Teorema

Sean $(X_n)_{n \geq 1}$ una sucesión de variables aleatorias independientes e idénticamente distribuidas con esperanza y varianza finita, entonces (bajo ciertas condiciones generales) se cumple que

$$
\frac{\sum^n X_i - n\mu}{\sqrt{n} \sigma} \stackrel{\text{}}{\implies Z} \sim \mathcal N(0, 1)
$$

La suma de las variables aleatorias, estandarizada, tiende a una distribución normal estándar

La utilización de esta aproximación depende de la distribución original. La puedo usar siempre, entendiendo que estoy trabajando con una aproximación

> [!note]
> El teorema sirve para variables tanto discretas como mixtas
