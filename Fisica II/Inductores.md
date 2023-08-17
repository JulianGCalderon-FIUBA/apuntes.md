Los inductores son bobinados, alrededor de un cierto material magnético $(\mu_r)$. Este bobinado tendrá un coeficiente de autoinducción $L_1$, una corriente $I_1$, y un número de vueltas o espiras $N$ y una longitud $l_1$

Este bobinado generará un campo de inducción magnética $\vec B$, dentro del material magnético, en sentido del mismo.

$$
B = \frac{\mu_0\mu_r\cdot N_1 \cdot I_1}{l_1}
$$

$$
\varphi_{11} = \frac{\mu_0\mu_r \cdot N_1\cdot S_1}{l_1}
$$

$$
L = \frac{\mu_0 \mu_r\cdot N_1^2 \cdot S_1}{l_1}
$$

## Bobinado Interno

Si en el interior del inductor, insertamos un bobinado dentro, podremos calcular el coeficiente de inductancia mutua.

$$
\varphi_{21} = \frac{\mu_0\mu_r \cdot N_1\cdot S_2}{l_1}
$$

$$
M_{21} = \frac{\mu_0 \mu_r\cdot  N_1 N_2 \cdot S_2}{l_1}
$$

## Acoplamiento Magnético

### Notación Circuital

Los puntos rojos (bornes homólogos) indican el sentido de la corriente, si los bornes están del mismo lado, los campos que genera cada inductor son aditivos.

Las dos líneas paralelas del medio, indican que ambos inductores están sobre un mismo material magnético

![[Inductores 1.png|300]]

Si yo quiero calcular la diferencia de potencial de esos inductores, debo calcular:

$$
\mathcal E_1 = \mathcal E_{11} +\mathcal E_{12}  = -L_1 \cdot \frac{di_1}{dt} - M_{12} \cdot \frac{di_2}{dt}
$$

Si los bornes no son homólogos, entonces se debe restar:

$$
\mathcal E_1 = \mathcal E_{11} -\mathcal E_{12}  = -L_1 \cdot \frac{di_1}{dt} + M_{12} \cdot \frac{di_2}{dt}
$$

## Conexión de Inductores en Serie

Cuando colocamos inductancias en serie, la corriente es la misma.

Si los bornes homólogos están del mismo lado del inductor, los flujos son aditivos. En el caso contrario, son sustractivo

$$
L_{eq} = L_1 + L_2 \color{Red}{\pm} 2M
$$

El signo de $\pm$ varía si los bornes son homólogos $(+)$ o no homólogos $(-)$

## Energía en Inductores

Son componentes, capaces de almacenar energía. Esta energía será el trabajo que me cueste **energizar** ese inductor.

$$
U = W = \int_0^t P(t) \cdot dt = \int_0^I i(t)\cdot L \cdot di
$$

$$
U = \frac 12 \cdot L \cdot I^2
$$

> [!note]
> Si los inductores están conectados en serie, puedo remplazar el coeficiente de autoinductancia $L$ por el equivalente.

### Acoplamiento Magnético

Si los inductores están en acoplamiento magnético. Vamos a dividir la carga de energía en dos, para simplificar el cálculo.

Primero hacemos circular una corriente por el circuito uno hasta que $t_1$, que esta corriente sea estacionaria. Una vez que esta corriente es estacionaria, hacemos circular corriente por el circuito dos. Hasta un $t_2$, donde se vuelve estacionaria.

$$
U_1 = \int_0^{t_1} P(t)\cdot dt = \frac 12 \cdot L_1 \cdot I_1^2
$$

$$
U_2 = \int_{t_1}^{t_2} P(t)\cdot dt = M\cdot I_1 I_2 + \frac 12 \cdot L_2 \cdot I_2^2
$$

$$
U_T = U_1 + U_2 = \frac 12 L_1 I_1^2 + \frac 12 L_2 I_2^2\ \color{Red}{\pm}\  MI_1 I_2
$$

El signo de $\pm$ varía si los bornes son homólogos $(+)$ o no homólogos $(-)$

## Transformador Ideal

Compuesto por un toroide de un cierto material magnético. Alrededor del toroide tiene envuelto dos solenoides de $N_1, N_2$ espiras. Podemos encontrar una relación entre el número de espiras entre $N_1$ y $N_2$, para lograr transformar el voltaje desde $\varepsilon_1$ a $\varepsilon_2$

![[Inductores 2.png|375]]

$$
\frac{\varepsilon_1}{\varepsilon_2} = \frac{N_1}{N_2}
$$
