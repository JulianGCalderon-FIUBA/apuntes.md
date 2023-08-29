**Magnitud Física:** atributo de un cuerpo que puede determinarse cuantitativamente

Separaremos un valor $x$ en su valor representativo $<x>$, y su cota de error $\Delta x$, o incerteza absoluta.

$$
x = <x> \pm \Delta x
$$

El resultado de una medición es un intervalo, que tiene en cuenta la imprecisión del artefacto medidor.

También podemos calcular la incerteza relativa, según $\displaystyle \varepsilon = \frac{\Delta x}{x}$

## Clasificación de mediciones

- Medición directa: Medir a partir de un objeto:
- Medición indirecta Medir a partir de relaciones matemáticas

## Cifras Significativas

Es el número de dígitos contenidos en el resultado de la medición que están a la izquierda del primero dígito afectado por el error

- Todos los dígitos distintos de cero son cifras significativas
- Los ceros que están entre dos dígitos distintos de cero son cifras significativas
- Los ceros situados después de la coma y a la derecha de un dígito distinto de cero son cifras significativas
- los ceros a la izquierda del primer dígito distinto de cero no son cifras significativas
- Para números enteros, los ceros situados a la derecha del último dígito distinto de cero pueden o no ser cifras significativas

## Aproximaciones

- **Aproximación en medición directa:** Valor medio de las incertezas absolutas y los valores representativos. Las incertezas absolutas solo pueden tener una cifra significativa, se redondea el número.
- **Aproximación en medición indirecta:** Utilizaremos las derivadas para hallar el error:

	$$
	\Delta y = \frac{\partial y}{\partial x_1}\Delta x_1 + \frac{\partial y}{\partial x_2}\Delta x_2 + \dots + \frac{\partial y}{\partial x_n}\Delta x_n
	$$

	$$
	\Delta y = \varepsilon \cdot y
	$$

## Clasificación de incertezas

- Sistemáticas: Imperfección del instrumento. Asociadas a estas, está la exactitud del instrumento. La exactitud de un instrumento es la calidad de calibración del mismo
- Accidentales: Son distintas en cada medición. La precisión de un instrumento es la menor variación de la magnitud que detecta el mismo.
