---
title: Transformación de Datos
---

Algunas tareas de estas etapas son:

- **Integración de Datos:** Integración de múltiples bases de datos, archivos.
- **Limpieza de Datos:** Completar valores faltantes, eliminar el ruido. Identificar y eliminar valores atípicos y corregir incoherencias
- **Reducción de Datos:** Reducción de dimensionalidad y numerosidad
- **Transformación de Datos:** Normalizaciones, generación de jerarquías conceptuales *(feature engineering).*

## Limpieza de Datos

Hay muchos tipos de datos que pueden ser identificados como datos faltantes. Como datos inconsistentes, errores de tipeo, errores de escalas, entre otros.

Algunos errores se pueden arreglar a partir del resto de observaciones del *dataset*.

### Datos Faltantes

Existen diferentes mecanismos de datos faltantes:

- **MCAR (missing completely at random):** En este caso, la razón de falta del dato es ajena a los datos mismos. No está relacionado con la variable, faltan por azar.
- **MNAR (missing not at random):** Se dice así cuando la razón de falta de datos está totalmente relacionado con los datos mismos.
- **MAR (missing at random):** Propio de las encuestas mal diseñadas. Es un punto medio entre los dos mecanismos anteriores. No está relacionado con los datos en sí, pero si con alguna otra variable. Por ejemplo: ¿A qué se dedican tus hijos? Cuando la persona entrevistada no tiene hijos. En este caso dejaría el campo en blanco.

Algunas estrategias para lidiar con los datos faltantes:

- Eliminar registros o variables: No se recomienda en situaciones de MCAR. Si la eliminación de un subconjunto disminuye significativamente la utilidad de los datos, entonces puede no ser efectiva.
- Imputar Datos: Utilizar métodos de relleno de faltantes, ya sea a partir de un algoritmo de aprendizaje automático o consultando con un experto. Esta estrategia trae sus consecuencias.

### Imputación de Datos

Algunas estrategias para imputar los datos faltantes:

- **Sustitución de Casos:** Se reemplaza con valores no observados. Hay que consultar con un experto.
- **Sustitución por Media:** Se reemplaza utilizando la medida calculada de los valores presentes. Sin embargo, esto trae consecuencias
	- La varianza estimada por la nueva variable no es válida, ya que es atenuada por los valores repetidos
	- Se distorsiona la distribución
	- Las correlaciones que se observen estarán deprimidas debido a la repetición de un solo valores constante.
- **Imputación Cold Deck:** Se pueden obtener los datos faltantes a partir de otras variables del dataset.
- **Imputación Hot Deck:** Se reemplazan los datos faltantes con los valores que resultan más "similares". Tenemos que definir que es "similar".
- **Imputación por Regresión:** El dato faltante es reemplaza con el valor predicho por un modelo de regresión.
- **MICE (multivariate imputation by chained equations):** Trabaja bajo el supuesto de que el origen de los datos es MAR. Es un proceso de imputación iterativo, donde cada iteración los valores faltantes se predicen en función de las variables restantes. El proceso se repite hasta que se encuentre consistencia en los datos (usualmente 10 iteraciones es suficiente). La primera iteración se realiza por uno de los métodos vistos anteriormente para rellenar los datos faltantes.

## Transformación de Datos

El objetivo principal de esta etapa es mejorar el rendimiento de los modelos creados mediante la transformación de los datos que se utilizan.

Algunas técnicas son:

- **Normalización**: Consiste en escalar los valores para llevarlos a un rango más pequeño.
- **Discretización**: Llevar una variable de rango continuo a rango discreto
- **Lograr Normalidad**: Se utiliza cuando se quiere llevar los datos a una distribución normal.
- **Imaginación**: Generación de nuevas variables a partir de los datos. O a partir de incorporar nuevas fuentes.

### Normalización

Es principalmente utilizada cuando las unidades de medida dificultan la comparación de *features*. Se busca evitar que los atributos con mayores magnitudes tengan más peso que el resto.

- $X_{\min}^* = \frac{X - \min X}{\text{range } X}$: Algoritmo *MinMax* que lleva una variable a un rango entre 0 y 1.
- $Z{-}score = \frac{X - \mu}{\sigma}$: Los valores se normalizan basándonos en su media y desvío estándar.
- $X_{\text{decimal}} = \frac{X}{10^d}$: Asegura que cada valor normalizado se encuentra entre -1 y 1

Son transformaciones que respetan la distribución original

### Discretización

Algunos métodos para esta técnica son:

- **Binning**: Busca dividir una variable en un número específico de **bins**. Hay distintos criterios de agrupamiento:
	- **Igual-Frecuencia:** La misma cantidad de observaciones en un *bin*
	- **Igual-Ancho:** Dividimos rangos o intervalos de clases para cada *bin*
	- **Cuantiles:** Separar los inter valores según los distintos cuantiles de la variable (mediana, cuartiles, percentiles).

### One Hot Encoding (variables dummies)

Cuando el modelo que buscamos usar no permite variables categóricas, utilizamos variables *dummies*. Creamos una variable por cada valor distinto de la categoría y le damos el valor binario 0 o 1, para indicar si pertenece o no a esa variable. Solo necesitamos $k{-}1$ variables para $k$ categorías, ya que son conjuntos excluyentes.
