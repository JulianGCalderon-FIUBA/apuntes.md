---
title: Clasificación de Texto
---

Es un problema de clasificación, sirve para asignar un tópico o categoría de forma automática a algún extracto de texto.

## Métodos de Clasificación

- **Reglas escritas a mano:** Si el texto contiene cierta palabra particular, entonces se catalogara en la categoría designada
	- **PROS:** La precisión de este método puede ser muy alta
	- **CONS:** Construir y mantener estas reglas puede ser costoso
- **Aprendizaje automático supervisado**: Se tiene un documento $d$, un conjunto $C$ fijo de clases, y un conjunto $m$ de documentos clasificados. Buscamos entrenar un modelo clasificador.

## Tipos de Clasificadores

- **Naïve Bayes**
- **Logistic Regression**
- **Support-Vector Machines**
- **K-Nearest Neighbors**

## Naïve Bayes

Un enfoque posible para la resolución es encontrar la probabilidad de que un documento pertenezca a cierta clase. Utilizaremos probabilidad condicional

$$
P(C | d) = \frac{P(d | c) P(c)}{P(d)}
$$

Si tenemos un conjunto $C$ de clases, busquemos la clase que maximice esta probabilidad.

Necesitaremos, ahora, calcular estas probabilidades. Para $P(c)$, utilizaremos la fórmula de Laplace con el conjunto de documentos que tendremos para el entrenamiento.

Usaremos un método conocido como **bag word**. Un documento será entonces una bolsa de características, o palabras. Las probabilidades de cada característica $x_1,x_2,...$ dada una clase, son independientes entre sí.

El orden de las palabras no importa. Esto trae algunos inconvenientes.

Ventajas:

- Este algoritmo es muy rápido y requiere poco almacenamiento.
- Es robusto ante características irrelevantes
- Es muy bueno en dominios en donde hay muchas características y todas son importantes.

### Bag Word

Contamos todas las palabras que aparecen en los documentos, y hacemos una lista de palabras y sus ocurrencias.

Podemos usar solo algunas palabras, en lugar de todas. Filtrando palabras.

$$
P(d|c) = P(x_1,x_2,...|c) = P(x_1|c) * P(x_2|c) * ...
$$

Entonces la probabilidad de que cierta característica provenga de una clase, la calcularemos como

$$
P(x_i|c) = \frac{\text{Cantidad de veces que aparece $x_i$ en documentos de la clase $C$}}{\text{Cantidad de veces que aparece $x_i$ en todos los documentos}}
$$

### Laplace Smoothing

Consiste en sumar 1 a cada cantidad ($w_i, c_j)$ calculada. Normalizamos también agregando en el denominador uno por cada palabra del vocabulario.

Esto soluciona el caso de que surge una palabra nueva, y la probabilidad para cada clase es 0.

## Redes Bayesianas

Para entender o modelar el conocimiento de un clasificador de Bayes naïve, utilizaremos redes bayesianas. Grafos acíclicos.

Estas redes tienen una tabla asociada a cada nodo, con las probabilidades condicionales.

Estas redes permiten hacer inferencias, para calcular probabilidades condicionales complejas.

Estas redes son complejas de construir y mantener, pero son útiles para modelar conocimiento.
