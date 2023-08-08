# Separación Entrenamiento / Test

Nunca se utiliza el mismo dato para entrenar un método que para testearlo. Separamos una porción de los datos para testear (aproximadamente un $20\%$ o $30\%$)

**Cross-Validation Split:** A partir de los datos de entrenamiento, separamos en 5 secciones aleatorios y realizamos 5 entrenamientos distintos. Se realiza esto para validar que tomemos las muestras correctamente y elegir los mejores hiperparametros.

![https://scikit-learn.org/stable/_images/grid_search_cross_validation.png](https://scikit-learn.org/stable/_images/grid_search_cross_validation.png)

# Conjuntos Balanceados

Ambas técnicas consisten en incluir más muestras de una clase que de otra, con el fin de compensar el desbalance se ya se encuentra presente en los datos. 

**Undersampling:** Se toman menos muestras de la clase mayoritaria con el fin de balancear el test de entrenamiento

**Oversampling:** Se duplican muestras del test minoritario con el fin de obtener un set mayor de entrenamiento.

![[Entrenamiento y Testing 1.png|Untitled]]

# Overfitting

Al entrenar un metodo, pueden ocurrir distintos resultados:

- **Underfitting**: El método no se entrenó correctamente por lo que no predice correctamente
- **Overfitting**: El método se aprendió de memoria los datos de entrenamiento, pero no funciona de forma correcta con un set de datos nuevo
- **Balanced**: El método se entrena correctamente y es útil para predecir.

![[Entrenamiento y Testing 2.png|Untitled]]

# Métricas

Hay distintos conceptos que podemos utilizar para definir la eficacia de un método entrenado.

- **TP (True Positive)**: Cantidad de clasificaciones positivas, correctas
- **FP (False Positive)**: Cantidad de clasificaciones positivas, incorrectas
- **TP (True Negative)**: Cantidad de clasificaciones negativas, correctas
- **FP (False Negative)**: Cantidad de clasificaciones negativas, incorrectas

A partir de estos valores, podemos definir:

- **Accuracy:** $\frac{TP + TN}{TP + TN + FP + FN} \to$ Representa qué proporción de la muestra clasificó correctamente.
- **Precision:** $\frac{TP}{TP+ FP} \to$ Indica la proporción de *TP* respecto a los acertados
- **Recall:** $\frac{TP}{TP + FN} \to$ Indica la proporcion de los *TP* respecto al total de positivos. También se lo conoce como *TPR (true positive rate)*
- **FPR:** $\frac{FP}{FP + TN} \to$ Indica la proporción de los FP respecto al total de negativos.
- **F1-Score:** $\frac{a}{b} \to$ ***Indica un balance entre *accuracy* y *recall*.

![[Entrenamiento y Testing 3.png|Untitled]]

# ROC

A partir de modificar el modelo (cambiando los hiperparametros) podemos obtener predicciones diferentes. Luego podemos graficar el **ROC**. Que muestra el *TPR* a partir del *FPR*

![[Entrenamiento y Testing 4.png|Untitled]]

Luego, nos quedamos con los hiperparametros que predigan mejor nuestro modelo.

**AUC**: Llamamos AUC al área bajo la curva. A mayor área bajo la curva, mejor nuestro predictor.