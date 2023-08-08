La recursividad es un método para solucionar problemas, que consta en repetir el mismo algoritmo en situaciones cada vez mas sencillas, hasta llegar a un caso base.

Se divide en dos partes:

- **Bajada,** voy simplificando el problema hasta llegar al caso base
- **Subida**, resuelvo el problema

Cada vez que se llama una función, se crea un ámbito nuevo y se va apilando en el stack de ejecución hasta que termine de ejecutarse la llamada.

Toda función iterativa puede volverse recursiva, pero no toda función recursiva puede volverse iterativa.

![[Apuntes/Algoritmos I/Attachments/Recursividad 1.png|Recursividad%2035c0a614b2c94cbbb90af315935b717d/Untitled.png]]

```c
long factorial(int n){
	if (n <= 0){
		return 1;
	} else {
		return n * factorial(n-1);
	}
}
```

# Ejemplos de Recursividad

```c
//POST: La sumatoria desde 'numero' hasta 0
long suma(int numero){
	if (numero <= 0){
		return 0;
	}
		return numero + suma(numero-1);
}
```

```c
//POST: Cantidad de pares desde 0 hasta 'numero'
long cuantos_pares(int numero, int i){
	if (i==numero){
		if ( i%2 == 0){
			return 1;
		} else {
			return 0;	
		}
	} else {
		if ( i%2 == 0){
			return 1 + cuantos_pares(numero, i+1);
		} else {
			return 0 + cuantos_pares(numero, i+1);	
		}
	}
}
```

```c
//Imprime todos los numeros desde 0 hasta 'numero', de forma ascendente.
void imprimir_ascendente(int numero){
	if (numero >= 0){
		imprimir_ascendente(numero-1);
		printf("%i", numero);
	}
}
```

```c
//Imprime todos los numeros desde 0 hasta 'numero', de forma descendente.
void imprimir_descendente(int numero){
	if (numero >= 0){
		printf("%i", numero);	
		imprimir_ascendente(numero-1);
	}
}
```

## Recursividad Avanzada

```c
//POST: Cantidad de caracteres desde indice 'i' hasta final de 'string'
int longitud_string(char string[], int i){
	if (string[i] == '\0'){
		return 0;
	} else {
		return 1 + longitud_string(string, i+1);
	}
}
```

```c
//Imprime todos los elementos de 'vector', a partir de 'indice'
void imprimir_vector_aux(int vector[], int tope, int indice){
	if  (indice!= tope){
		printf("%i\n", vector[indice]);
		imprimir_vector_aux(vector, tope, indice+1);
	}
}

//Imprime todos los elementos de 'vector'
void imprimir_vector(int vector[], int tope){
	imprimir_vector_aux(vector, tope, 0);
}
```