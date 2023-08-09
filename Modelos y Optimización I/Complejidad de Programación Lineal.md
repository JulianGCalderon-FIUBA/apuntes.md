## Método Simplex

En la práctica, este método es eficiente. El el caso promedio, se puede resolver en tiempo polinomial. Sin embargo, en el peor caso, su complejidad es exponencial. Se creía ser un problema $NP$

## Método del Elipsoide

El método del elipsoide es un algoritmo polinómico para los problemas de programación lineal continua. Si bien no se usa en la practica, su hallazgo fue de gran importancia teórica, ya que permitió clasificar a los problemas de programación lineal continua como un problema $P$.

### ¿Porque se utiliza el método Simplex?

Simplex nos motiva a repensar las métricas de complejidad, ya que es un algoritmo de complejidad exponencial que en la práctica es similar a los algoritmos polinómicos conocidos. Entonces, si bien no garantiza tiempos polinomiales en todos los casos, en la mayoría sí lo hace.

Además, nos permite realizar análisis de sensibilidad y responder de forma rápida a las modificaciones del problema.

## Programación Lineal Entera

Si existiese una reducción en tiempo polinomial para convertir un problema de programación lineal a su capsula convexa, entonces sería un problema $P$ (ya que la programación lineal continua lo es). Lamentablemente, este algoritmo no existe, haciendo que la resolución de la programación lineal entera sea un problema $NP$.
