Cuando queremos más precisión a la hora de representar números decimales, podemos utilizar el sistema de representación de punto flotante. Utiliza la notación científica para representar números.

$$
M \cdot \text{base}^{exp}
$$

Por norma, se usa la base binaria para representar el número.

El principal inconveniente del punto flotante, es que el cero y los valores cercanos a él no pueden ser representados. El cero se representa con un valor especial.

## Componentes

- **Signo:** Representa el signo del número.
- **Mantisa:** Representa el significado del número. Por norma, empieza con $1,d_1d_2d_3 \dots d_n$
- **Exponente:** Representa la magnitud del número (con signo). Se representa con *"exceso".* En el exponente no están permitidos los extremos del rango de representación. No admite todos ceros ni todos unos.

![[Punto Flotante 1693351678.png]]

Formatos típicos de los números de máquina.

### Representación en Exceso

Si se tienen 4 bits, Parte del -7 con todos los bits en 0. Luego va sumando uno por uno hasta llegar al 7 positivo. El número inicial depende de la cantidad de bits del número.

La ventaja de este sistema de representación es que es más fácil comprar exponentes.

## Valores Especiales

- **Cero:** Todos los bits en cero. (no importa el signo)
- **Infinito:** Exponente: Todos unos, Mantisa: Todos ceros. (no importa el signo)
- **NaN**: Exponente: Todos unos, Mantisa: ≠ 0 (no importa el signo)

## Sumar en Punto Flotante

Esta operación es muy costosa, mucho menos efectiva que en punto fijo.

1. Calcular la diferencia $d$ de exponentes (cuál es mayor)
2. Correr $d$ posiciones a la derecha la coma del número mayor
3. Sumar las mantisas
4. El exponente del resultado es el del número mayor
5. Normalizar la mantisa, ajustando el exponente de ser necesario.
