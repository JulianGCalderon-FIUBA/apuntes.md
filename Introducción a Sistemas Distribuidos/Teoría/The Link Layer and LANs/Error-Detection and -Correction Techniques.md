Incluso con el uso de bits EDC *(error detection and correction bits)*, un remitente puede enviar un datagrama corrupto a la capa de red, inconsciente de que los contenidos del paquete fueron corrompidos. Analizaremos tres técnicas conocidas:

## 1. Parity Checks

El remitente incluye un bit adicional que indica que la cantidad de unos del paquete completo es un par (o impar) (esto incluye el propio bit de paridad). Si ocurre una cantidad impar de errores, entonces este error es suficiente. Si este número es par, entonces no se detectara el error.

Si la probabilidad de error del enlace es pequeña, esta técnica será suficiente, ya que la probabilidad de dos errores es baja. Sin embargo, se encontró que cuando ocurre un error de un bit, suele ocurrir más de uno. En condiciones de errores en ráfaga, la probabilidad de detectar errores con esta técnica será de 50%.

En la generalización bidimensional del esquema de paridad, los datos se separan en $i$ filas, y $j$ columnas. Se calcula un valor por cada columna y por cada fila. Los resultantes $i+j+1$ bits de paridad serán utilizados para la detección de errores.

![[Error-Detection and -Correction Techniques 1693351685.png|442]]

Si ocurre un solo error, entonces podremos utilizar la combinación de filas y columnas para invertir el bit corrupto. Si ocurre más de un error, esto no podrá realizarse, pero esto permite capturar los errores cuando ocurrió una cantidad par de ellos.

La habilidad del receptor de detectar los errores y poder corregirlos se conoce como **forward error correction (FEC)**. Son usualmente utilizadas en dispositivos de almacenamiento y reproducción de audios.

## 2. Checksumming Methods

En estas técnicas, los **frames** son tratados como una secuencia de enteros de $k$ bits. Se suman los enteros y el resultado es guardado en los bits de EDC.

El **checksum** de internet es basado en este enfoque, donde se toman enteros de 16 bits para los datos del paquete, se suman, y su complemento a 1 es guardado en el *checksum*. De esta forma, si sumas los datos del paquete, deberías obtener todos los bits en 1. Si ocurrió un error, se tendrá al menos un bit en 0.

## 3. Cyclic Redundancy Check (CRC)

Esta técnica consisten en la utilización de **cyclic redundancy check codes**, conocidos como *polynomial codes*.

En primer lugar, tanto el remitente como el receptor deben acordar en un patrón de $r{+}1$ bits, conocido como un generador, el cual denotaremos como $G$. Es necesario que el bit más significativo del patrón sea un uno.

Por una cadena de datos $D$, el remitente agrega $r$ bits adicionales, de forma que el patrón resultante sea divisible por $G$. Utilizando aritmética en módulo dos. Si los bits recibidos por el receptor también son divisibles por $G$, entonces se concluye que no hay errores.

Esta técnica puede detectar errores en ráfaga de menos de $r+1$ bits, además, una ráfaga de errores mayor a esta longitud, es detectada con probabilidad $1{-}0.5r$.
