## Regresión Lineal

La primera forma de regresión lineal documentada fue el método de cuadrados mínimos. Consisten en aproximar los datos con una función lineal, y luego utilizar esta función lineal para predecir variables dependientes.

$$
Y \approx \beta_0 + \beta_1 X
$$

![[Modelos Comunes 1693351687.png|475]]

### Medidas de Error/

- **RMSE (raíz del error cuadrático medio)**
- **MAE (error medio absoluto)**
- **MSE (error cuadrático medio)**

### Medidas de Comparación

- **RSS (Residual Sum of Squares):** Variabilidad no explicada por los datos
- **TTS (Total Sum of Squares):** Variabilidad total de los datos
- **$R^2$ (Coeficiente de Determinación):** Indica la capacidad de predicción del modelo. Muestra el porcentaje de relaciones que nuestro modelo puede explicar. Es la proporción de variabilidad explicada por los datos. Devuelve un valor entre 0 y 1.

## Regresión Logística

A partir de datos del problema, buscamos decidir si la muestra pertenece a una cierta categoría. Estas categorías son finitas y conocidas de antemano.

Se utiliza la regresión logística. Donde a partir de los datos, se crea una función del estilo $\frac{1}{1 + e^{-x}}$. Para encontrar esta función se grafican los datos, con un 0 si no pertenece a la categoría, y con un 1 si pertenece.

![[Modelos Comunes 1693351687-1.png|500]]

Esta función asigna un valor entre 0 y 1, que indica la probabilidad de que la muestra pertenezca a la categoría. Diremos que la muestra pertenece a la categoría si $y \geq 0.5$.

## K-Means

Permite agrupar un conjunto de datos en una cantidad K de grupos:

1. El usuario decide una cantidad K de grupos
2. K-Means elige al azar K centroides
3. Forman un grupo con sus puntos más cercanos
4. K-Means recalcula los centroides al centro de cada grupo
5. K-Menas vuelve a asignar las puntas utilizando los nuevos centroides
6. Repite 4 y 5 hasta que los puntos no cambien de grupo

![[Modelos Comunes 1693351687-2.png|500]]

### Elección del K

#### Regla del Codo

Se grafica la distancia promedio al centroide de cada punto en función de la cantidad de grupos y se selecciona el número donde se "quiebra" la gráfica

![[Modelos Comunes 1693351688.png|500]]

#### Método Silhouette

Utilizamos el coeficiente de Silhouette y graficamos para cada punto, para cada valor de $K$. Nos quedamos con la elección de K que minimice los outliers.

Se define $a(i)$ como la distancia promedio de un punto $i$ al resto de puntos de su clúster

Se define $b(i)$ como la distancia promedio de un punto $i$ al los puntos del clúster externo más cercano

$$
s(i) = \frac{b(i) - a(i)}{\max{[a(i), b(i)]}}
$$

![[Modelos Comunes 1693351688-1.png|500]]

#### Estadística de Hopkins

Se utiliza para evaluar la tendencia de agrupación de un conjunto de datos midiendo la probabilidad de que un conjunto de datos sea generado por una distribución uniforme. Prueba la aleatoriedad espacial de los datos.

Si $H < 0.5$, Decimos que es poco probable que el conjunto de datos tenga conglomerados estadísticamente significativos. Si $H \approx 1$, Entonces concluimos que el conjunto de datos es un dato agrupable.
