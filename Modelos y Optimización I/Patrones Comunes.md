## Problemas de Centros de Producción

En este tipo de problemas, la producción se divide en distintos lugares físicos (llamados centros) en cada uno de los cuales se realizan distintas partes del proceso. Para modelar estas situaciones, plantearemos las variables de entrada y de salida de cada centro, relacionado con los centros siguientes.

## Problemas de Mezcla (Blending)

En este tipo de problemas, ciertos insumos se deben mezclar con proporciones específicas para producir bienes. La suma de los insumos da como resultado un nuevo producto.

$$
Y = x_1 + x_2 + x_3 + x_4
$$

$$
x_1 = \alpha Y
$$

$$
x_3 \geq \gamma Y
$$

$$
x_2 \leq \beta Y
$$

$$
 \sigma Y \leq x_3 \leq \delta Y
$$

## Problemas de Armado

En este tipo de problemas, debe fabricar un producto utilizando una determinada cantidad de otros productos. A diferencia del problema de mezcla, la suma de los insumos no da como resultado el producto. Para indicarle al problema que un producto $Y$ necesita una cantidad exacta de recurso $x$, es a partir de la siguiente relación.

$$
x_1 = \alpha Y
$$

$$
x_1 = \gamma Y
$$

$$
x_1 = \beta Y
$$

$$
x_1 = \delta Y
$$

## Condiciones de un modelo

Las condiciones de un modelo relacionan actividades entre sí o con el contexto. Existen tres tipos distintos:

- **Fuertes:** Deben ser cumplidas siempre
- **Débiles:** Pueden no cumplirse a un cierto costo
- **Conflictivas o contradictorias:** Múltiples condiciones no pueden cumplirse simultáneamente.

## Programación de Metas

Para resolver condiciones débiles, utilizamos programación de metas. Esta nos permite separar una variable en dos estados. Si $X > \lim$, se impone un costo adicional.

$$
X - \lim = \text{Exceso} - \text{Defecto},\quad
\text{Exceso} \leq 0,\text{Defecto} \leq 0
$$

Sí se cumple $X \leq \lim$, entonces $\text{Defecto} = \lim - X$, con $\text{Exceso} = 0$. Por el otro lado, cuando se cumple que $X > \lim$, entonces $\text{Defecto} = 0$, con $\text{Exceso} = X - \lim$.

Sin embargo, esto solo se puede realizar si la utilización de $\text{Defecto}$ es más ventajoso que la utilización de $\text{Exceso}$, de modo que priorice primero la utilización de este. Para otros casos, necesitamos utilizar variables bivalentes.

## Problemas con varios Períodos

En estos casos, no utilizamos la hipótesis "todo lo que se produce se vende", ya que muchas veces dejaremos producto producido en un mes para ser vendido el mes siguiente. Muchas veces esto permite al modelo producir con antelación, para cumplir requisitos en periodos posteriores.

Podemos relacionar el producto a lo largo de los periodos con la siguiente ecuación

$$
V_i + A_i = P_i + A_{i-1}
$$

Esta ecuación puede ser modificada para, por ejemplo, definir un stock inicial para el primer periodo, o un stock final para el último.

## Programación de Tareas

Para los casos donde debemos distribuir tareas a lo largo de un perdido, podemos definir variables para la cantidad de tareas/empleados asignados en cada subperiodo necesario.

## Rotación de Tareas

Si debemos distribuir $n$ elementos en $m$ tareas disponibles, comenzaremos primero por separar en la cantidad de elementos asignados a cada tarea, siendo el total no mayor a la cantidad de elementos totales. Luego, podemos imponer restricciones individuales sobre cada grupo.

Para la rotación de tareas, debemos definir para cada elemento del periodo anterior, la tarea que tendrá asignada en el periodo siguiente (a veces, podemos considerar una tarea "nula" que representa aquellos elementos que no realizaran trabajo en cierto periodo).

Una vez hecha esta nueva división, podemos volver a agrupar los elementos según la tarea actual.

## Restricción Financiera

Si en un modelo mensual cobramos el producto un tiempo después, entonces debemos tenerlo en cuenta en el funcional. Sin embargo, si contamos con la restricción que necesitamos $\$X$ en la caja a fin del periodo, estos ingresos por venta no los puedo contar como ingreso de caja, ya que no los obtendré en el periodo a analizar.

Sea $C_0$ el valor de caja inicial, $C_i$ los ingresos de caja, $C_e$ los egresos de caja, y $C_f$ el valor de caja a alcanzar. Entonces, podemos plantear la siguiente ecuación para hallar el exceso y el defecto

$$
(C_0 + C_i - C_e) - C_f = \text{Exceso} - \text{Defecto}
$$

Cuando los intereses se pagan (o cobran) vencidos, no son egresos (o ingresos) de caja, pero cuando estos se pagan (o cobran) por adelantado, si lo son.
