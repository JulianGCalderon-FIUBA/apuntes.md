Es una red que trabaja con secuencias. La salida de una neurona es alimentada a la siguiente de forma sucesiva

![[Redes Recurrentes 1.png]]

![[Redes Recurrentes 2.png]]

Tendremos entonces un conjunto de $n$ entradas y un conjunto de $n$ salidas, estas entradas son analizadas en secuencia.

Para hacer esto, cada neurona recurrente tiene dos entradas, la entrada usual, y otra entrada que sería la salida del paso anterior. Tendremos los siguientes componentes:

- Matriz de pesos para X
- Matriz de pesos para Y
- Función de activación
- Vector de bias

Son también llamadas celdas de memoria, ya que …. ALGO

Si solo nos interesa el resultado final, por ejemplo en clasificación de textos. Entonces podemos ignorar todas las salidas exceptuando la última.

También puede ser utilizada para clasificación de imagen, enviándole la misma imagen a todas las entradas.

## Entrenamiento

Para entrenarla, primero debemos desplegarla en el tiempo y luego utilizar back propagation.

Solemos calcular la pérdida para las últimas $T$ salidas.

## Series de Tiempo

Son una secuencia de números que representan valores en orden temporal. Para predecir valores $n$ pasos adelante, podemos alimentar la red recurrente con las predicciones anteriores ($n-1$). A medida que avanzamos en el tiempo perdemos precisión.

Otra alternativa es que la ultima neurona tenga $n$ salidas.

## Métricas

El enfoque **naive** para analizar el error es comprar con el último valor de una secuencia ya conocida

## Problemáticas

- Existe el desvanecimiento del gradiente: Las mejoras se hacen cada vez menores
- Gradientes inestables: No convergen
- Memoria a corto plazo: Cuando la secuencia es demasiado larga, pierde eficacia. No puede recordar tantas entradas. Algunas soluciones son:
	- Celdas LSTM
	- Celdas GRU
	- Celldas GRU + Redes Convolucionales

## LSTM: Long Short-Term Memory

Estas celdas suelen ser mas rapidas, y con mayor memoria.

![[Redes Recurrentes 3.png]]

Tiene una entrada $c$, llamada entrada a largo plazo. Permite tener más memoria debido a esta nueva entrada.

La puerta del olvido controla que partes de la entrada a largo plazo se van a olvidar

La puerta de entrada controla que parte de la entrada se van a sumar

La puerta de salida controla que partes continúan a la siguiente neurona, como entrada a corto plazo

## GRU: Gated Recurrent Unit

Versión simplificada de la versión anterior, pero funciona igual de bien

![[Redes Recurrentes 4.png]]

No tendremos una entrada a largo plazo. La puerta del olvido y de entrada se simplificaron en una sola, o bien borro recuerdos, o sumo recuerdos.

## GRU + Convolucionales

Utilizaremos redes convolucionales de 1D para extraer características de una secuencia de valores. Luego esto alimentará a una red GRU
