Un `vector` almacena una colección finita y secuencial, de elementos de un mismo tipo de dato.

- El **tamaño** del vector define la cantidad máxima de elementos que puede llegar a tener
- El **tope** de un vector define la cantidad de elementos significantes que tiene el vector
- El **índice** es la posición en la que se encuentra cada elemento, empieza a contar desde 0.

Las **operaciones** entre vector se hacen elemento a elemento. Existen dos tipos de eliminaciones:

- **Eliminación Física:** Es aquella que consiste en eliminar realmente el elemento del vector
- **Eliminación Lógica:** Es aquella que consiste en marcar como 'eliminado' un elemento del vector, Pero dejándolo en su posición.

```c
int agregar_elemento(int edades[MAXIMO], int *tope, int elemento){
	edades[*tope] = elemento;
	(*tope)++
}

int const MAXIMO = 10;
int edades[MAXIMO] = {12, 23, 34, 45, 56, 67};
int tope = 6;

agregar_elemento(edades, &tope, 78);
```

## Matrices

Una `matriz` es un arreglo de 2 dimensiones, como vectores adentro de un vector. Se comporta como un vector

```c
int matriz[MAX_FILAS][MAX_COLUMNAS] = ...

printf("%i", matriz[i][j])
```
