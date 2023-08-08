# ID3

**Iterative Dichotomiser 3** es un algoritmo creado por *Ross Quinlan*

Este algoritmo permite crear un arbol de decisiones a partir de un conjunto de ejemplos. Esto es un grafo acíclico con un nodo raiz, del cual parten los demas nodos.

Este arbol nos permite tomar decisiones a partir de ciertos valores de entrada. Los nodos hijos representan preguntas con respecto al valor de uno de los atributos. 

Para tomar deciciones, utiliza un concepto llamado **entropia (de la informacion o de Shannon)**.

![[Arboles 1.png|Untitled]]

 

Algoritmo basico:

1. Calcular la **entropía** para todas las clases
2. Calcular la **entropía** para cada valor posible de cada atributo
3. Seleccionar el mejor atributo basado en la **reducción de la entropía**. A partir del cálculo de **ganancia** de información
4. **Iterar**, para cada subnodo, excluyendo el nodo raíz.

## Entropía de Información

Es una medida de desorden o de pureza, mide la aleatoriedad de los datos. Para $n$ clases posibles. se utiliza la siguiente formula:

$$
E(S) = \sum p_i \log_2 \bigg [ \frac{1}{p_i} \bigg ]
$$

Donde:

- $S:$ Es una lista de clases posibles
- $P_i:$  Es la probabilidad de cada clase

Para una muestra homogenea, la entropia es $0$, mientras que, para $n{=}2$ la maxima entropia es $1$.

La entropia, no sirve para calcular otra medida, la ganancia de informacion.

## Ganancia de Informacion

Se aplica para saber que caracteristica de un conjunto nos proporciona la mayor cantidad de informacion. Definimos entonces:

$$
G(S, A) = E(S) - \sum_{v \in V(A)} \frac{|S_v|}{|S|} E(S_v)
$$

Donde:

- $S$: Es una lista de los valores posibles para el atributo $A$
- $A$: Uno de los atributos del set
- $V(A):$ Conjunto de valores de $A$.
- $S_v / S:$ Probabilidad de cada valor para el atributo $A$
- $E(S_v):$  Entropía calculada anteriormente, para el valor $v$ de $A$.

# Impureza de Gini

La impureza de Gini es una medida de cuán a menudo un elemento elegido aleatoriamente del conjunto sería etiquetado incorrectamente si fue etiquetado de manera aleatoria de acuerdo a la distribución de las etiquetas en el subconjunto. Utilizamos la siguiente formula:

$$
\text{Gini} = 1 - \sum_{i=1}^C p_i^2
$$

Donde $C$ implica el conjunto de clases, y $p_i$ la probabilidad de que el elemento pertenezca a esa clase. Se realiza este calculo para cada atributo.

Se realiza un promedio ponderado de las probabilidades, para cada valor posible del atributo.

# C4.5

Este algoritmo es una mejora al algoritmo de ID3:

- Se agrega soporte para rangos continuos. Para esto, se convierte el campo en un campo booleano, generando una particion a partir del umbral $c$. Este umbral se calcula a partir de la ganancia de informacion.
    - Se ordena de menor a mayor el conjunto
    - Identificamos los valores adyacentes (de la clase de salida)
    - Detectamos cuando se genera un cambio de salida, entones en esos limites estan nuestros $c_i$ cantidatos.
    - Se crean distintas particiones y se mantiene la que tenga mayor ganancia de informacion
- Se manejan  los datos faltantes. Para manejar los datos faltantes, estos se marcan y no se utilizan para el calculo de la entropia.
- Se introduce el metodo de **poda**: Se realiza un analisis recursivo, partiendo de las hojas, que elimina nodos, verificando si el testeo mejora o empeora tras eliminarlo. (a partir de error)

# Random Forest

> “**Muchos estimadores mediocres, promediados pueden ser muy buenos**”
> 

**Boostrap Aggregating:** Es una tecnica, o meta-algoritmo que dice lo siguiente:

Dado un conjunto de entrenamiento $D$, de tamaño $n$, la técnica de ***bagging*** generará **m** nuevos conjuntos de entrenamiento $D_1, \cdots, D_m$ cada uno de tamaño $n'$ tomando muestras aleatorias de $D$. Donde $n' \approx \frac 23 n$

Ahora, entrenamos un arbol para cada uno de estos conjuntos de datos, creando una matriz de confusion para cada uno de ellos. Realizando metricas (*accuracy*) para cada matriz de confusion.

Luego, a partir de un conjunto de entrenamiento, nos quedamos con el mejor arbol. Repetimos este proceso $k$ veces. 

Luego tendremos un conjunto de arboles (*forest*)*,* donde cada arbol vota. Si la mayoria de arboles devolvieron una misma categoria, nos quedamos con esa categoria.