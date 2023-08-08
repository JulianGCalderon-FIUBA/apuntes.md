Los errores son una herramienta mas, no deben pensarse como algo negativo. No se pueden ignorar y hay que trabajar con ellos.

# Fuente de Errores

- **Redondeo:** La computadora desprecia decimales.
- **Inherente:** El error viene de la percepción humana al medir.
- **Truncamiento:** Ocurre cuando se desprecian términos de una serie.

A diferencia de redondeo, en truncamiento se desprecian términos de forma consiente.

# Términos

- **Error Absoluto:** Diferencia entre el valor real y el valor medido. $e_a = x - \overline x$
- **Cota:** El valor máximo que puede tener nuestro error absoluto. $\|e_a\| \leq \Delta x$
- **Error Relativo:** Relación entre el error absoluto y la magnitud del valor medido. $e_r = \frac{\Delta x}{x}$
- **Resultado Final:** El resultado final se expresa como $x = \overline x + \Delta x$

La cota se expresa con una sola cifra significativa redondeando hacia arriba mientras que el valor medido se redondea (al mas cercano) hasta el orden de magnitud de la cota

Para calcular la cota de error de una función, se utiliza la siguiente fórmula

$$
\Delta f(a,b, \cdots, z) = \Big|\frac{df}{da}\Big|\Delta a + \Big|\frac{df}{db}\Big|\Delta b + \cdots + \Big|\frac{df}{dz}\Big|\Delta z
$$