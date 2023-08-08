Una variable aleatoria $X$ tiene distribucion normal si su funcion de densidad toma la siguiente forma

$$
\frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

Proponemos la variable aleatoria $Z = \frac{X - \mu}{\sigma}$, entonces demostramos que si $X$ tiene distribucion normal, entonces $Z$ tiene distribucion normal estandar.

De esta forma, podemos transformar cualquier variable aleatoria normal en una estandar, a partir de la siguiente expresion

$$
F_X(x) = \Phi\Big(\frac{x - \mu}{\sigma}\Big)
$$

**Propiedad Interesante:**

Sea $X$ una variable aleatoria normal, entonces si buscamos la probabilidad de que se aleje en un desvio de su media, podemos utilizar la transformacion para encontrar una expresion simplificada

$$
P(\mu - a\sigma < x < \mu + a\sigma) = 2\Phi(a) - 1
$$

# Distribucion Normal Multivariada

Se dice que un vector aleatorio $X$ tiene distribucion normal multivariada de dimension $p$, de parametros $\mu \in \mathbb{R}^p$ y $\Sigma \in \mathbb{R}^{p \times p}$ (simetrica y definida positiva), entonces $X \sim \mathcal N(\mu, \Sigma)$, si su funcion de densidad esta dada por

$$
f_X(x) = \frac{1}{(2\pi)^{p/2} | \Sigma |^{1/2}} \exp[ -\frac 12 (x-\mu)^T \Sigma ^{-1}(x - \mu)]
$$

El vector $\mu$ esta conformado por todas las esperanzas de las variableas aleatorias $X_i$, mientras que $\Sigma$ es la matriz de covarianzas de $X$.

**Otra definicion puede ser:**

Se dice que $X$ es un vector aleatoria con distribucion normal multivariada si y solo si, $\forall t \in \mathbb{R}^p$ se  tiene que $t^T X$ es normal univariada, es decir, $t^T X \sim \mathcal N(t^T\mu, t^t Z t)$. Ademas, $X_1, \cdots X_p$ son independientes si $\Sigma$ es una matriz diagonal

## Propiedades

- Si $X \sim \mathcal N_p(0, \text{diag}(\lambda_1, \cdots, \lambda_p)$ entonces $X_i, \cdots, X_p$ son independientes y de distribucion $X_i \sim \mathcal N(0, \lambda_i)$
- Si $X \sim \mathcal N_p(\mu, \Sigma)$ y $A \in \mathbb{R}^{p \times p}$ no singular, entonces $Ax + b \sim \mathcal N_P(A\mu + b, A \Sigma A^t)$