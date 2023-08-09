Falta aún, calcular la circulación de un campo magnético. Ya vimos que el flujo a través de una superficie cerrada es nulo. El campo es solenoidal.

Si plantemos un campo magnético generado por un hilo infinito, entonces llegamos a que la circulación por una curva cerrada está únicamente relacionada con nuestro movimiento en el sentido de las líneas de campo en $\hat \varphi$.

Esta expresión se denomina **Ley de Ampere** en su forma integral. Es válida únicamente para corrientes estacionarias.

$$
 \oint\limits_{\lambda} \vec B \cdot d\vec l = \mu_0 \cdot I_{S(\lambda)}
$$

Siendo $I_{S(\lambda)}$ la corriente concatenada. Es decir, la corriente que atraviesa toda superficie que tenga como borde la superficie $S$.

Podemos extender esta ley para casos con mas de una corriente, realizando la sumatoria de las corrientes concatenadas.

$$
I_{S(\lambda)} =\sum I_{i\ S(\mathfrak{c})}
$$

Si la corriente atraviesa en el mismo sentido que la normal de la superficie, suma. De lo contrario, resta.

La ley de Ampere no está definida para tramos de corrientes. Para este tipo de corrientes, es necesario resolverlo mediante la integral (Biot y Savart).

Esta ley también puede ser expresada en su forma diferencial.

$$
\vec \nabla \times \vec B= \mu_0 \cdot \vec j
$$

## Calculo del Campo Magnético

Al igual que con ley de Gauss calculábamos el campo eléctrico. Podemos realizar algo parecido con la ley de Ampere.

Al igual que antes, para esto necesitamos la dependencia y la dirección del campo magnético de antemano. Debemos elegir una curva que sea paralela y ortogonal en porciones al campo magnético
