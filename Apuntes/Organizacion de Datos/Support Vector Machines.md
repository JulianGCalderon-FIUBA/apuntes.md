Este método permite separar un conjunto de datos en dos, de forma lineal. Se dice que los datos son linealmente separables si puedo encontrar un cuerpo lineal que los separa. (punto, línea, superficie, etc)

## Clasificador con Margen

Cuando los datos están en una sola dimensión, podemos definir un umbral para separar las observaciones. El umbral, lo podes colocar en el punto medio entre los conjuntos: **Maximal Margin Classifier.**

El problema es que este método es sensible a los outliers, podemos mejorarlo permitiendo clasificaciones erróneas. Estas no serán tan afectadas por los valores atípicos: **Soft Margin Classifier.**

![[Apuntes/Organizacion de Datos/Attachments/Support Vector Machines 1.png|Untitled]]

Para utilizar el margen, se puede utilizar la validación cruzada:

- Se partirá el conjunto en $n$ subconjuntos
- Utilizara pares de observaciones similares para calcular la distancia media del umbral, validando la clasificación con otros conjuntos
- Se debe definir de antemano cuantas clasificaciones erróneas soportar

## Otras Dimensiones

Cuando analizamos otras dimensiones, entonces los margenes ya no seran puntos:

![[Apuntes/Organizacion de Datos/Attachments/Support Vector Machines 2.png|Untitled]]

![[Apuntes/Organizacion de Datos/Attachments/Support Vector Machines 3.png|Untitled]]

La ventaja de este método es que puede soportar la existencia de outliers.

## Support Vector Machines

¿Que pasa cuando nuestro conjunto de datos no es linealmente separable? En esto casos, debemos aplicar algoritmos para llevar el conjunto de datos a otra dimensión, y poder separarlo.

![[Apuntes/Organizacion de Datos/Attachments/Support Vector Machines 4.png|Untitled]]

![[Apuntes/Organizacion de Datos/Attachments/Support Vector Machines 5.png|Untitled]]

El algoritmo detrás de este método usa algo llamado **Funciones Kernel**, que sistemáticamente buscan clasificadores de tipo **Support Vector Classifiers** en dimensiones altas.

Estas funciones kernel sólo calculan la distancia como si estuviesen en otra dimensión, pero no realizan la verdadera transformación. Este truco reduce la cantidad de computo necesario.