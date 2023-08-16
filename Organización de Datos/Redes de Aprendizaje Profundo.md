---
title: Redes de Aprendizaje Profundo
---

Es una estrategia que creció en popularidad recientemente, se utiliza para resolver problemas más complejos.

Se separa la red en distintas capas, de esta forma podemos obtener comportamientos avanzados

- Reconocimiento facial
- Reconocimiento del habla
- etc.

Hay dos tipos principales de problemas

- **Clasificación**: Deep Belief Networks y Perceptrones Multicapa con Rectified Linear Units (RELU)
- **Análisis de serie de tiempo**: Recurrent net

## Tiempo de Entrenamiento

Suelen tardar mucho tiempo en entrenarse, las redes de aprendizaje profundo puede tardar meses en ser entrenada. Con el incremento de GPUs, estos tiempos se pueden reducir a días.

## Restricted Boltzmann Machines

- Ejecutar una entrada en sentido directo. Observamos la salida en función de la entrada
- Hacer la ejecución en sentido inverso. Tratamos de encontrar la entrada en función de la salida.
- Utilizamos KL Divergence para ajustar los pesos y bias, hasta que las salidas de la red invertida coinciden con las entradas.

Esta es una alternativa al algoritmo de **back propagation**. Una red Deep Belief Net es exactamente como un perceptrón multicapa, pero su método de entrenamiento es completamente diferente.

El algoritmo se entrena de a poco, capa por capa.

### Autoencoder

Un algoritmo que busca reproducir la salida a partir de la entrada. A partir de esta, podemos construir compresores. También podemos utilizarlas para reducir ruido.

## Convolutional Neural Nets

Son redes que dominan completamente la visión espacial.

Estas redes tienen distintas capas, son complejas:

- **Cada de Entrada:** neurona de entrada está conectada con la información de un pixel.
- **Capa Convolucional:**
	- Hay una capa de múltiples niveles, donde cada neurona está conectada con múltiples neuronas de entrada
	- Todas las neuronas de la cada nivel de esta capa tienen los mismos pesos y configuraciones que el resto de neuronas del mismo nivel
- **Capa RELU:** Una capa de activación que se entrena con backpropagation
- **Capa Pooling:** Una capa que reduce la dimensionalidad de la entrada
- **Capa Fully Connected:** Perceptrón final de dos capas que clasifica la salida.

**Convolución:** Es una forma de combinar dos funciones en una función nueva. Podemos decir que le aplica la función a la entrada para obtener una entrada simplificada. Por ejemplo, detectar líneas de una imagen

**Relu:** Es una función de activación. devuelve el máximo entre la entrada y el valor cero.

**Pooling:** Por lo general funciona de dos formas, puede devolver tanto la entrada máxima como la entrada promedio.

## Redes Recurrentes

Son útiles cuando los patrones de los datos cambian con el tiempo. Pueden recibir una secuencia de valores de entrada y devolver una secuencia de valores de salida. Las capas están conectadas en secuencia, donde cada capa puede tener una o múltiples neuronas.

![[Redes de Aprendizaje Profundo 1.png]]

Se conoce como celdas de memoria, a la parte de una red neuronal que mantiene algún estado a lo largo de los pasos de tiempo.

Este tipo de redes se puede utilizar para clasificar vídeos cuadro a cuadro, o predecir acciones. Utilizando componentes temporales.

También se puede utilizar para la clasificación de documentos. A veces, ignoramos todas las salidas exceptuando la salida final.

Para el etiquetamiento de imagen, podemos hacer que la entrada sea siempre la misma. En cada ciclo se genera una palabra para el título de la imagen.

Las redes hacia adelante se utilizan para clasificación o predicción, pero las redes recurrentes se utilizan para series, predicciones y pronosticó.

### Costo

Las redes recurrentes profundas son costosas, Es como entrenar una red con muchas capas de alimentación hacia adelante.

Para solucionar esto, se encontraron algunas soluciones:

- Gating: Celdas de memoria con mecanismos internos para facilitar el calculo
	- LSTM
	- GRU
- Gradient Clipping
- Better Optimizers
- Steeper Gates

## Recursive Neural Tensor Net

Tienen estructuras de neuronas en forma de un árbol. El nodo raíz genera un *score* que es vuelto a ingresar en los nodos hojas, de forma recursiva. Los nodos hojas reciben una entrada y devuelven un score a su nodo padre. Esto se repite sucesivamente sumando entradas hasta llegar a un score final.

Para entrenar estas redes, se utiliza back propagation.

Se puede utilizar para diversos casos:

- Reconocimiento de imágenes
- Análisis gramatical
- Deteccion de cancer
- Radiología
- Finanzas
- Detección de fraude

## Deep Fake Nets

Se utiliza para la sustitución de caras en peliculas o imagenes. Para construirlas, se utilizan las *Restricted Boltzmann Machines*

1. Construimos un autoencoder para la imagen de la cara 1
2. Construimos un autoencoder para la imagen de la cara 2
3. Creo un nuevo encoder, con la codificación de un modelo y la decodificación de otro modelo.
4. Tendremos un modelo que puede transformar la cara 1 por la cara 2

## Clasificación de Objetos

Es una red convolucional que se utiliza para la clasificación de imágenes. Consiste en dos etapas:

- Feature Learning: Varias iteraciones de Capas Convolucionales + Relu, seguidos de un pooling.
- Clasificación: Utiliza la función softmax para devolver probabilidades de pertenecer a cada clase

## Generative Adversarial Networks

Son redes neuronales profundas no supervisadas que generan datos nuevos:

- Puede generar datos totalmente nuevos
- Completar datos faltantes de una observación.
- Transformar datos en otros datos:
	- Foto → Pintura
	- Zebras → Caballos

Funcionamiento:

1. Tendremos una red convolucional que recibe una entrada de datos. Esta red convolucional nos devuelve si es una foto real o no.
2. Por otro lado, tendremos una generador. Una red convolucional inversa, partimos de ruido y generamos una imagen.
3. Aquellas imágenes generadas que no sean detectados como imagen, serán devueltos al generador para que actualice sus pesos.

![[Redes de Aprendizaje Profundo 2.png]]

### ProGAN

Genera imágenes de alta calidad, pero en la mayoría de los modelos no puede controles las características específicas de la imagen generada
