---
title: Reduccion de Dimensionalidad
---

Visualizamos los datos en una dimensión menor a la que tenemos, preservando características importantes de estas, como distancias o correlaciones.

- Permite entender fácilmente la distribución de los datos
- Reducimos el ruido de los datos
- Aceleramos los tiempos de entrenamiento del modelo
- Comprimimos la información
- Presentamos los datos de una forma prolija

Hay distintos algoritmos que resuelven este problema. Cada uno con sus ventajas y desventajas:

## PCA: Análisis de Componentes Principales

Permite reducir la información en componentes principales, manteniendo la distribución de los datos y las agrupaciones formadas.

Primero seleccionamos dos atributos

1. Calculamos el valor promedio de cada característica
2. Calculamos el centro del conjunto de datos (centro de cada promedio)
3. Movemos el conjunto de datos, para que el origen de coordenadas este en el centro del conjunto de datos
4. Buscamos una línea que mejor ajuste a los datos, maximizando la suma de las distancias al cuadrado, medidas desde los puntos proyectados sobre la recta hasta el origen de coordenadas.

Esta línea que encontramos, se llamara componente principal 1: **PC1**. Se le llama a esta variable, una combinación lineal de las variables. La proyección de cada nodo sobre esta recta será la distancia de cada nodo a PC1. Las distancias al cuadrado sumadas serán: **Autovalor de PC1.**

Solemos trabajar con SVD, dividiendo por la longitud de la hipotenusa, obteniendo sus catetos normalizados. Las proporciones de cada eje se llamarán: **Loading Score de PC1.**

Buscamos **PC2**, debe ser perpendicular a nuestro otro componente, pasando por el eje de coordenadas. Si este no es único, lo calculamos maximizando, como el PC anterior.

Luego, buscamos las variaciones de cada PC: $V_i = \frac{\text{Autovalor (PC i) }}{n-1}$. Siendo la variación total $VT$ la suma de las variaciones. La proporción de variación de cada PC será $P_i = V_i/VT$

Finalmente, nos quedaremos con los componentes principales con más variación acumulada, para no graficar información innecesaria.

Este algoritmo permite mantener las agrupaciones de datos, reduciendo la dimensionalidad de los datos.

## MDS: Multi-Dimensional Scaling

Hay dos variaciones, nos centraremos en la clásica (idéntica a PCoA). Se busca preservar distancia entre los puntos.

1. Calculamos todas las distancias (según cualquier medida de distancia) entre dos puntos. (todas las posibilidades)
2. Realizamos una matriz de distancias
3. Buscamos una nueva matriz $M$, con la misma cantidad de columnas, pero reducimos la cantidad de filas (según la dimensión que quiera visualizar), donde las filas serán los valores $\text{MDS }i$

Al graficar este nuevo set de datos, encontraremos uno con distancias similares al set original

## t-SNE: t-distributed stochastic neighbor embedding

Similar a PCA, realizar una proyección para preservar los clústeres

1. Proyecta todos los nodos sobre una recta, actualmente están desordenados. Luego mueve los puntos uno por uno, en pasos secuenciales
2. Para cada clúster, lo mueve a izquierda o derecha, dependiendo del resto de nodos
	1. Los puntos del mismo clúster, atraen al nodo
	2. Los puntos de otro clúster, repelen el nodo
3. Este algoritmo se repite hasta obtener el resultado deseado

Este algoritmo es lento, ya que es **iterativo**.

## ISOMAP

**Hipótesis:** La mayoría de los conjuntos de datos de alta dimensionalidad quedan cerca de una variedad con muchas menos dimensiones. Este supuesto de forma empírica.

> [!note]
> Una variedad es una porción del espacio, de dimension $n$, que se parece a un espacio de una dimension menor.

**Distancia Geodésica**: La longitud de la línea de mínima longitud que une dos puntos en una superficie dada, y está contenida en la superficie.

Para aproximar esta distancia geodésica:

1. Para cada punto en el espacio de entrada, tomamos los $k$ vecinos más cercanos (distancia euclidiana)
2. Trazamos aristas que conectan cada punto con sus vecinos, ponderamos esas aristas según la distancia
3. Para encontrar la distancia mínima en el grafo, utilizamos el algoritmo de Dijkstra (u otro).

Este es un algoritmo muy lento, y puede generar una proyección errónea si $k$ es demasiado grande.

> [!note]
> Landmark ISOMAP es una variación que consiste en seleccionar $N$ puntos especiales, y solo tomar las distancias que involucran estos puntos seleccionados.
