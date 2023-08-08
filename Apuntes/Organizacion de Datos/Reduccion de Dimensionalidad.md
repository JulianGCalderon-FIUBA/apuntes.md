Visualizamos los datos en una dimension menor a la que tenemos, preserviendo caracteristicas importantes de estas, como distancias o correlaciones.

- Permite enteneder facilmente la distribucion de los datos
- Reducimos el ruido de los datos
- Aceleramos los tiempos de entrenaiento del modelo
- Comprimimos la informacion
- Presentamos los datos de una forma prolija

Hay distintos algoritmos que resuelven este problema. Cada uno con sus ventajas y desventajas:

# PCA: Analisis de Componentes Principales

Permite reducir la informacion en componentes principales, manteniendo la distribucion de los datos y las agrupaciones formadas. 

Primero seleccionamos dos atributos

1. Calculamos el valor promedio de cada caracteristica
2. Calculamos el centro del conjunto de datos (centro de cada promedio)
3. Movemos el conjunto de datos, para que el origen de coordenadas este en el centro del conjunto de datos
4. Buscamos una linea que mejor ajuste a los datos, maximizando la suma de las distancias al cuadrado, medidas desde los puntos proyectados sobre la recta hasta el origen de coordenadas.

Esta linea que encontramos, se llamara componente principal 1: **PC1**. Se le llama a esta variable, una combinacion lineal de las variables. La proyeccion de cada nodo sobre esta recta sera la distancia de cada nodo a PC1. Las distancias al cuadrado sumadas seran: **Autovalor de PC1.**

Solemos trabajar con SVD, dividiendo por la longitud de la hipotenusa, obteniendo sus catetos normalizados. Las proporciones de cada eje se llamaran: **Loading Score de PC1.**

Buscamos **PC2**, debe ser perpendicular a nuestro otro componente, pasando por el eje de coordenadas. Si este no es unico, lo calculamos maximizando, como el PC anterior.

Luego, buscamos las variaciones de cada PC: $V_i = \frac{\text{Autovalor (PC $i$) }}{n-1}$. Siendo la variacion total $VT$ la suma de las variaciones. La proporcion de variacion de cada PC sera $P_i = V_i/VT$

Finalmente, nos quedaremos con los componentes principales con mas variacion acumulada, para no graficar informacion innecesaria.

Este algoritmo permite mantener las agrupaciones de datos, reduciendo la dimensionalidad de los datos.

# MDS: Multi-Dimensional Scaling

Hay dos variaciones, nos centraremos en la clasica (identica a PCoA). Se busca preservar distancia entre los puntos.

1. Calculamos todas las distancias (segun cualquier medida de distancia) entre dos puntos. (todas las posibilidades)
2. Realizamos una matriz de distancias
3. Buscamos una nueva matriz $M$, con la misma cantidad de columnas, pero reducimos la cantidad de filas (segun la dimension que quiera visualizar), donde las filas seran los valores $\text{MDS }i$

Al graficar este nuevo set de datos, encontraremos uno con distancias similares al set original

# t-SNE: t-distributed stochastic neighbor embedding

Similar a PCA, realizar una proyeccion para preservar los clusters

1. Proyecta todos los nodos sobre una recta, actualmente estan desordenados. Luego mueve los puntos uno por uno, en pasos secuenciales
2. Para cada cluster, lo mueve a izquierda o derecha dependiendo del resto de nodos
    1. Los puntos del mismo cluster, atraen al nodo
    2. Los puntos de otro cluster, repelen el nodo
3. Este algoritmo se repite hasta obtener el resultado deseado

Este algoritmo es lento, ya que es **iterativo**.

# ISOMAP

Hipotesis: La mayoria de los conjuntos de datos de alta dimensionidad quedan cerca de una variedad con muchas menos dimensines. Este supuesto de forma empirica.

> [!note]
> Una variedad es una porcion del espacio, de dimension $n$, que se parece a un espacio de una dimension menor.


**Distancia Geodesica**: La longitud de la linea de minima longitud que une dos puntos en una superficie dada, y esta contenida en la superficie.

Para aproximar esta distancia geodesica:

1. Para cada punto en el espacio de entrada, tomamos los $k$ vecinos mas cercanos (distancia euclidiana)
2. Trazamos aristas que conectan cada punto con sus vecinos, ponderamos esas aristas segun la distancia
3. Para encontrar la distancia minima en el grafo, utilizamos el algoritmo de dijkstra (u otro).

Este es un algoritmo muy lento, y puede generar una proyeccion erronea si $k$ es demasiado grande.

> [!note]
> Landmark ISOMAP es una variacion que consiste en seleccionar $N$ puntos especiales, y solo tomar las distancias que involucran estos puntos seleccionados.
