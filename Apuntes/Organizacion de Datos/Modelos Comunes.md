# Regresión Lineal

La primer forma de regresión lineal documentada fue el método de cuadrados mínimos. Consisten en aproximar los datos con una función lineal, y luego utilizar esta función lineal para predecir variables dependientes.

$$
Y \approx \beta_0 + \beta_1 X
$$

![[Apuntes/Organizacion de Datos/Attachments/Modelos Comunes 1.png|Untitled]]

## Medidas de Error/

- **RMSE (raíz del error cuadrático medio)**
- **MAE (error medio absoluto)**
- **MSE (error cuadrático medio)**

## Medidas de Comparación

- **RSS (Residual Sum of Squares):** Variabilidad no explicada por los datos
- **TTS (Total Sum of Squares):** Variabilidad total de los datos
- $R^2$ **(Coeficiente de Determinación):** Indica la capacidad de predicción del modelo. Muestra el porcentaje de relación que nuestro modelo puede explicar. Es la proporción de variabilidad explicada por los datos. Devuelve un valor entre 0 y 1.

# Regresión Logística

A partir de datos del problema, buscamos decidir si la muestra pertenece a una cierta categoría. Estas categorías son finitas y conocidas de antemano.

Se utiliza la regresión logística. Donde a partir de los datos, se crea una función del estilo $\frac{1}{1 + e^{-x}}$. Para encontrar esta función se grafican los datos, con un 0 si no pertenece a la categoria, y con un 1 si pertenece.

![[Apuntes/Organizacion de Datos/Attachments/Modelos Comunes 2.png|Untitled]]

Esta función asigna un valor entre 0 y 1, que indica la probabilidad de que la muestra pertenezca a la categoria. Diremos que la muestra pertenece a la categoria si $y \geq 0.5$.

# K-Means

Permite agrupar un conjunto de datos en una cantidad K de grupos:

1. El usuario decide una cantidad K de grupos
2. K-Means elige al azar K centroides
3. Forman un grupo con sus puntos mas cercanos
4. K-Means recalcula los centroides al centro de cada grupo
5. K-Menas vuelve a asignar los puntas utilizando los nuevos centroides
6. Repite 4 y 5 hasta que los puntos no cambien de grupo

![[Apuntes/Organizacion de Datos/Attachments/Modelos Comunes 3.png|Untitled]]

## Elección del K

### Regla del Codo

Se grafica la distancia promedio al centroide de cada punto en función de la cantidad de grupos y se selecciona el número donde se “quiebra” la gráfica

![[Apuntes/Organizacion de Datos/Attachments/Modelos Comunes 4.png|Untitled]]

### Método Silhouette

Utilizamos el coeficiente de Silhouette y graficamos para cada punto, para cada valor de $K$. Nos quedamos con la elección de K que minime los outliers.

Se define $a(i)$ como la distancia promedio de un punto $i$ al resto de puntos de su cluster

Se define $b(i)$ como la distancia promedio de un punto $i$ al los puntos del cluster externo mas cercano

$$
s(i) = \frac{b(i) - a(i)}{\max{[a(i), b(i)]}}
$$

![[Apuntes/Organizacion de Datos/Attachments/Modelos Comunes 5.png|Untitled]]

### Estadistica de Hopkins

Se utiliza para evaluar la tendencia de agrupación de un conjunto de datos midiendo la probabilidad de que un conjunto de datos sea generado por una distribución uniforme. Prueba la aleatoriedad espacial de los datos.

Si $H < 0.5$, Decimos que es poco probable que el conjunto de datos tenga conglomerados estadisticamente significativos. Si $H \approx 1$, Entonces concluimos que el conjunto de datos es un dato agrupable.