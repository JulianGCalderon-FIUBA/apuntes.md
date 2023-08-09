La idea es crear modelos predictivos a partir de un conjunto de datos. Los modelos tienen dos partes

- **Datamining**: Técnicas que vienen de la estadística y fórmulas
	- Regresión Lineal
	- Análisis Discriminante
	- Análisis de componentes principales
- **Machine** **Learning**: Hacen uso de la inteligencia artificial
	- Redes neuronales
	- Support Vector Machines (SVM)
- Elementos que combinan ambas
	- Algoritmo ID3 (arboles de decision)
	- K Means (distancia euclidiana)
	- Bayes Naive (probabilidad condicional, teorema de bayes)

## Tipos de Variables

- Variables Independientes: Utilizadas para entrenar el modelo (entrada)
	- Cualitativas
		- Texto
			- Nominales (categorias)
			- Ordinales (poco, mucho)
		- Numericas
			- Nominales
			- Ordinarias
	- Cuantitativas
		- Discreta
		- Continua
- Variables dependientes (salidas, categorias)

## Tipos de Problemas

1. Si la variable dependiente es cualitativa, el tipo de problema es de **clasificacion**. Buscamos clasificar una observacion en funcion de sus datos de entrada
2. Si la variable es cuantitativa, el problema es de **regresión**. Buscamos predecir un valor en funcion de otros
3. Si no hay variables dependientes, el problema es de **agrupamiento**. Buscamos agrupar observaciones segun sus caracteristicas.

## Outliers

Los outliers son valores atipicos, debemos decir que hacer con estas observaciones. Hay distintas técnicas para lidiar con estos datos.

## Correlacion entre Variables

hay distintos tipos de correlacion:

- Positiva
- Negativa
- Sin correlación

La correlación NO implica causalidad. Pueden no tener relación entre si, o depender de una tercer variable externa.

Las relaciones de causalidad son difíciles de encontrar y demostrar.

> [!note]
> [https://www.tylervigen.com/spurious-correlations](https://www.tylervigen.com/spurious-correlations)

### Varianza

Es el error cuadrático medio de las observaciones respecto a su media. Representa que tan separadas están las muestras.

$$
\text{Var} = \frac{\sum (x - \overline x)^2}{n-1}
$$

### Covarianza

Indica el grado de variación conjunta de dos variables aleatorias respecto a sus medias. Toma un valor entre -1 y 1.

$$
\text{Cov} = \frac{\sum (x - \overline x)^2(y - \overline y)^2}{n}
$$

Si los datos se encuentran en escalas distintas, entonces podemos encontrar números mucho mayores, por lo que se suele utilizar la **Correlación de Pearson**.

$$
\rho = \frac{\text{Cov}(X,Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}}
$$

Si da 1, las variables están relacionadas linealmente de forma perfecta

Si da -1, las variables están relacionadas linealmente (negativa) de forma perfecta.

### Desvío Estándar

Se utiliza para cuantificar la variación o la dispersión de un conjunto numérico. Un desvío estándar bajo indica un mayor agrupamiento de los datos.
