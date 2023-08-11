Faraday notó, luego de unos experimentos, que un campo magnético puede generar corriente en un circuito cercano. Sin embargo, esta corriente es temporal. Solo surge cuando el campo no es estacionario, sino que depende del tiempo. A esta corriente, se la denomina **corriente inducida**.

## Ley de Faraday-Lenz

$$
\mathcal{E} = -\frac{d\phi}{dt}
$$

Esta ley, también conocida como regla de flujo, propone que la variación del flujo de un campo magnético genera una potencial en un circuito cercano. Este potencial va a generar la corriente mencionada.

La corriente inducida va a generar un campo magnético, que va a contrarrestar la variación de flujo del campo magnético inicial.

### Variación de Flujo

Las variaciones de flujo ocurren tanto cuando:

- La corriente no es estacionaria. $i(t) \to B(t)$
- La superficie del flujo varía. $S(t)$
- Modificando la posición relativa entre los vectores $(\vec B \cdot d\vec S)$

### Ley de Maxwell-Faraday

Si desarrollamos la expresión anterior y la relacionamos con la circulación del campo eléctrico, llegamos a la primera definición que vincula el campo eléctrico con el campo magnético.

$$
\vec\nabla\times\vec E = -\frac{\delta\vec B}{\delta t}
$$

## Coeficiente de Inducción Mutuo

Tenemos un circuito, con una corriente que depende del tiempo, generando un campo magnético. Por el otro lado, otro circuito inicialmente sin corriente.

Ambos circuitos tienen un número $N_1, N_2$ de espiras.

Si calculamos el potencial inducido sobre el segundo circuito por el campo magnético generador por el primero, llegamos a la siguiente expresión.

$$
\mathcal E_{21} = -N_2 \cdot \frac{d\phi_{21}}{dt} = -N_2 \cdot \frac{d\varphi_{21}}{di_1} \frac{di_1}{dt} = -M_{21} \cdot \frac{di_1}{dt}
$$

Podemos entonces agrupar los parámetros en un coeficiente de inducción mutuo, simplificando la ecuación.

$$
M_{21} =N_2 \cdot \frac{d\varphi_{21}}{di_1} 
$$

Si ahora calculamos el flujo de este nuevo campo magnético sobre el circuito inicial, llegamos a un resultado completamente análogo. En medios lineales se cumple que:

$$
M_{12} = M_{21} =M
$$

### Medios Lineales

Como trabajamos con medios lineales, la relación del flujo con respecto a la corriente es lineal. Entonces, simplificamos:

$$
\frac{d\phi}{di} = \frac{\phi}{i}
$$

## Coeficiente de Autoinducción

También podemos calcular el flujo sobre un circuito del campo magnético generador por el mismo.

$$
\mathcal E = -N_1 \cdot \frac{d\phi_{11}}{dt} = -N_1 \cdot \frac{d\phi_{11}}{di_1} \frac{di_1}{dt} =-L_1 \cdot \frac{di_1}{dt}
$$

Definimos entonces el coeficiente de autoinducción

$$
L_1 = N_1 \cdot \frac{d\phi_{11}}{di_1} 
$$

## Relación entre Coeficientes

Podemos definir un factor de acoplamiento $k$, que varía entre $0$ y $1$, Y relaciona los coeficientes de autoinductancia con los coeficientes de inductancia mutua

$$
M = k \sqrt{L_1 \cdot L_2}
$$

- Si $k = 0$, decimos que los circuitos están **desacoplados**
- Si $k = 1$, decimos que los circuitos están en **acoplamiento perfecto**
