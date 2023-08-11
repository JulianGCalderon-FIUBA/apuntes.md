Un sistema numérico es un conjunto de símbolos y reglas para su organización.

- **Sistema Numérico Posicional:** Es relevante la posición de un símbolo en el cálculo de su peso.
- **Sistema Numérico no Posicional:** No es relevante la posición de un símbolo en el cálculo de su peso.

Estos sistemas utilizan **punto fijo** para representar los decimales.

## Definiciones

- **Base de un Sistema:** Cantidad de símbolos
- **Posición de un Símbolo:** Se cuenta de derecha a izquierda y empieza desde el 0, las posiciones decimales son negativas
- **Peso de un Símbolo:** $\text{Peso} = \text{Base}^\text{Posicion}$

## Precisión

Si tengo $n_1$ decimales en la base $b_1$, necesito $n_2$ decimales en la base $b_2$

$$
b_1^{n_1} = b_2^{n_2} \implies n_2 = n_1 \cdot \frac{\log B_1}{\log B_2}
$$

Como no puedo tener una cantidad no natural de dígitos, se redondea para arriba.

Se utiliza para saber cuantos decimales necesito en cierta base para tener una precisión de tantos decimales en base 10

## Punto Fijo

Este sistema divide la parte fraccionaria de un número en sumas de potencias de ese número.

Por ejemplo: $0.75 = \frac 12 + \frac 14$, o $0.825 = \frac 12 + \frac 14 + \frac 18$, o $0.625 = \frac 12 + \frac 18$.

Este método no es muy preciso, ya que hay algunos números que nunca podrán ser representados de esta forma. Por ejemplo: $0.2$.

Los números de punto fijo son números enteros, multiplicados por una constante $2^{-n}$, que traslada la coma $n$ posiciones.
