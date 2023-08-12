## Definición

Un **diccionario** es una colección de pares [clave, valor]. Se accede a los elementos mediante una clave, que funciona como índice. También es conocido como un ***hashmap***.

La utilidad del diccionario es que aumenta el rendimiento a la hora de acceder a valores. En los diccionarios, no hay entradas duplicadas.

Un **hash** es una estructura que contiene valores, puedo acceder a estos valores a partir de una clave. La función que convierte una entrada en un índice de la tabla se denomina **Función Hash.**

Esta función puede tener colisiones, es decir. Distintas claves que redireccionan al mismo índice.

## Clasificación de Hash

### Hash Abierto

Un hash abierto, o de direccionamiento cerrado. Es aquel en el que el elemento se encuentra obligatoriamente en el índice de su clave.

Se denomina **abierto** porque depende de una estructura externa al hash. Cada posición del hash apunta a una lista que contiene todos los valores que direccionan a esa posición.

Como se utiliza una lista con nodos (cada elemento de la lista apunta al siguiente), se denomina *Chaining* o *Encadenamiento*.

### Hash Cerrado

En un hash abierto, o de direccionamiento abierto, todos los valores se guardan en la misma tabla. Esto implica que, cuando hay una colisión, se debe redireccionar la clave hacia el índice siguiente.

Se denomina **cerrado** porque no depende de una estructura externa.

#### Métodos de Búsqueda

- **Probing Lineal:** Buscar el siguiente espacio libre inmediato
- **Probing Cuadrático**: Utilizar un polinomio para encontrar el siguiente espacio libre
- **Hash Doble**: Aplicar una segunda función hash a la clave cuando hay colisión

#### Factor de Carga

El factor de carga $\alpha$ indica el grado de ocupación de la tabla del hash. Es decir, nos dice que tan probable es de encontrar una colisión

$$
\alpha = n/m
$$

Siendo $n$ el número de claves almacenadas actualmente y $m$ la capacidad de la tabla el hash.

#### Rehash

Cuando $\alpha ≥ 0.75$, es hora de rehashear. Esto implica aumentar la capacidad de la tabla de hash. Podemos, por ejemplo, duplicar la capacidad.

Cómo aumentamos la capacidad, debemos reorganizar los elementos acorde a la nueva capacidad. Nuestra función hash debe ser moldeable a la capacidad de la tabla del hash.

Esta es una operación muy costosa, por lo que debemos minimizar la cantidad de veces que la necesitamos hacer.

### Zona de Desborde

Este es un **hash** cerrado, que utiliza una porción de la tabla para los elementos con colisiones. Este método no es muy efectivo ya que la zona de desborde se encuentra completamente desordenada.

## Operaciones de Hash Cerrado

Vamos a definir las siguientes operaciones:

- Crear
- Insertar
- Quitar
- Obtener
- Cantidad
- Destruir
- Contiene

Si nosotros insertamos un valor en una clave existente, entonces debemos modificar el valor actual. Es una operación de modificación.

Si buscamos un valor y no se encuentra en el hash de su clave, entonces debemos acceder al siguiente hasta llegar a un espacio vacío o hasta el fin de la tabla

Si quitamos un elemento, debemos reorganizar el hash. Avanzamos hasta encontrar un espacio vacío, o una elemento que puede reemplazarlo. Si encontramos un espacio vacío, termina el algoritmo de quitado. Si encontramos una elemento que pueda reemplazarlo, entonces colocamos ese elemento en la posición donde quitamos el elemento y repetimos el algoritmo a partir del elemento movido.
