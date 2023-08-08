Un outlier es una observación que se desvía tanto de las otras observaciones como para despertar sospecha que fue generado por un mecanismo diferente ~ *D. Haukins. Identification of Outliers (1980)*

- Es un concepto subjetivo al problema.
- Son observaciones distantes al resto de los datos.
- Pueden deberse a un error de medición, aleatoriedad, etc.

La presencia de outliers puede influenciar los resultados de un análisis estadístico clásico.

**¿Es necesario eliminarlos?**

- Deben ser cuidadosamente inspeccionados
- Pueden estar alertando anomalías, en algunas situaciones nuestra tarea de interés será encontrarlos.

# Tipos de Outliers

Hay diferentes tipos de outliers:

- Global Outlier: Los datos están alejados del resto de datos.
- Contextual Outlier: Los datos son anómalos debido a su contexto (temperatura alta en invierno)
- Collective Outlier: Subgrupos dentro de un conjunto de datos.

Segun las variables:

- Univariados: Podemos encontrar en una sola variable, son buenos para deteccion de extremos.
- Multivariados: Se pueden encontrar en un espacio n-dimensional. Para detectarlos es necesario ajustar un modelo.

Los outliers, en casos multivariados, pueden provocar dos tipos de efectos:

- El efecto de enmascaramiento se produce cuando un grupo de outliers esconden a otros. Se harán visibles cuando se eliminen los outliers que los esconden
- El efecto de inundación ocurre cuando una observación solo es outlier en presencia de otras observaciones.

# Detección de Outliers

Para el caso de los outliers univariados, tomó información respecto a la distribución de la variable

- Z-score: Realizamos esta transformación y tomamos como outliers a los valores cuyo modulo es mayor a 3.
- Z-score Modificado: Tomamos una medida nueva llamada MAD (median absolute deviation). Tomamos como outliers los valores cuyo módulo es mayor a 3.5.
- IQR: Tomamos outliers según su distancia a los cuartiles extremos (primero y tercero) de la variable. Si la distancia es $\pm 1.5\cdot IQR$ se considera un outlier moderado. Si la distancia es $\pm3.5 \cdot IQR$ se considera un outlier severo. Definimos $IQR$ como la distancia entre el primer y el tercer cuartil.

Para el caso de los outliers multivariados:

- Clustering: Utilizando medidas de distancia como Mahalanobis, los valores similares son agrupados y los que quedan aislados pueden ser considerados outliers.
- LOF (local outlier factor): Método basado en distancias, calcula un *score de outlier* a partir de una distancia que se normaliza por densidad (observa la densidad de los vecinos para detectar si el punto está aislado o se encuentra en una zona densa)
- Isolation Forest: Consiste en partir las variables en intervalos al azar de forma recursiva hasta aislar todas las variables. Se realizan muchas iteraciones y los valores que se pudieron aislar rápidamente en la mayoría de los casos se consideran outliers.

**Distancia de Mahalanobis**: Es una distancia no euclidiana que tiene en cuenta la media de todos los parámetros, y cómo se relacionan entre sí (a partir de la matriz de covarianzas)