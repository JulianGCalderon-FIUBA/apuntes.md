Este TDA se encarga de recorrer secuencialmente los datos almacenados en la lista.

Existen dos tipo de iteradores:

- Iterador Interno
- Iterador Externo

## Iterador Interno

Permite recorrer todos los elementos de una lista sin controlar el ciclo en el cual recorre el mismo. Lo que hace es aplicar a cada elemento de la lista una función con el parámetro indicado. Nosotros debemos definir la función a aplicar con los parámetros necesarios.

Para pasar multiples parámetros, tenemos distintas opciones

- Definir un `struct` personalizado que contenga los parametros necesarios
- Crear un arreglo de punteros void: `void *parametros[CANTIDAD_PARAMETROS]`
- Con un **TDA lista**

## Iterador Externo

Este iterador es un TDA que provee una serie de primitivas y operaciones para recorrer la estructura. Para eso consta de una lista la cual recorre y el elemento actual de la lista.

Están definidas las siguientes funciones:

- `crear()`
- `siguiente()`
- `elemento_actual()`
- `tiene_siguiente()`
- `primer()`
