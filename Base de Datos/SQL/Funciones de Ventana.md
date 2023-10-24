Permiten aplicar un procesamiento final a los resultados de una consulta, siguiendo una serie de pasos:

1. Se dividen en grupos, llamados particiones
2. Cada partición se ordena internamente
3. Se cruza información entre las filas de cada partición

A cada atributo del `SELECT` de una consulta se le puede aplicar una función de ventana distinta, o no aplicarle función a alguna.

Esto permite agregar información según el ordenamiento de las filas de la tabla.

## Única Partición

El esquema básico es el siguiente, donde se puede utilizar una función de agregación `f(A)` o una función de ventana `w(A_i,...)`.

```SQL
SELECT atleta, RANK() OVER(ORDER BY tiempo DESC)
FROM ...
```

Esto agrega a cada fila del resultado, una columna dependiente de dicha fila y su orden respecto al resto de filas. Si no se utiliza `ORDER BY` dentro de `OVER`, se tendrá un orden indefinido. Existen múltiples funciones de ventana, como `RANK`, `ROW_NUMBER`, `LAG`, etc.

También se pueden utilizar funciones de agregación como `SUM` y `AVG`. Para este caso, se aplica únicamente para las filas anteriores a la fila actual, según el orden propuesto. Si no se aplica un orden, el comportamiento de las funciones de agregación es el normal.

A diferencia del `GROUP BY`, no agrupa. No cambiará la cantidad de filas en el resultado.

La función de ventana se aplica antes del ordenamiento que pueda hacerse en la cláusula `ORDER BY`.

Si vamos a utilizar una misma ventana múltiples veces, podemos definirla con `WINDOW`.

```SQL
SELECT atelta, RANK() OVER ventana_tiempo
FROM ...
WINDOW ventana_tiempo AS (ORDER BY tiempo DESC)
```

## Múltiples Particiones

En un esquema con múltiples particiones, antes de aplicar cada ventana, se puede agrupar el resultado por el valor de un conjunto de atributos. A cada uno de estos grupos, se lo denomina partición.

```SQL
SELECT pais, producto, RANK() OVER(ORDER BY ...)
FROM ...
```

Para cada producto, se calcula su posición respecto al resto de países, ordenando por cantidad de exportaciones. Se puede pensar como una agrupación dentro de una ventana.
