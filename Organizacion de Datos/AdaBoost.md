Esta técnica consiste en entrenar un predictor, un clasificador base, calcular los errores que comete, y entrenar un nuevo predictor que corrija estos errores. 

El proceso se repite $n$ veces hasta disminuir el error. Esta técnica no puede realizarse en paralelo, por lo que es poco escalable al tener grandes volúmenes de árboles.

Los árboles utilizados son ***stumps***, árboles con un solo nodo y dos hojas 

A cada observación del ***dataset*** se le asigna un peso, este se utiliza en la creación de ***stumps***. Inicialmente, todos tienen el mismo peso inicial $\frac 1n$

En cada iteración, se crea un tocón o **stump** para cada atributo, seleccionado aquel que tenga menor impureza de ***Gini.***

Para calcular el peso relativo del tocón en el clasificador final, utilizamos una métrica llamada ***Amount of Say.***

$$
\text{Amount of Say} = \frac 12 \ln (\frac{1 - \text{Total Error}}{\text{Total Error}})
$$

Debemos aumentar el peso relativo de cada instancia mal clasificada, para por mejorar esas predicciones.

Para realizar esto, calcularemos el nuevo peso de la siguiente forma, a partir del peso anterior.

$$
\text{Peso}_i = \text{Peso}_{i-1} \cdot e^{\text{Amount of Say}}
$$

Para calcular el peso de las instancias bien clasificados, utilizaremos la función inversa.

$$
\text{Peso}_i = \text{Peso}_{i-1} \cdot e^{\text{-Amount of Say}}
$$

Para la siguiente iteración, podemos usar la impureza de ***Gini*** como realizamos anteriormente, o bien podemos crear un nuevo *dataset* teniendo en cuenta los pesos recientemente calculados

Agregamos una nueva columna llamada distribución, que es la suma sucesiva de los pesos de cada observación

| Sample Weight | 0.25 | 0.4 | 0.45 |
| --- | --- | --- | --- |
| Distribution | 0.25 | 0.64 | 1 |

Luego, tomamos un número al azar y elegimos la observación a la que le corresponda el número, a partir de la distribución

Copiamos los valores que salen en el nuevo dataset, hasta llegar a un dataset del mismo tamaño (pueden quedar observaciones repetidas)

Volvemos a realizar el algoritmo visto con el nuevo dataset. Repitiendo este algoritmo lo necesario.

Una vez obtenido nuestro bosque, utilizamos el Amount of Say de cada árbol, para tomar una decisión a partir de una votación.