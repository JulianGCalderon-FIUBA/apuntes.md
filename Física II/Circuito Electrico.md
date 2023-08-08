Red conductora que contiene al menos una trayectoria cerrada por la que puede fluir la carga eléctrica. Las cargas eléctricas se mueven por acción del campo eléctrico dentro del conductor. 

En un circuito cerrado, la corriente eléctrica es constante, estacionaria. Además, la diferencia de potencial en un circuito cerrado es nulo, debemos respetar esto para diseñar circuitos cerrados.

# Notación Circuital

Una llave es una porción del circuito que se puede abrir o cerrar, también se puede para conectar distintas ramas. (con llaves entre varios caminos distintos)

Los conductores ideales (cables) no tienen resistencia, en la practica este cable no existe.

![[Circuito Electrico 1.png|Untitled]]

![[Circuito Electrico 2.png|Untitled]]

 Para nosotros, los siguiente significan lo mismo. Fuentes de corriente continua

![[Circuito Electrico 3.png|Untitled]]

Un capacitor almacena cargas, energía. Hay varios tipos distintos. Se considera un capacitor variable si podemos modificar sus propiedades. El capacitor polarizado es mas barato pero solo permite que las cargas positivas estén de un lado, si esto no se cumple el capacitor se quema.

![[Circuito Electrico 4.png|Untitled]]

Las resistencias imponen una diferencia de potencial sobre el circuito. permite que los componentes no se quemen. La caída de potencial que causa la resistencia es negativa en el sentido positivo de la corriente.

![[Circuito Electrico 5.png|Untitled]]

# Leyes de Kirchhoff

**Nodos:** Los nodos son puntos donde convergen tres o mas conductores.

**Ramas:** Las ramas son porciones del circuito donde circula una única corriente. Para cada rama, hay una corriente. Una rama es cualquier camino que pueda tomar entre dos nodos.

Para cada rama, necesitamos una ecuación. Estas ecuaciones provienen de las mallas, y de los nodos.  v  Las ecuaciones no son linealmente independientes, por eso debemos usar tanto ecuaciones de malla como de nodo.

Las ecuaciones de nodo consisten en tomar un nodo y computar todas las corrientes que circulan por ese nodo. Si tenemos $n$ nodos, vamos a obtener $n{-}1$ ecuaciones independientes.

Las ecuaciones de malla consisten en tomar un camino cerrado y computar las caídas y subidas de potencial de la misma. Vamos a tomar la cantidad de ecuaciones de malla que necesitemos para completar el sistema de ecuaciones.

$$
\sum_{i=1}^n I_i = 0\\
\small\color{gray}\text{Ley de Nodo}
$$

$$
\sum_{i=1}^n V_i = 0\\
\small\color{gray}\text{Ley de malla}
$$

Esto es así ya que en el circuito no debe estar acumulando carga en ningún punto del circuito, y en un camino cerrado el trabajo es nulo.

# Conexión de Resistencias

## Serie

Si conectamos resistencias en serie, entonces entonces la corriente que pasa por cada una es la misma, pero la diferencia de potencial se divide. (el potencial total sigue siendo el mismo).

$$
R_{eq} = \sum_{i=1}^n R_i
$$

## Paralelo

Cuando las conectamos en paralelo, la corriente se divide pero la diferencia de potencial es la misma para cada camino.

$$
\frac{1}{R_{eq}} = \sum_{i=1}^n \frac{1}{R_i}
$$

# Potencia

Podemos definir la potencia como la variación de energía en función del tiempo.

$$
P = \frac{dU}{dt} = \frac{dq}{dt}\ \Delta V = I \cdot \Delta V
$$

**Donde se calcula la potencia?**

Las pilas tienen una corriente y un voltaje, por lo que entregan (o absorben) potencia, dependiendo del sentido de la corriente. 

Las resistencias por el otro lado, siempre tienen potencia negativa. Debido a esto, las resistencias siempre *disipan potencia*, pierden energía en forma de calor.

$$
P = \frac{\Delta V^2}{R} = I^2 R
$$

## Balance de Potencia

En un circuito cerrado, la potencia total del circuito deberá ser nula.

$$
P_{\text{entregada}} = P_{\text{abosrbida}} + P_{\text{disipada}}
$$

$$
\sum_{j = 1}^n I_j \cdot \mathcal{E}_i= \sum_{k = 1}^n I_k \cdot \mathcal{E}_j + \sum_{l = 1}^n I_l \cdot \mathcal{E}_l
$$