## Bias vs. variance

- Bias: Es el debido al modelo según la diferencia entre el valor esperado del estimador y el valor real.
- Varianza: Se define como cuanto varia el modelo según los datos de entrada.

Se busca tener *low bias, low variance*

![[Ensambles 1.png]]

## Ensamble de Modelos

A veces, un solo modelo no es suficiente para aprender un concepto completo, pero muchos modelos en conjuntos pueden aprender una gran parte del concepto

![[Ensambles 2.png]]

Se puede utilizar un proceso de *votación* para obtener la mejor clase, utilizando la predicción de cada modelo. Si devuelven probabilidades, se puede hacer una votación ponderada.

## Bagging

Es una técnica que consiste en construir nuevos conjuntos de entrenamiento utilizando bootstrap, para entrenar distintos modelos y combinarlos.

Esta técnica, tiene diversas ventajas:

- Disminuye la varianza final de nuestro modelo
- Efectivo en conjuntos de datos con alta varianza
- Reduce el overfitting
- Reduce el ruido de los outliers

Para el caso de árboles, si hay algunos atributos mças importantes que otros, todos los árboles se parecerán entre sí.

## Boosting

Es una alternativa, busca nuevos modelos para las instancias clasificadas por los modelos anteriores. Para cada iteración, se reentrena el modelo dándole mayor importancia a los datos mal clasificados.

Al final, podemos realizar una votación ponderada por todos los modelos construidos.

Esta técnica necesita pesos. Debemos adaptar nuestro algoritmo de aprendizaje y tomar muestras con reemplazo según los pesos.

También puede sobre ajustar a los datos de entrada.

## Modelos Exitosos

Algunos modelos que implementan estas técnicas son:

- [[AdaBoost]]
- [[Gradient Boost]]
- [[XGBoost]]

## Ensambles Híbridos

Los ensambles homogéneos combinan el mismo tipo de modelo:

- Bagging
- Boosting

Los ensambles híbridos combinan clasificadores de distinto tipo:

- Voting: Construimos $n$ modelos (distintos) con los mismo datos, y tomamos la predicción mayoritaria
- Stacking: Entrenamos diferentes modelos, y un nuevo modelo que decide (dada una instancia nueva) que modelo utilizar.
	- Se puede interpretar como una mejora del modelo
	- Funciona mejor si los clasificadores base pueden generar medidas de certeza (probabilidad)
- Cascading: Se pasa sucesivamente los datos de un modelo a otro.
	- A diferencia de stacking, cada capa tiene un solo modelo.
	- Los modelos se entrenan con las instancias predichas con baja certeza por el modelo anterior.
	- A diferencia de voting y stacking tienen un enfoque *multi-experto*, cascading tiene un enfoque *multi-estado*.

Los ensambles permite generar clasificadores con más precisión, a cambio de menor compresión de los mismos. Además de tener mayor complejidad computacional.
