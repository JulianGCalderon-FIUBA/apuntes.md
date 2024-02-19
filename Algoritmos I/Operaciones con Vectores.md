## Inserción Ordenada

La idea de este algoritmo es poder insertar un elemento dentro de un vector, manteniendo el orden del mismo

```c
/*
 * PRE: tope < MAX_ELEMENTOS
 * Inserta 'elemento' en 'vector', respetando el orden.
 */
void insertar_ordenado(vector_t vector, int *tope, elemento_t elemento){
	int i = *tope;
	while (i > 0 && vector_ordenado[i-1] > elemento){
		vector[i] = vector[i-1]
		i--;
	}
	vector[i] = elemento;
	(*tope)++;
}
```

## Eliminación Ordenada

La idea de este algoritmo es eliminar un elemento dentro de un vector, sin dejar huecos en el medio.

```c
/*
 * Elimina 'elemento' de 'vector', si existe.
 */
void eliminar_ordenado(vector_t vector, int *tope, elemento_t elemento){
	int pos = -1;
	int i = 0;

	while (i < *tope && pos == -1){
		if(vector[i] == elemento){
			pos = i;
		}
	}

	if (pos != -1){
		(*tope)--;
		for(i = pos; i < tope; i++){
			vector[i]=vector[i+1];
		}

	}
}
```

## Búsqueda Lineal

La búsqueda lineal busca sucesivamente cada elemento de un arreglo, hasta encontrar el elemento buscado

```c
/*
 * POST:
 *  / indice del elemento si lo encuentra.
 *  / -1 si no lo encuentra.
 *
 * Busca el elemento ingresado en el vector.
 */
int busqueda_lineal(vector_t vector, int tope, elemento_t elemento_buscado){
	int pos = -1;
	int i = 0;

	while (i < tope && pos == -1){
		if(vector[i] == elemento){
			pos = i;
		}
		i++;
	}

	return pos;
}
```

## Búsqueda Binaria

La búsqueda binaria es un algoritmo más eficiente para buscar elementos, cuando los elementos del arreglo están ordenados.

```c
/*
 * POST:
 *  / indice del elemento si lo encuentra.
 *  / -1 si no lo encuentra.
 *
 * Busca el elemento ingresado en el vector.
 */
int busqueda_binaria(vector_t vector, int tope, elemento_t elemento_buscado){
	int centro;
	int inicio = 0;
	int fin = tope-1;

	int pos = -1;

	while (inicio <= fin && pos == -1){

		centro = (fin+inicio)/2;

		if (elemento_buscado == vector[centro]){
			pos == centro;
		} else if (elemento_buscado < vector[centro]){
			fin = centro-1;
		} else {
			inicio = centro+1;
		}
	}

	return pos;
}
```

## Mezcla

La mezcla consiste en tomar todos los valores de ambos arreglos

```c
void mezcla(vector_t vectorA, int topeA, vector_t vectorB, int topeB,
						vector_t vectorC, int *topeC){
	int i = 0;
	int j = 0;
	*topeC = 0;

	while (i < topeA && j < topeB){
		if (arregloA[i] <= arregloB[j]){
	    resultado[*topeC] = arregloA[i];
	    i++;
		} else {
	    resultado[*topeC] = arregloB[j];
	    j++;
		}
		(*topeC)++;
	}

	while (i < topeA){
		resultado[*topeC] = arregloA[i];
		i++;
		(*topeC)++;
	}

	while (j < topeB){
		resultado[*topeC] = arregloB[j];
		j++;
		(*topeC)++;
	}
}
```

## Unión

La unión es similar a la mezcla, pero el resultado no tendrá elementos repetidos

```c
void union(vector_t vectorA, int topeA, vector_t vectorB, int topeB,
						vector_t vectorC, int *topeC){
	int i = 0;
	int j = 0;
	*topeC = 0;

	while (i < topeA && j < topeB){
		if (arregloA[i] < arregloB[j]){
	    resultado[*topeC] = arregloA[i];
	    i++;
		} else if (arregloA[i] > arregloB[j]){
	    resultado[*topeC] = arregloB[j];
	    j++;
		} else {
			resultado[*topeC] = arregloA[i];
			i++;
			j++;
		}
		(*topeC)++;
	}

	while (i < topeA){
		resultado[*topeC] = arregloA[i];
		i++;
		(*topeC)++;
	}

	while (j < topeB){
		resultado[*topeC] = arregloB[j];
		j++;
		(*topeC)++;
	}
}
```

## Diferencia

La diferencia entre $A$ y $B$ $(A{-}B)$, toma los valores de $A$ que no están en $B$

```c
void diferencia(vector_t vectorA, int topeA, vector_t vectorB, int topeB,
						vector_t vectorC, int *topeC){
	int i = 0;
	int j = 0;
	*topeC = 0;

	while (i < topeA && j < topeB){
		if (arregloA[i] < arregloB[j]){
	    resultado[*topeC] = arregloA[i];
	    i++;
			(*topeC)++;
		} else if (arregloA[i] > arregloB[j]){
	    j++;
		} else {
			i++;
			j++;
		}
	}

	while (i < topeA){
		resultado[*topeC] = arregloA[i];
		i++;
		(*topeC)++;
	}
}
```

## Intersección

La intersección devuelve los elementos que se encuentran en ambos conjuntos

```c
void diferencia(vector_t vectorA, int topeA, vector_t vectorB, int topeB,
						vector_t vectorC, int *topeC){
	int i = 0;
	int j = 0;
	*topeC = 0;

	while (i < topeA && j < topeB){
		if (arregloA[i] == arregloB[j]){
	    resultado[*topeC] = arregloA[i];
	    i++;
			(*topeC)++;
		} else if (arregloA[i] < arregloB[j]){
	    i++;
		} else {
			j++;
		}
	}
}
```
