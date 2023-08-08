Los capacitores están formados por dos conductores, de cargas opuestas e igual modulo. Entre estos capacitores podemos dibujar un campo eléctrico, que nace en las cargas positivas, y muere en las cargas negativas. Este capacitor tiene la capacidad de almacenar energía.

Para cargar ambos conductores con cargas opuestas, utilizamos una pila. La pila mueve cargas de un capacitor al otro. La pila tiene asociada una diferencia de potencial $\Delta V$, la cual que permite mover las cargas, hasta que entre los dos conductores haya la misma diferencia de potencial que entre los bornes de la pila. 

![[Apuntes/Física II/Attachments/Capacitores 1.png|Untitled]]

La carga final del capacitor resulta proporcional a la diferencia de potencial de la pila, siendo $C$ la capacidad del capacitor. La unidad de la capacidad es el **Faradio** $[F] = C/V$

$$
Q = C \cdot \Delta V
$$

La energía almacenada va a ser igual al trabajo que me cuesta cargar este capacitor.

$$
W = \int dw = \int_0^Q \frac{q}{C}\cdot dq = \frac{Q^2}{2C}
$$

$$
U_{almacenada} = \frac 12\cdot C\Delta V^2 = \frac 12 \cdot Q\Delta V 
$$

# Capacidad de Capacitor

La capacidad de un capacitor esta relacionado con la geometría y el medio de los conductores

$$
C = \varepsilon_0\varepsilon_r \cdot \frac{A}{d}
$$

Siendo $A$ el area de la placa del capacitor, y $d$ la distancia entre las placas.

En el caso de un capacitor cilíndrico, la capacidad equivale a

$$
C = \varepsilon_0\varepsilon_r \cdot\frac{2\pi L }{\ln(b/a)}
$$

Siendo $L$ la longitud del cilindro, $a$ el radio menor, y $b$ el radio mayor

En el caso de un capacitor esférico, la capacidad equivale a

$$
C = \epsilon_0\epsilon_r \cdot \frac{ab}{b-a}
$$

# Conexión de Capacitores

Vamos a trabajar con capacitores inicialmente descargados

## Serie

Los capacitores en serie están uno a continuación del otro, podemos relacionar la capacidad de los capacitores de la siguiente manera:

$$
\frac 1{C_{eq}} = \frac 1{C_1} + \frac 1{C_2}
$$

## Paralelo

Tambien podemos conectar los capacitores en paralelo, podemos relacionar la capacidad de los capacitores de la siguiente manera:

$$
C_{eq} = C_1 + C_2
$$

# Mallas e Islas

Cuando las conexiones son mas complejas que en los casos vistos anteriormente, podemos utilizar este método para resolver el problema

**Malla:** Camino cerrado de forma que la diferencia de potencial sea nula.

**Isla:** Porción aislada donde la carga se conserva.

Utilizando estos conceptos, podemos encontrar la ecuaciones que necesitemos para completar el sistema de ecuaciones.