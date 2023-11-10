Los parámetros en los lenguajes de programación se pueden pasar de distintas formas.

## Pasaje por Referencia / Variable

Como parámetro pasa el identificador de una variable, en lenguajes imperativos, esto permite mutar el valor de las variables enviadas.

El pasaje por variable es un caso especial, cuando el identificador es una celda.

## Pasaje por Valor

El valor de la variable se copia por cada llamada a la función. Las modificaciones que se hacen son invisibles a quien llama al procedimiento.

## Pasaje por Valor - Resultado

Parecido al pasaje por variable. El contenido es puesto en una nueva celda, y cuando finaliza, recién ahí, se pone en la variable que llego por parámetro. De esta forma, es imposible observar resultados intermedios.

## Pasaje por Nombre

Crea un *procedure value* por cada parámetro. Cada vez que se necesita el parámetro, se ejecuta el procedimiento.

## Pasaje por Necesidad

Variante del pasaje por nombre, pero solo se evalúa el parámetro la primera vez que lo necesita.
