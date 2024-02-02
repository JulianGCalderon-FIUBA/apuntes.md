## Selección

Consta en buscar el elemento de menor valor del arreglo e intercambiarlo con el elemento que está en la primera posición, repitiendo este algoritmo con el resto de posiciones hasta que todos los elementos estén ordenados.

```c
// Ordena los elementos del vector, de forma ascendente.
void seleccion(vector_t vector, int tope){
	for (int i = 0; i < tope; i++){

    int minimo = i;
    for (int j = i + 1; j < tope; j++){

	    if (vector[j] < vector[minimo]){
	      minimo = j;
	    }
    }

    elemento_t aux = vector[i];
    vector[i] = vector[minimo];
	  vector[minimo] = aux;
	}
}
```

## Burbujeo

Este método consiste en ir comparando cada elemento del arreglo con su adyacente, e intercambiarlos si están en el orden incorrecto. Se repite esto hasta que el elemento mayor se encuentre en el extremo, y se repite la pasada hasta que el arreglo esté ordenado.

```c
// Ordena los elementos del vector, de forma ascendente.
void burbujeo(vector_t vector, int tope){
    for (int i = 0; i < tope; i++){

        for (int j = 0; j < tope - i - 1; j++){

            if (vector[j] > vector[j + 1]){
                elemento_t aux = vector[j];
                vector[j] = vector[j + 1];
                vector[j + 1] = aux;
            }
        }
    }
}
```

## Inserción

Se parte de un vector con un solo elemento, y se van agregando uno por uno los nuevos elementos al vector, de forma ordenada. Hasta que el nuevo vector contenga todos los elementos, de forma ordenada.

```c
// Ordena los elementos del vector, de forma ascendente.
void insercion(vector_t vector, int tope){
	for (int i = 1; i < tope; i++){

    int j = i;
    elemento_t aux = arreglo[i];

    while (j > 0 && aux < arreglo[j - 1]){
      arreglo[j] = arreglo[j - 1];
      j--;
    }

    arreglo[j] = aux;
  }
}
```
