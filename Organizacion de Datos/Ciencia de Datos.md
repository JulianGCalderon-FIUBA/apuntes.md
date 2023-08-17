---
title: Ciencia de Datos
---

La idea es crear modelos predictivos a partir de un conjunto de datos. Los modelos tienen dos partes

- **Datamining**: Técnicas que vienen de la estadística y fórmulas
	- Regresión Lineal
	- Análisis Discriminante
	- Análisis de componentes principales
- **Machine** **Learning**: Hacen uso de la inteligencia artificial
	- Redes neuronales
	- *Support Vector Machines (SVM)*
- Elementos que combinan ambas
	- Algoritmo ID3 (árboles de decisión)
	- K-Means (distancia euclidiana)
	- Bayes Naive (probabilidad condicional, teorema de Bayes)

## Tipos de Variables

- Variables Independientes: Utilizadas para entrenar el modelo (entrada)
	- Cualitativas
		- Texto
			- Nominales (categorías)
			- Ordinales (poco, mucho)
		- Numéricas
			- Nominales
			- Ordinarias
	- Cuantitativas
		- Discreta
		- Continua
- Variables dependientes (salidas, categorías)

## Tipos de Problemas

1. Si la variable dependiente es cualitativa, el tipo de problema es de **clasificación**. Buscamos clasificar una observación en función de sus datos de entrada
2. Si la variable es cuantitativa, el problema es de **regresión**. Buscamos predecir un valor en función de otros
3. Si no hay variables dependientes, el problema es de **agrupamiento**. Buscamos agrupar observaciones según sus características.

## Outliers

Los **outliers** son valores atípicos, debemos decir que hacer con estas observaciones. Hay distintas técnicas para lidiar con estos datos.

## Correlación entre Variables

hay distintos tipos de correlación:

- Positiva
- Negativa
- Sin correlación

La correlación NO implica causalidad. Pueden no tener relación entre sí, o depender de una tercera variable externa.

Las relaciones de causalidad son difíciles de encontrar y demostrar.

> [!note] Ejemplos de Correlaciones Inexplicables
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
