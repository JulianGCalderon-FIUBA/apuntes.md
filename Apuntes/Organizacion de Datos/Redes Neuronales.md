Es un algoritmo de aprendizaje que busca simular la inteligencia humana. Para ello, se basa en ***neuronas***.

Una neurona simple, tiene una serie de entradas. Estas se multiplican por unos pesos correspondientes, luego se suma y el resultado es pasado a una función de activación, la cual determina un resultado

![[Apuntes/Organizacion de Datos/Attachments/Redes Neuronales 1.png|Untitled]]

# Perceptrón Simple

Su función de activación es un escalón, función simple que vale cero o uno. Se le puede introducir un sesgo $b$, para evitar el sobre modelado.

En la primera iteración, se utilizan pesos aleatorios y se calcula el error obtenido. Luego se mueven los pesos en la dirección que se minimiza el error. Se utiliza la función del error

![[Apuntes/Organizacion de Datos/Attachments/Redes Neuronales 2.png|Gráfico de la función escalón]]

Gráfico de la función escalón

$$
w_1 = w_1 + \alpha + E
$$

$$
w_0 = w_0 + \alpha + E
$$

El perceptrón en definitiva, crea una línea que corta el plano, esto permite generar compuertas logicas (solo las linealmente separables)

# Perceptrón Multicapa

Para los problemas que no son linealmente separables, podemos utilizar múltiples capas para generar redes más complejas

![[Apuntes/Organizacion de Datos/Attachments/Redes Neuronales 3.png|Ejemplo de perceptrón multicapa]]

Ejemplo de perceptrón multicapa

![[Apuntes/Organizacion de Datos/Attachments/Redes Neuronales 4.png|Separación del plano de forma compleja]]

Separación del plano de forma compleja

# Redes SOM

*Mappean* un espacio de entrada en un espacio de salida, para hacerlo se utiliza una matriz de pesos. Cada entrada, está conectada con cada nodo de salida.

Se calcula la distancia euclidiana de cada nodo, gana la neurona con la menor distancia.

Cuando una neurona gana, actualiza los pesos de todas las neuronas dentro de un radio.

Estos radios disminuyen hasta que no se realicen cambios. Al final, se generan vecindarios

![[Apuntes/Organizacion de Datos/Attachments/Redes Neuronales 5.png|Untitled]]

![[Apuntes/Organizacion de Datos/Attachments/Redes Neuronales 6.png|Untitled]]

![[Apuntes/Organizacion de Datos/Attachments/Redes Neuronales 7.png|Untitled]]

# Backpropagation

Mejor algoritmo para entrenar redes neuronales. Partimos de un perceptrón multicapa con cada nodo está conectado con todos sus nodos siguientes.

Los nodos, solo se conectan con los nodos siguientes.

Pueden tanto aumentar como disminuir la cantidad de nodos en cada capa.

![[Apuntes/Organizacion de Datos/Attachments/Redes Neuronales 8.png|Untitled]]

La función de activación de este método es la función sigma

$$
f(x) = \frac{1}{1+e^{-x}}
$$

En la primera iteración, se calculan los resultados con pesos aleatorios. Desde la primer capa hasta la última.

Calculamos el error cuadrático medio de las salidas

$$
E =  \sum \frac 12 (\text{target} - \text{output})^2
$$

Ahora aplicamos el algoritmo, de backpropagation. Es una técnica de ascenso por el gradiente.

$$
\nabla E = \bigg(\frac{\partial E}{\partial w_1}, \frac{\partial E}{\partial w_2}, \frac{\partial E}{\partial w_3} \cdots, \frac{\partial E}{\partial w_n}\bigg)
$$

Para cada derivada parcial, utilizamos la regla de la cadena. Luego movemos los pesos en la dirección que minimice el error.

# Funciones de Activación

Hay distintas funciones de activación dependiendo de nuestro problema:

- Regresión: Sigmoidea, Lineal, Relu, ETC
- Clasificación de clases excluyentes: Sigmoidea
- Clasificación de clases simultáneas: Softmax, función exponencial normalizada. Se utiliza como función de activación de la capa de salida en modelos de calcificación, interpretandola como *scoring*.

![[Apuntes/Organizacion de Datos/Attachments/Redes Neuronales 9.png|Untitled]]

# Métodos de Regularización

Son métodos para prevenir el sobre modelado, a veces no son necesarios.

- Regularización L1 y L2: Penalizan el valor de los pesos de la red, evite que se le dé  más importancia a una característica que a otra. L1 es proporcional al módulo de los pesos, L2 es proporcional al cuadrado.
- Dropout: Apaga activaciones aleatoriamente durante el entrenamiento, esto hace que el resultado no dependa de unas pocas neuronas
- Early Stopping: Frena el modelo antes de que el error del set de validación empieza a aumentar.
- Data Augmentation: Generar más datos de prueba, a partir de los datos existentes. Aplicando transformaciones, especialmente útil para las imágenes.

# Optimizadores

Es una implementación concreta del algoritmo de backpropagation.

- SGD: Stochastic Gradient Descent, algoritmo clásico.
- Momentum: El gradiente se utiliza para la aceleración, y no para la velocidad. Utilizamos un hiper parámetro momentum que indica la fricción.
- Nesterov: En lugar de calcular el gradiente del error en el punto actual, lo calcula en la dirección del momento, avanzando un poco.
- AdaGrad: El error descenderá por la dimensión con la pendiente más empinada, esto no necesariamente al que conduzca al mínimo global. Tiene un buen desempeño para problemas cuadráticos simples. Pero a menuda se detiene demasiado pronto en redes profundas.
- RMSProp: Soluciona el problema de AdaGrad al ir olvidando las pendientes anteriores, a medida que avanza. SOlo acumula los gradientes de las iteraciones recientes. Tendremos un hiper parámetro $\beta$, tasa de decaimiento.
- Adam (Adaptive Moment Estimation): Combina ideas anteriores de Momentum y RMSProp. haciendo un seguimiento de una media de decaimiento exponencial de gradientes pasados y de gradientes cuadráticos pasados.
- AdaMax: es una modificación de Adam, adam suele dar mejores resultados
- AdaDelta: Es una variación de AdaGrad, en vez de calcular el escalado del factor de entrenamiento de cada dimensión, se restringe a una ventana de tamaño fijo de los últimos $n$ gradientes. Similar a RMSProp, que olvida gradientes.

# Número de Capas

Ante problemas complejos, las redes profundas tendrán mejor desempeño. Para muchos problemas, una capa será suficiente.

Lo habitual, es hacer una pirámide, poniendo cada vez menos neuronas, son técnicas que vienen de la experiencia empírica.