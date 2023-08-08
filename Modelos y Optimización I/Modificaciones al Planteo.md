# Agregado de Variables

Se nos presenta la oportunidad de agregar una variable mas al análisis, no se agregan restricciones, pero si coeficientes en las mismas.

Podremos realizar una estimación previa para definir si valdrá la pena producir este recurso.

$$
\text{Lucro Cesante} = \sum \text{Uso Del Recurso $i$ $\cdot$ VM del Recurso $i$}
$$

Esta es una estimación que representa cuanto perderé si me veo forzado a producir una unidad del nuevo. Pero no podemos asegurar su certeza ya que el valor marginal esta pensado para la variación de un solo recurso, y aquí se varían multiples. Esta estimación es menor que el valor real. 

Si el lucro cesante es mayor al beneficio del nuevo producto, no conviene producir el nuevo producto. Si es menor, entonces puede llegar a ser conveniente.

Para definir el beneficio real con certeza, debemos agregar este producto a la tabla óptima pero no directamente (ya que la base esta cambiada). Debemos obtener la matriz de cambio de base que transforme un vector de la primera tabla a su equivalente en la tabla óptima. 

La matriz de cambio de base va a estar formada por las columnas de los vectores de la tabla optima, que en la tabla inicial formaban la matriz identidad. Es un problema con únicamente restricciones de menor igual, este será dado por las variables ***slack***.

Una vez obtenida la matriz, multiplicamos esta por la columna del nuevo producto y la agregamos a la tabla óptima. A partir de allí, continuamos la resolución del método hasta hallar la nueva tabla.

# Agregado de Restricciones

Notamos que al agregar una variable, entonces puede llegar a mejorar el funcional (estamos ampliando el espacio de soluciones). Cuando agregamos una restricción, únicamente reducimos el espacio de soluciones por lo que nunca mejoraremos el funcional. La solución se mantendrá igual, o podrá empeorar.

Inicialmente, podemos analizar si la solución actual cumple la nueva restricción. Si no lo hace, debemos encontrar la nueva solución optima que cumpla con todas las restricciones.

No es posible agregar directamente una fila en el problema inicial, debido a que ya no tendríamos vectores canónicos. Debemos hallar la tabla optima del problema dual y agregar una columna en ella, a partir de la técnica que vimos de agregado de variables (matriz de cambio de base).

En la tabla inicial del dual, los vectores canónicos estaban asociados a variables artificiales, pero estos vectores no se pueden reconstruir desde la tabla óptima del primal. Afortunadamente, sabemos que estas son los vectores de las ***slack***, cambiadas de signo.

Luego, la matriz de base sera las columnas de las ***slack*** de la tabla óptima, cambiadas de signo si la variable ***slack*** tiene una artificial asociada.

Nuevamente, multiplicamos la nueva columna por la matriz de cambio de base y obtenemos la nueva columna en la tabla óptima. Continuamos la resolución del método a partir de la nueva tabla.

# Variaciones en Cadena

Supongamos que se nos ofrece modificar el valor de un términos independiente, y al mismo tiempo variar el valor de los coeficientes del funcional. Para hallar la nueva tabla optima, debemos trabajar aplicando las operaciones en cadena. Tendremos dos procedimientos para resolverlo:

- Desde el problema dual, variamos el termino independiente. Luego pasamos a la tabla primal y variamos los coeficientes del funcional.
- Desde el problema dual, variamos los coeficientes del funcional. Luego pasamos a la tabla dual y variamos el término independiente.

Cual procedimiento utilizamos dependerá del contexto de la situación. Debemos elegir en cada caso el procedimiento que resulte menos trabajoso. Es preferible iniciar con la variación que no modifique la estructura optima de la solución.

# Compraventa de Recursos

Se nos ofrece la oportunidad de intercambiar cierta cantidad de un recurso (ya sea vender recurso, o comprar recurso) por un precio fijo. Una primera aproximación consiste en analizar el valor marginal del recurso.

- Venta: A menor cantidad de producto, el valor marginal solo podrá aumentar, por lo que en el peor caso, este se mantendrá fijo. Si el valor marginal es mayor al precio por unidad ofrecido, no convendrá realizar la venta.
- Compra: De forma análoga, no convendrá realizar el intercambio si el valor marginal es menor al precio por unidad ofrecido.

## Soluciones Alternativas

Si estamos antes tablas optimas alternativas, podremos tener dos tablas optimas (y por lo tanto, dos valores marginales) para un mismo problema. ¿Que valor marginal debemos tomar para realizar este análisis?

Si estamos vendiendo producto, debemos quedarnos con el valor marginal mayor. Si estamos comprando producto, nos quedamos con el valor marginal menor.

## Multiples Propuestas

Se nos ofrecen multiples intercambios, todos convenientes si se analizan de forma individual. Solo podremos seleccionar una de las propuestas.

Si todos los intercambios ofrecen la misma ganancia, ¿que criterio tomamos para preferir uno por sobre el otro? Nos quedaremos con el intercambio que maximiza el rendimiento. Por regla de tres simple, tendremos:

$$
\text{Rendimiento} = \frac{\text{Beneficio}}{\text{Costo}}
$$

Si los intercambios no ofrecen la misma ganancia, la elección dependerá del contexto. Debemos analizar las restricciones económicas de la situación.

# Compra vs. Fabricación

Se nos ofrece la oportunidad de comprar una cierta cantidad de un producto, en lugar de fabricarlo. El precio de fabricación es menor al precio de venta, pero tenemos demanda minima del producto, por lo que es posible que nos convenga comprar unidades de este producto con el fin de destinar recursos a la fabricación de otro producto.

Para simular la compra de estos productos, podemos disminuir la restricción de demanda minima a un precio fijo por unidad.

Recordemos que el valor marginal de un recurso nos indica cuanto esperamos mejorar el funcional si yo “aflojo” en una unidad esa restricción (independiente del sentido de la restricción). En el caso de demanda de un producto, esto será al reducir en una unidad la demanda minima. Debido a esto, al costo de oportunidad de una restricción de demanda minima se lo llama ***costo de oportunidad encubierto***.

Para calcular la ganancia del intercambio, debemos tener en cuenta tres componentes:

- La ganancia calculada por el modelo al aliviar la restricción de demanda minima.
- El precio de compra de los productos (resta).
- El precio de venta de los productos comprados. Estos valores son transparentes al modelo, ya que desde su punto de vista, únicamente se aflojo una restricción.