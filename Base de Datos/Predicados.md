Los datos no se almacenan como oraciones, sino con relaciones. Separamos los datos en **sujetos** relacionados y agregamos información sobre dicha relación.

Una tabla, luego, es una representación de hechos. Cada fila de la tabla nos dice algo.

Las bases de datos tradicionales almacenan datos de texto o numéricos, que pueden enunciarse a través de proposiciones. Un conjunto de proposiciones con la misma estructura puede tipificarse a través de un predicado.

> [!example]
> Dada la proposición: *"Rogerer Federer ganó el Abierto de Australia en 2018"*. Podemos abstraer un predicado: *"[jugador] ganó el [torneo] en [año]"*.

El predicado puede ser pensado como una función que recibe las variables del mismo, y nos devuelve un resultado. El resultado será verdadero o falso y nos va a indicar si dicha fila se encuentra en la tabla.

Las bases de datos modernas aprovechan estas repeticiones en la estructura de datos para poder almacenar información de forma eficiente. La clave para el manejo de la complejidad es el concepto de **abstracción**.

## Lógica de Predicados

La lógica de predicados de primer orden se basa en tres componentes:

- **Predicados:** Son funciones de una o más variables cuyo resultado es un valor de verdad (verdadero o falso).
- **Operaciones** entre predicados: $\land$, $\lor$, $\neg$, $\to$.
- **Cuantificadores** de variables: Existen dos cuantificadores:
	- Cuantificador universal: $(\forall m)q(m)$. Es verdadero si para cualquier valor de $m$, el predicado $q(m)$ es verdadero
	- Cuantificador existencial: $(\exists m)q(m)$. Es verdadero si existe al menos un valor de $m$ para el cual el predicado $q(m)$ es verdadero.
